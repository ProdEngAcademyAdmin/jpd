import requests, json
from src.utils.configParser import ConfigParser
from cryptography.fernet import Fernet

class Auth:
    def __init__(self):
        self.token = None
        config = ConfigParser("config.yaml", "authentication").get_data()
        self.user = config['user']
        self.password = config['password']
        self.base_url = config['url']

    def get_cookies(self):
        url = f"https://{self.base_url}/ui/api/v1/ui/auth/login?_spring_security_remember_me=false"
        headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"97\", \" Not;A Brand\";v=\"99\"", "Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", "Sec-Ch-Ua-Platform": "\"macOS\"", "Origin": "https://blabla12.jfrog.io", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        json={"password": f"{self.password}", "type": "login", "user": f"{self.user}"}
        res = requests.post(url, headers=headers, json=json)
        return res.cookies["ACCESSTOKEN"], res.cookies["REFRESHTOKEN"]

    def get_token_for_service(self, service):
        ACCESSTOKEN, REFRESHTOKEN = self.get_cookies()
        url = f"https://{self.base_url}/ui/api/v1/access/token/scoped?expiry=0&services[]={service}&scope=applied-permissions%2Fadmin&username={self.user}"
        cookies = {"ACCESSTOKEN": f"{ACCESSTOKEN}", "REFRESHTOKEN": f"{REFRESHTOKEN}"}
        headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"97\", \" Not;A Brand\";v=\"99\"", "Accept": "application/json, text/plain, */*", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36", "Sec-Ch-Ua-Platform": "\"macOS\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
        res = requests.get(url, headers=headers, cookies=cookies).json()
        access_token = res['access_token']
        key = Fernet.generate_key()
        encryption_type = Fernet(key)
        token_encoded = bytes(access_token,'UTF-8')
        encrypted_token = encryption_type.encrypt(token_encoded)
        self.token = encrypted_token
        self.key = key
            
    def get_token(self,service):
        if self.token is None:
            self.get_token_for_service(service)
        encryption_type = Fernet(self.key)
        decrypted_token = encryption_type.decrypt(self.token)
        return decrypted_token.decode('utf-8')

# if __name__ == '__main__':
#     t = Auth().get_token(service='xray')
#     print(t)