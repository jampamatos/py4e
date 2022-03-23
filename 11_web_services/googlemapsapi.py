from audioop import add
import urllib.request, urllib.parse, urllib.error
import json


api_key = 42
endpoint = 'http://py4e-data.dr-chuck.net/json?'

while True:
    print('Enter Location or type EXIT to quit:')
    address = input()
    print('')
    if address.lower() != 'exit':
        parameters = dict() 
        parameters['address'] = address 
        parameters['key'] = api_key 
        url = endpoint + urllib.parse.urlencode(parameters)

        print('Retrieving', url + '...')
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters.')

        try:
            js = json.loads(data)
        except:
            js = None
        
        if not js or 'status' not in js or js['status'] != 'OK':
            print('=== ERROR: Failure To Retrieve ===')
            print(data)
            continue
        
        print('')
        lat = js['results'][0]['geometry']['location']['lat']
        lng = js['results'][0]['geometry']['location']['lng']
        place_id = js['results'][0]['place_id']
        print('lat:', lat, 'lng:', lng)
        print('')
        location = js['results'][0]['formatted_address']
        print('Place ID:', place_id)
        print('')
        print(location)
        print('')
    else:
        print("Thank you for using our services!")
        break