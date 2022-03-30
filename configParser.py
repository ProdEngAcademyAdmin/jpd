import yaml 

class ConfigParser():
    
    def __init__(self):
        pass

    with open ("data.yaml", 'r') as file:
        try:
            parsed_yaml=yaml.safe_load(file)
        except yaml.YAMLError as exc:
            print(exc) #raise

    #@property
    def get_data(self, key):
        
        return self.parsed_yaml[key]



