import yaml


class Parser:

    def __init__(self, my_input='configs.yml'):
        self.input_file = my_input
        self.configs_dict = self.parse

    @property
    def parse(self):
        with open(self.input_file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    def get_key(self, key):
        if key in self.configs_dict:
            return self.configs_dict[key]
        else:
            return None

