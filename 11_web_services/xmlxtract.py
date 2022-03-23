import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

def main():
  print('XML EXTRACTOR')
  print('')
  print("Press 1 for sample data, 2 for actual data, type in an URL or type EXIT to quit:")
  choice = input()
  if choice == '1':
    return 'http://py4e-data.dr-chuck.net/comments_42.xml'
  elif choice == '2':
    return ' http://py4e-data.dr-chuck.net/comments_1510270.xml'
  else:
    return choice

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
  url = main()
  if url == 'exit':
    print('Thank you for using our service!')
    break
  print('')
  print('Extracting XML from', url)
  
  try:
    xml = urllib.request.urlopen(url, context= ctx)
  except:
    print('ERROR! Could not retrieve url. Press 1 to retry or any other key to exit.')
    choice = input()
    if choice == '1':
      continue
    else:
      print('Thank you for using our service!')
    break

  data = xml.read().decode()
  print('')
  print('Extracted', len(data), 'bytes.')
  tree = ET.fromstring(data)
  sum = 0
  list = tree.findall('comments/comment')
  count = tree.findall('.//count')
  for item in list:    
    sum += int(item.find('count').text)
  print('')
  print ('Count:', len(count))
  print ('Sum:', sum)
  print('')