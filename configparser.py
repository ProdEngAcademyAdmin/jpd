import yaml
from yaml.loader import SafeLoader


def data(platform):
    with open('userdetails.yaml') as datafile:
        data_dict=yaml.safe_load(datafile)
        key_to_extract=[platform]
        new_data={key: data_dict[key] for key in key_to_extract}
    print(type(new_data))
    return new_data

if __name__ == "__main__":
    data("authentication")
