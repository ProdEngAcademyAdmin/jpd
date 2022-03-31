import RESTclient
from configParser import ConfigParser
from RESTclient import RESTClient
from Auth import Auth

class artifactory:

    def __init__(self):

        self.artifactory_data= ConfigParser(file_name='config.yaml',app='artifactory').get_data()


    def ping(self):

        api_path ="artifactory/api/system/ping"
        resp = RESTClient(api_path=api_path,http_method="GET").api_call()
        if resp.status_code <= 201:
            print("Ping Is OK")
        else:
            print("Ping is not good")


    def storage_info(self):

        api_path ="artifactory/api/storageinfo"
        resp = RESTClient(api_path=api_path,http_method="GET").api_call().json()
        print(resp)

    def create_repo(self):

        data_dict=self.artifactory_data["new_repositories"]
        for repo in data_dict:
            resp = RESTclient.send_api_request("/api/repositories/"+"karam","PUT",repo)
            print(repo)
        if resp.data == b'OK':
            print(f"Response from  {(resp.data.decode('utf-8'))}")
        else:
            print(f"Error from server \n{(resp.data.decode('utf-8'))}")
if __name__ == '__main__':
    arti = artifactory().storage_info()

