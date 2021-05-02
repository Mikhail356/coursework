import aiosqlite
import mf2py
import mf2util
import json
import sys
import requests
import bs4

if len(sys.argv) < 2:
  print("Err inp parametres:", sys.argv[0], "URL-link")
  sys.exit()
try:
  requests.get(sys.argv[1])
except OSError:
  print('Not correct url')
  sys.exit()

fil = requests.get(sys.argv[1])
fil.encoding = "html5lib"
soup = bs4.BeautifulSoup(fil.text, features="html5lib")
print(soup.prettify)

for link in soup.find_all('a'):
    print(link.get('href'))