import json

input = '''[
    {
        "id": "001",
        "x": "2",
        "name": "Chuck"
    },
    {
        "id": "007",
        "x": "9",
        "name": "James"
    }
]'''

info = json.loads(input)
print("User count:", len(info))
print('')
for item in info:
    print("Name:", item['name'])
    print('ID:', item['id'])
    print('Attribute:', item['x'])
    print('')