import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter URL: ')
print('Retrieving URL', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

info = json.loads(data)
#print(info['comments'])
#print(type(info['comments']))
#print(json.dumps(info, indent=4))
counts = list()
for item in info['comments']:
    count = item['count']
    count = int(count)
    counts.append(count)

print('Found:',len(counts))
print('Total:',sum(counts))

