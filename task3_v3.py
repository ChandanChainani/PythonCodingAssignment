
def signlatlon(selection):
    if (selection == "N"):
        return 1
    return -1


def parselatlon(instr):
    // Parse strings dd.dd dd:mm.mm dd:mm:ss.ss
    var deg,min,sec,colonIndex,degstr,minstr,str
    str=instr
    colonIndex=str.indexOf(":")
    if (colonIndex==-1){ // dd.dd?
                        if (!isPosNumber(str)){
                            badLLFormat(instr)
                            return 0.
                        } else {
                            return parseFloat(str)
                        }
                        } // falls through if we have a colon 

    degstr=str.substring(0,colonIndex)  //DD
    str=str.substring(colonIndex+1,str.length) //MM...
    if (!isPosInteger(degstr)){
        badLLFormat(instr)
        return 0.
    } else {
        deg=parseFloat(degstr+".0")
    }
    //now repeat to pick off minutes
    colonIndex=str.indexOf(":")
    if (colonIndex==-1){ // dd:mm.mm?
                        if (!isPosNumber(str)){
                            badLLFormat(instr)
                            return 0.
                        } else {
                            min=parseFloat(str)
                            if (min < 60.){
                                return deg+parseFloat(str)/60.
                            } else {
                                badLLFormat(instr)
                                return 0.
                            }  

                        }
                        }// falls through if we have a second colon

    minstr=str.substring(0,colonIndex)+".0"  //MM.0
    str=str.substring(colonIndex+1,str.length) //SS.SS
    if (!isPosNumber(minstr) || !isPosNumber(str)){
        badLLFormat(instr)
        return 0.
    } else {
        if ( (parseFloat(minstr) < 60) && (parseFloat(str) < 60.)){
            return deg+ parseFloat(minstr)/60.+parseFloat(str)/3600.
        } else {
            badLLFormat(instr)
            return 0.
        }
    }

def checkField(name, value):
    latlon=parselatlon(value)
    if (name.substring(0,3)=="lat" and latlon > 90.):
        print("Latitudes cannot exceed 90 degrees")
    if (name.substring(0,3)=="lon" and latlon > 180.):
        print("Longitudes cannot exceed 180 degrees")
    return latlon


