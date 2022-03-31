import requests, json
from configParser import ConfigParser
from cryptography.fernet import Fernet

class Auth:
    def __init__(self):
        self.token = None
        config = ConfigParser("config.yaml","authentication").get_data()
        self.user = config['user']
        self.password = config['password']
        self.base_url = config['url']

    # Create Token For JPD
    def create_token(self):
        api_path = 'artifactory/api/security/token'
        url = f"https://{self.base_url}/{api_path}"
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = f"username={self.user}&scope=member-of-groups:administrators&expires_in=3600"
        auth = f"{self.user}",f"{self.password}"
        response = requests.post(url=url, headers=header, data=data, auth=auth).json()
        access_token = response['access_token']

        key = Fernet.generate_key()
        encryption_type = Fernet(key)
        token_encoded = bytes(access_token,'UTF-8')
        encrypted_token = encryption_type.encrypt(token_encoded)
        self.token = encrypted_token
        self.key = key
    
    def get_token(self):
        if self.token is None:
            self.create_token()
        encryption_type = Fernet(self.key)
        decrypted_token = encryption_type.decrypt(self.token)
        return decrypted_token.decode('utf-8')

if __name__ == '__main__':
    t = Auth().get_token()
    print(t)