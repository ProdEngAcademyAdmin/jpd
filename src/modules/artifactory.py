from src.utils.configParser import ConfigParser
from src.utils.RESTClient import RESTClient
import json
import click
import os


app_name = os.path.basename(__file__).split('.')[0].lower()
artifactory_data = ConfigParser(file_name='config.yaml', app=app_name).get_data()


class Artifactory:

    def __init__(self):
        pass
        # self.app_name = os.path.basename(__file__).split('.')[0].lower()
        # self.artifactory_data = ConfigParser(file_name='config.yaml', app=self.app_name).get_data()

    @staticmethod
    @click.command()
    def ping():
        """
        input: client

        :return: response from JPD, Get a simple status response about the state of Artifactory
                Returns 200 code with an 'OK' text if Artifactory is working properly, if not will return an HTTP error code with a reason.
        """
        api_path = "artifactory/api/system/ping"
        resp = RESTClient(api_path=api_path, http_method="GET").api_call()
        if resp.status_code <= 201:
            click.echo("Ping Is OK")
        else:
            click.echo("Ping is not good")

    @staticmethod
    @click.command()
    def storage_info():
        """
        inputs: client

        :return: response from JPD , Returns storage summary information regarding binaries, file store and repositories.
        """
        api_path = "artifactory/api/storageinfo"
        resp = RESTClient(api_path=api_path, http_method="GET").api_call()
        click.echo(resp.text)

    @staticmethod
    @click.command()
    def create_repo():
        """
        :input: client and the data about the repos

        :return: Creates a new repository in Artifactory with the provided configuration.
         Supported by local, remote, virtual and federated repositories.
        """
        repositories_list = artifactory_data["new_repositories"]
        for repository_data_block in repositories_list:
            repo_data = (next(iter(repository_data_block.values())))
            key = repo_data["key"]
            api_path = f"artifactory/api/repositories/{key}"
            repo_json = json.dumps(repo_data).encode('utf-8')
            resp = RESTClient(api_path=api_path, http_method="PUT", data=repo_json).api_call()
            click.echo(resp.text)


