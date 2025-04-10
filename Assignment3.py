import urllib.request
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
try:
    pos = int(input('Enter position: '))
    cout = int(input('Enter count: '))
    print("Retrieving: " + url)
except ValueError or pos <= 0 or cout <= 0:
    print("Invalid value")
    exit()

for i in range(cout):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[pos - 1].get('href', None)
    print("Retrieving: " + url)

print("Final URL: " + url)