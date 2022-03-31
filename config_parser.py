import yaml
from yaml.loader import SafeLoader


def data(application):
    with open('userdetails.yaml') as datafile:
        data_dict=yaml.safe_load(datafile)
        new_data={key: data_dict[key] for key in [application]}
    return new_data

if __name__ == "__main__":
    data("authentication")
