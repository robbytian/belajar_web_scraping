import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.9606866736828e-05, 'date': 'Sat, 8 Jan 2022 23:55:01 GMT', 'inverseRate': 14366.398702887}, 'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 6.1534019509745e-05, 'date': 'Sat, 8 Jan 2022 23:55:01 GMT', 'inverseRate': 16251.173057883}}
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
