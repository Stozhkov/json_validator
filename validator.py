import os
import json
from configparser import ConfigParser
from json_loader import JsonLoader


current_dir = os.path.dirname(os.path.realpath(__file__))

try:
    config = ConfigParser()
    config.read(current_dir + '/' + 'config.cfg')
    path_to_json_folder = current_dir + '/' + config.get('directories', 'json_folder')
    path_to_schema_folder = current_dir + '/' + config.get('directories', 'schema_folder')
except Exception as e:
    print('Some problem with config file')
    print(e)

for f in os.listdir(path_to_json_folder):
    print('\n Starting check file "' + f + '"')
    jl = JsonLoader(path_to_json_folder + '/' + f)
    jl.load()

    if not jl.check_json():
        continue

    schema_name = jl.get_schema_name()

    if schema_name:
        schema_file = path_to_schema_folder + '/' + schema_name + '.schema'
        try:
            with open(schema_file, 'r') as fp:
                schema = json.load(fp)
        except IOError:
            print('Can not find schema "' + schema_name + '".')
        else:
            jl.validate_json(schema)
