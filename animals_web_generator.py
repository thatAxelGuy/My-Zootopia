import json

def load_data(filepath):
    '''Loads data from json file'''
    with open(filepath, 'r') as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in animals_data:
    name = animal.get('name')
    characteristics = animal['characteristics']
    locations = animal['locations']

    if name:
        print("Name: " + name)

    if characteristics.get('diet') is not None:
        print("Diet: " + characteristics.get('diet'))

    if locations:
        print("Location: " + locations[0])

    if characteristics.get('type') is not None:
        print("Type: " + characteristics.get('type'))
    print("\n")
