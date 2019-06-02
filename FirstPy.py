import json

with open('USD.json')as f:
    data=json.load(f)

print('Base Dollars:' + data['base'])