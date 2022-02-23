import json
from pprint import pprint

filename = 'population_data.json'
with open(filename) as f:
    data = json.load(f)
    pprint(data)


