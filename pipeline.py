#from RESTClinet import RestClient
import requests, json
from configParser import ConfigParser
from Auth import Auth
from RESTClient import RESTClient

class Pipeline:

    def __init__(self):
        self.data = ConfigParser('config.yaml','pipeline').get_data()
        # self.integrations = data['integrations']
        # self.integrations = data['integrations']

    def create_inegrations(self):     
        http_method = 'POST'
        api_path = 'pipeline/api/v1/projectIntegrations'
        self.integrations = self.data['integrations']
        for integration in self.integrations:
            payload = json.load(integration['masterIntegrationName']) 
            response = RESTClient().api_call(http_method, api_path, payload)

    def create_pipeline_source(self):
        http_method = 'POST' 
        api_path = 'pipeline/api/v1/pipelinesources'
        self.source = self.data['source']
        for integration in self.integrations:
            payload = json.load(integration['masterIntegrationName']) 
            response = RESTClient().api_call(http_method, api_path, payload)

    def trigger_pipeline():
        pass
        
    def report_status():
        pass
