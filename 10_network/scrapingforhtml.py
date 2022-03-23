import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def check_url():
    print('Press 1 for sample and 2 for data to process')
    return_url = input()
    if return_url == '1':
        return 'http://py4e-data.dr-chuck.net/comments_42.html'
    elif return_url == '2':
        return 'http://py4e-data.dr-chuck.net/comments_1510268.html'
    else:
        print('ERROR! Please type in 1 or 2 according to the menu.')
        check_url()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = check_url()
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
tags = soup('span')
for tag in tags:
    # print ('TAG:',tag)
    # print ('CLASS:', tag.attrs.get('class'))
    # print ('Contents:',tag.contents[0])
    # print ('Attrs:',tag.attrs)

    sum += int(tag.contents[0])

print (sum)