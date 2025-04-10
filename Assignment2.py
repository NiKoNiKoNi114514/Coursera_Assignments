from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


cout = 0
total = 0
tags = soup('span')
for tag in tags:
    if tag.contents[0]:
        total += int(tag.contents[0])
        cout += 1

print("Count", cout)
print("Sum", total)
