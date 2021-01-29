import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

xmlurl = input('Enter URL: ')
print('Retrieving',xmlurl)

xmldoc = urllib.request.urlopen(xmlurl)
data = xmldoc.read()
tree = ET.fromstring(data)

counts = list()
for comments in tree.findall('.//count'):
    count = comments.text
    count = int(count)
    counts.append(count)

print('Found:',len(counts))
print('Total:',sum(counts))

