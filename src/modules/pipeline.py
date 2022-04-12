import json, click
from src.utils.configParser import ConfigParser
from src.utils.RESTClient import RESTClient

# Get data about pipeline from config YAML
data = ConfigParser('config.yaml', 'pipeline').get_data()
integrations = data['integrations']
source = data['source']


def get_rt_apikey():
    http_method = 'GET'
    api_path = 'artifactory/api/security/apiKey'
    response = RESTClient(api_path, http_method).api_call().json()
    return response


def create_rt_apikey():
    http_method = 'POST'
    api_path = 'artifactory/api/security/apiKey'
    response = RESTClient(api_path, http_method).api_call().json()
    return response


def regenerate_rt_apikey():
    http_method = 'PUT'
    api_path = 'artifactory/api/security/apiKey'
    response = RESTClient(api_path, http_method).api_call().json()
    return response


def get_integration_id(integration_name = None):
    http_method = 'GET'
    api_path = 'pipelines/api/v1/projectIntegrations'
    response = RESTClient(api_path, http_method).api_call().json()
    response = json.dumps(response)
    response = json.loads(response)
    for integration in response:
        if integration['masterIntegrationName'] == integration_name:
            integration_id = integration["id"]
    return integration_id


class Pipeline:

    def __init__(self):
        pass

    @staticmethod
    @click.command()
    def create_integrations():
        http_method = 'POST'
        api_path = 'pipelines/api/v1/projectIntegrations'
        try:
            for integration in integrations:
                payload = json.dumps(integration)
                if integration['masterIntegrationName'] == 'artifactory':
                    api_key = get_rt_apikey()
                    api_key = json.dumps(api_key)
                    if api_key[0] == 'error' or api_key[0] == 'apiKey':
                        api_key = regenerate_rt_apikey()
                    else:
                        api_key = create_rt_apikey()
                        api_key = api_key['apiKey']
                    json_dict = json.loads(payload)
                    json_dict['formJSONValues'][0]['value'] = api_key
                    payload = json.dumps(json_dict)
                response = RESTClient(api_path, http_method, payload).api_call()
                if response.status_code == 200:
                    print(f"New integrations have been created - {integration['masterIntegrationName']}")
        except BaseException as err:
            raise err

    @staticmethod
    @click.command()
    def create_pipeline_source():
        http_method = 'POST' 
        api_path = 'pipelines/api/v1/pipelinesources'
        source['projectIntegrationId'] = get_integration_id(integration_name='github')
        try:
            payload = json.dumps(source)
            response = RESTClient(api_path, http_method, payload).api_call()
            if response.status_code == 200:
                return 'New integrations have been created'
        except BaseException as err:
            raise err

    @staticmethod
    @click.command()
    def trigger_pipeline():
        http_method = 'POST'
        api_path = 'pipelines/api/v1/pipelineSteps/4/trigger'
        try:
            response = RESTClient(api_path, http_method).api_call().json()
            print('Trigger Pipeline Start')
            return response
        except BaseException as err:
            raise err
