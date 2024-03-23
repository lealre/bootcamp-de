import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/15")
data = response.json()

data_types = data['types']
types_list: list = []
for type_info in data_types:
    types_list.append(type_info['type']['name'])

types = ', '.join(types_list)
print(data['name'], types)
