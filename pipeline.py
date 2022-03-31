#from RESTClinet import RestClient
import requests, json
from configParser import ConfigParser
from Auth import Auth

class Pipeline:

    def __init__(self):
        self.data = ConfigParser('config.yaml','pipeline').get_data()
        # self.integrations = data['integrations']
        # self.integrations = data['integrations']

    def create_inegrations(self):     
        method = 'POST'
        api_path = 'api/v1/projectIntegrations'
        self.integrations = self.data['integrations']
        for integration in self.integrations:
            payload = json.load(integration['masterIntegrationName']) 

            #     print(integration['formJSONValues'])
            # elif integration['masterIntegrationName'] == 'github':
            #     pass


    def create_pipeline_source(self):
        method = 'post' 
        api_path = 'api/v1/pipelinesources'
        payload = {}

    def trigger_pipeline():
        pass
        
    def report_status():
        pass
