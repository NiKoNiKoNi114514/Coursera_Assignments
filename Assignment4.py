import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter location: ')

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//count')
nums = list()
for result in counts:
    nums.append(int(result.text))

print('Count:', len(nums))
print('Sum:', sum(nums))

