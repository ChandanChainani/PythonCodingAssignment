import sys
import requests
from bs4 import BeautifulSoup
from pprint import pprint

with open('./search_repos.html') as f:
    html = f.read()
if len(sys.argv) == 1:
    response = requests.get("https://github.com/vinta/awesome-python")

    if (response.status_code != 200):
        print("Not able to connect to resource")
        sys.exit(1)

    html = response.text
soup = BeautifulSoup(html, 'html.parser')
# search_result = soup.find("a", string="graphene")
# print(search_result)
d = {}
for a in soup.select("article ul li a"):
    d[a.get_text()] = a
search_string = input("> Query? ")

search_result = d.get(search_string, None)

if search_result:
    print("> Output: ", search_result['href'])
else:
    print("No match found")

