import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def main_menu():
    print('Enter URL or select 1 for sample data or 2 for final problem')
    selection = input()
    if selection == '1':
        return 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    elif selection == '2':
        return 'http://py4e-data.dr-chuck.net/known_by_Suze.html'
    else:
        return selection

def enter_num():
    try:
        return int(input())
    except:
        print ('Please enter an integer number.')
        return enter_num()

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = main_menu()
try:
    html = urllib.request.urlopen(url, context=ctx).read()
except:
    print("Error with provided URL")
    print("Select 1 to retry or any other key to quit")
    exc_selection = input()
    if exc_selection == '1':
        main_menu()
    else:
        quit()

print ("Enter count:")
count = enter_num()
print ("Enter position:")
pos = enter_num() - 1

for i in range(count):
    soup = BeautifulSoup(html, 'html.parser')
    temp_link = list()
    tags = soup('a')
    for tag in tags:
        temp_link.append(tag.get('href', None))
    print('Retrieving:', temp_link[pos])
    html = urllib.request.urlopen(temp_link[pos], context=ctx).read()
