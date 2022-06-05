from src.utils.configParser import ConfigParser
from src.utils.RESTClient import RESTClient
import json
import click
import os


app_name = os.path.basename(__file__).split('.')[0].lower()
security_data = ConfigParser(file_name='config.yaml', app=app_name).get_data()


class Security:

    def __init__(self):
        pass
        # self.app_name = os.path.basename(__file__).split('.')[0].lower()
        # self.artifactory_data = ConfigParser(file_name='config.yaml', app=self.app_name).get_data()


    @staticmethod
    @click.command()
    def get_users():
        """
        inputs: client

        :return: response from JPD , Get the users list.
        """
        api_path = "artifactory/api/security/users"
        resp = RESTClient(api_path=api_path, http_method="GET").api_call()
        if resp.status_code <= 201:
            click.echo("Retrieves the users list:")
            click.echo(resp.text)
        else:
            click.echo(resp.text)

    @staticmethod
    @click.command()
    def get_user_lock_policy():
        """
        inputs: client

        :return: response from JPD , Retrieves the currently configured user lock policy.
        """
        api_path = "artifactory/api/security/userLockPolicy"
        resp = RESTClient(api_path=api_path, http_method="GET").api_call()
        if resp.status_code <= 201:
            click.echo("Retrieves the currently configured user lock policy:")
            click.echo(resp.text)
        else:
            click.echo(resp.text)

    @staticmethod
    @click.command()
    def set_user_lock_policy():
        """
        inputs: client and the data about the repos

        :return: Configures the user lock policy that locks users out of their account 
         if the number of repeated incorrect login attempts exceeds the configured maximum allowed.
        """

        data = """
        {
         "enabled" : true,
         "loginAttempts" : 5
        }
        """
        api_path = "artifactory/api/security/userLockPolicy"
        resp = RESTClient(api_path=api_path, http_method="PUT", data=data).api_call()
        if resp.status_code <= 201:
            click.echo(resp.text)
            click.echo("Set the user lock policy that locks users out of their account after 5 repeated incorrect login attempts.")
        else:
            click.echo(resp.text)

    @staticmethod
    @click.command()
    def get_password_expiration_policy():
        """
        inputs: client

        :return: response from JPD , Retrieves the password expiration policy
        """
        api_path = "artifactory/api/security/configuration/passwordExpirationPolicy"
        resp = RESTClient(api_path=api_path, http_method="GET").api_call()
        if resp.status_code <= 201:
            click.echo("Retrieves the password expiration policy:")
            click.echo(resp.text)
        else:
            click.echo(resp.text)

    @staticmethod
    @click.command()
    def set_password_expiration_policy():
        """
        inputs: client and the data about the repos

        :return: Sets the password expiration policy
        """

        data = """
        { "enabled" : "true",
          "passwordMaxAge" : "60",
          "notifyByEmail": "true" }
        """
        api_path = "artifactory/api/security/configuration/passwordExpirationPolicy"
        resp = RESTClient(api_path=api_path, http_method="PUT", data=data).api_call()
        if resp.status_code <= 201:
            click.echo(resp.text)
            click.echo("Set a policy of password expiration every 60 Days, this is the frequently all users must change their password. and mail notification.")
        else:
            click.echo(resp.text)