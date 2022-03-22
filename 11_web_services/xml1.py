import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl"> +1 734 303 4456</phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text)
print('Phone Tag Type:', tree.find('phone').get('type'))
print('Email Attr:', tree.find('email').get('hide'))