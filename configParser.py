import yaml
from os.path import expanduser


class ConfigParser:
    """Get specific config data for your application
       Create an instance, give 2 params - yaml_name & app name(file name)
       Put the YAML file inside 'jpd' folder in your home directory """

    def __init__(self, yaml_name, app):
        self.yaml_data = {}
        self.yaml_name = yaml_name
        self.app = app

    def read_file(self):
        file_path = expanduser(f"~/jpd/{self.yaml_name}")
        with open(file_path, 'r') as stream:
            try:
                self.yaml_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_data(self):
        self.read_file()
        try:
            return self.yaml_data[self.app]
        except BaseException as err:
            raise BaseException(f"Can't find application: {err} in the {self.yaml_name} file")


c1 = ConfigParser(yaml_name='Test.yml', app='xray')
print(c1.get_data())



