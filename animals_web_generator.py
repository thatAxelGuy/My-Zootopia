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
output: str = ""
for animal in animals_data:
    name = animal.get('name')
    characteristics = animal['characteristics']
    locations = animal['locations']

    if name:
        output += f"Name:  {name}\n"

    if characteristics.get('diet') is not None:
        output += f"Diet:  {characteristics['diet']}\n"

    if locations:
        output += f"Location:  {locations[0]}\n"

    if characteristics.get('type') is not None:
        output += f"Type:  {characteristics['type']}\n"
    output += "\n"

# replace string in template with output and store in final_html
final_html = template.replace(
    "__REPLACE_ANIMALS_INFO__",
    output
)

# write final_html to animals.html
with open("animals.html", 'w') as handle:
    handle.write(final_html)

