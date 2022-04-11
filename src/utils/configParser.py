import yaml
import os


class ConfigParser:
    """Get specific config data for your application
       Create an instance, give 2 params - file_name & app name(file name)
       Put the YAML file inside 'jpd' folder in your home directory """

    def __init__(self, file_name, app, file_path = None):
        self.yaml_data = {}
        self.file_name = file_name
        self.app = app
        self.file_path = file_path

    def read_file(self):
        if self.file_path is None:
            self.file_path = os.path.expanduser("~/jpd/")
        file = os.path.join(self.file_path,self.file_name)
        with open(file, 'r') as stream:
            try:
                self.yaml_data = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def get_data(self):
        self.read_file()
        try:
            data = self.yaml_data[self.app]
            return data
        except BaseException as err:
            raise BaseException(f"Can't find application: {err} in the {self.file_name} file")
        except KeyError:
            print(f"Are you sure {self.app} is the correct application? Not found in the config file")
            raise KeyError


if __name__ == "__main__":
    # c1 = ConfigParser(file_name='Test.yml', app='xray')
    # print(c1.get_data())
    pass



