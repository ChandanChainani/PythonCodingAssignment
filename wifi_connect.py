import sys
from stdiomask import getpass
import wifi

if len(sys.argv) < 2:
    print("Please provide wlan interface name")
    sys.exit(0)

interface = sys.argv[1]

def findWlans():
    return sorted(wifi.Cell.all(interface), key=lambda w: w.signal, reverse=True)[0: 3]

def FindFromSavedList(ssid):
    cell = wifi.Scheme.find(interface, ssid)

    if cell:
        return cell

    return False

def addWlan(cell, password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell(interface, cell.ssid, cell, password)
    scheme.save()
    return scheme

def deleteWlan(cell):
    if cell:
        cell.delete()
        return True

    return False

def connectWlan(cell, password=None):
    if cell:
        savedcell = FindFromSavedList(cell.ssid)

        # Already Saved from Setting
        if savedcell:
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                if password:
                    scheme = addWlan(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except wifi.exceptions.ConnectionError:
                        deleteWlan(cell)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = addWlan(cell)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    deleteWlan(cell)
                    return False

                return cell

    return False

try:
    wlans = findWlans()
    wlans_count = len(wlans)

    print("> Your available wifi networks are:")

    for i in range(0, wlans_count):
        print("> [%d] %s " %(i + 1, wlans[i].ssid))

    wlan_selected = int(input("> Your choice? "))

    if wlan_selected > wlans_count or wlan_selected < 1:
        print('No wifi with given range')
        sys.exit(1)

    wlan_password = getpass(prompt="> Password: ")
    connectWlan(wlans[wlan_selected - 1], wlan_password)
except Exception as e:
    print(e)

