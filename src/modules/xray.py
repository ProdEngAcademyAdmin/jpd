from src.utils.configParser import ConfigParser
from src.utils.RESTClient import RESTClient
import json
import click
import os


class Xray:

    def __init__(self):
        self.app_name = os.path.basename(__file__).split('.')[0].lower()
        self.xray_data = ConfigParser(file_name='config.yaml', app=self.app_name).get_data()

    @click.command()
    def create_policy(self):
        """
        :input: client and the data about the policies

        :return: Creates a new policy , with the data that the user had submitted in the file
        """
        polices_list = self.xray_data["policies"]
        api_path = "xray/api/v2/policies"
        for policy_data_block in polices_list:
            policy_data = (next(iter(policy_data_block.values())))
            repo_json = json.dumps(policy_data)
            resp = RESTClient(api_path=api_path, http_method="POST", data=repo_json).api_call()
            click.echo(resp.text)

    @click.command()
    def create_watch(self):
        """
        :input: client and the data about the watches

        :return: Creates a new watch , with the data that the user had submitted in the file
        """
        watches_list = self.xray_data["watches"]
        api_path = "xray/api/v2/watches"
        for watch_data_block in watches_list:
            watch_data = (next(iter(watch_data_block.values())))
            repo_json = json.dumps(watch_data)
            resp = RESTClient(api_path=api_path, http_method="POST", data=repo_json).api_call()
            click.echo(resp.text)


