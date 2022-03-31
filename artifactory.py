from configParser import ConfigParser
from RESTClient import RESTClient
import json

class Artifactory:

    def __init__(self):
        self.artifactory_data= ConfigParser(file_name='config.yaml',app='artifactory').get_data()


    def ping(self):
        """
        input: client

        :return: response from JPD, Get a simple status response about the state of Artifactory
                Returns 200 code with an 'OK' text if Artifactory is working properly, if not will return an HTTP error code with a reason.
        """
        api_path = "artifactory/api/system/ping"
        resp = RESTClient(api_path=api_path,http_method="GET").api_call()
        if resp.status_code <= 201:
            print("Ping Is OK")
        else:
            print("Ping is not good")



    def storage_info(self):
        """
        inputs: client

        :return: response from JPD , Returns storage summary information regarding binaries, file store and repositories.
        """
        api_path = "artifactory/api/storageinfo"
        resp = RESTClient(api_path=api_path,http_method="GET").api_call()
        print(resp.text)

    def create_repo(self):
        """
        :input: client and the data about the repos

        :return: Creates a new repository in Artifactory with the provided configuration.
         Supported by local, remote, virtual and federated repositories.
        """
        repositories_list = self.artifactory_data["new_repositories"]
        for repository_data_block in repositories_list:
            repo_data=(next(iter(repository_data_block.values())))
            key = repo_data["key"]
            api_path = f"artifactory/api/repositories/{key}"
            repo_json = json.dumps(repo_data).encode('utf-8')
            resp = RESTClient(api_path=api_path, http_method="PUT", data=repo_json).api_call()
            print(resp.text)

if __name__ == '__main__':
    arti = Artifactory().create_repo()


