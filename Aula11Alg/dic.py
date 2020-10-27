import requests
import json


d = {}
d['chave1'] = 34.5
d['chave2'] = ['valor1', 'valor2']
d['chave1'] = 24.5


for key in d: #d.keys() também é aceito
    print(key) #imprimi só a chave
    print(d[key]) #imprimi apenas o valor


names = ['Lucas', 'João', 'Pedro', 'Maria', 'Fernanda']

for name in names:
    r = requests.get(f'https://api.agify.io/?name={name}')
    json_response = r.json()
    print(f'Type:{type(json_response)} - Response: {type(json_response)}')

recipes = requests.get('https://api.punkapi.com/v2/beers')
json_response = recipes.json()
print(json.dumps(json_response, indent=4))

