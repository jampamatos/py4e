import urllib.request, urllib.parse, urllib.error
import json
import ssl

def main_menu():
  print('JSON EXTRACTOR')
  print("Press 1 for sample data, 2 for actual data, type in an URL or type EXIT to quit:")
  choice = input()
  if choice == '1':
    return 'http://py4e-data.dr-chuck.net/comments_42.json'
  elif choice == '2':
    return 'http://py4e-data.dr-chuck.net/comments_1510271.json'
  else:
    return choice

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
  url = main_menu()
  if url == 'exit':
    print('Thank you for using our service!')
    break
  print('')
  print('Extracting JSON from', url)

  try:
    jsondata = urllib.request.urlopen(url, context= ctx)
  except:
    print('ERROR! Could not retrieve url. Press 1 to retry or any other key to exit.')
    choice = input()
    if choice == '1':
      continue
    else:
      print('Thank you for using our service!')
    break

  data = jsondata.read().decode()
  print('')
  print('Extracted', len(data), 'bytes.')
  info = json.loads(data)

  sum = 0
  count = len(info['comments'])

  for item in info['comments']:
    sum += int(item['count'])

  print('')
  print ('Count:', count)
  print ('Sum:', sum)
  print('')