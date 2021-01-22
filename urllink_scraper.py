import urllib.request
from bs4 import BeautifulSoup
import re

names = list()
togo = list()

url = input('Enter: ')
togo.append(url)
name = re.findall('known_by_(.+)\.html',url)
names.append(name[0])
linkpos = int(input('Enter position: '))
count = int(input('Enter count: '))

while count > 0:
    url = togo.pop()
    print('Retrieving:',url)
    count = count - 1

    html = urllib.request.urlopen(url).read()
    data = BeautifulSoup(html,'html.parser')

    tags = data('a')
    tag = tags.pop(linkpos-1)
    link = str(tag)
    newurl = re.findall('"(.+)"',link)
    name = re.findall('known_by_(.+)\.html',link)
    togo.append(newurl[0])
    names.append(name[0])

print(names)

