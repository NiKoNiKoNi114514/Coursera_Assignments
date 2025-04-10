import urllib.request
import json

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')

info = json.loads(data)
cout = 0
total = 0
for item in info['comments']:
    total += item['count']
    cout += 1

print('Count:', cout)
print('Sum:', total)

