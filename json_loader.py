import json
from jsonschema import Draft7Validator


class JsonLoader:
    def __init__(self, path_to_json_file):
        self.path_to_json_file = path_to_json_file
        self.data = None

    def load(self):
        with open(self.path_to_json_file, 'r') as fp:
            self.data = json.load(fp)

    def get_schema_name(self):
        try:
            schema_name = self.data['event']
        except:
            schema_name = False

        return schema_name

    def check_json(self):
        if type(self.data) is dict and self.data != {}:
            return True
        else:
            print('Wrong file.')

    def validate_json(self, schema):
        v = Draft7Validator(schema)

        errors = sorted(v.iter_errors(self.data), key=lambda e: e.path)

        for error in errors:
            print(error.message)
        if errors is None:
            print('No errors')


