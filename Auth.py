import requests, configparser, json
from configParser import ConfigParser

parser_yml = ConfigParser().get_data('Artifactory')
user = parser_yml['credentials']['user']
password = parser_yml['credentials']['password']
base_url = parser_yml['base_url']

# Create Token For JPD
def create_token(user,password,base_url):
    
    api_path = 'artifactory/api/security/token'
    url = base_url+api_path
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = f'username={user}&scope=member-of-groups:administrators'
    auth = (f'{user}',f'{password}')

    response = requests.post(url=url, headers=header, data=data, auth=auth).json()
    access_token = response['access_token']
    create_config(base_url, access_token)

# Create a config file
config = configparser.ConfigParser()
def create_config(user,base_url, access_token):
    
    config['jfrog'] = {
        'username': user,
        'url': base_url,
        'apikey': access_token
    }

    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    
    return True