import json


def load_data(filepath):
    '''Loads data from json file'''
    with open(filepath, 'r') as handle:
        return json.load(handle)


def serialize_animal(animal) -> str:
    out_string = ''
    name = animal.get('name')
    characteristics = animal['characteristics']
    locations = animal['locations']

    out_string += '<li class="cards__item">'

    if name:
        out_string += f'<div class="card__title">{name}</div>\n'

    out_string += '<p class="card__text">\n'

    if characteristics.get("diet") is not None:
        out_string += f'<strong>Diet:</strong> {characteristics["diet"]}<br>\n'

    if locations:
        out_string += f'<strong>Location:</strong> {locations[0]}<br>\n'

    if characteristics.get('type') is not None:
        out_string += f'<strong>Type:</strong> {characteristics["type"]}<br>\n'
    out_string += '</p>\n'
    out_string += '</li>'
    return out_string


animals_data = load_data('animals_data.json')

# open animals_template html and store it in template
with open("animals_template.html", 'r') as handle:
    template = handle.read()

# loop through json and store wanted data in output string
output: str = ""
for animal in animals_data:
    output += serialize_animal(animal)

# replace string in template with output and store in final_html
final_html = template.replace(
    "__REPLACE_ANIMALS_INFO__",
    output
)

# write final_html to animals.html
with open("animals.html", 'w') as handle:
    handle.write(final_html)

