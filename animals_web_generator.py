import json

def load_data(filepath):
    '''Loads data from json file'''
    with open(filepath, 'r') as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

# open animals_template html and store it in template
with open("animals_template.html", 'r') as handle:
    template = handle.read()

# loop through json and store wanted data in output string
output: str = "" # empty output string
for animal in animals_data:
    name = animal.get('name')
    characteristics = animal['characteristics']
    locations = animal['locations']

    output += '<li class="cards__item">'

    if name:
        output += f'<div class="card__title">{name}</div>\n'
        output += f"<div class=card__title>{name}</div>\n"

    output += "<p class=card__text>\n"

    output += '<p class="card__text">\n'

    if characteristics.get("diet") is not None:
        output += f'<strong>Diet:</strong> {characteristics["diet"]}<br>\n'

    if locations:
        output += f'<strong>Location:</strong> {locations[0]}<br>\n'

    if characteristics.get('type') is not None:
        output += f'<strong>Type:</strong> {characteristics["type"]}<br>\n'
    output += '</p>\n'
    output += '</li>'

# replace string in template with output and store in final_html
final_html = template.replace(
    "__REPLACE_ANIMALS_INFO__",
    output
)

# write final_html to animals.html
with open("animals.html", 'w') as handle:
    handle.write(final_html)

