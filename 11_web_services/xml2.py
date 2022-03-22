import xml.etree.ElementTree as ET

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="9">
            <id>007</id>
            <name>James</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))
print('')

for item in lst:
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:', item.get('x'))
    print('')