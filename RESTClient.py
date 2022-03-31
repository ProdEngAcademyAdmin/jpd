import requests
from configParser import ConfigParser
from Auth import Auth


class RESTClient:

    def __init__(self, api_path, http_method, data={}, config_path=None):
        if config_path is None:
            config_path = "config.yaml"
        try:
            fetched_url = ConfigParser(file_name=config_path, app="authentication").get_data()['url']
        except BaseException as err:
            raise err
        self.base_url = fetched_url
        self.token = Auth().get_token()
        self.api_path = api_path
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': f"Bearer {self.token}"}
        self.data = data
        self.http_method = http_method

    def api_call(self):
        response = requests.request(method=self.http_method,
                                    url=f"https://{self.base_url}/{self.api_path}",
                                    headers=self.headers,
                                    data=self.data)
        print(f"https://{self.base_url}/{self.api_path}")
        return response


if __name__ == '__main__':
    print(RESTClient(api_path="artifactory/api/system/ping", http_method="GET").api_call())



