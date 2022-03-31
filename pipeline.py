#from RESTClinet import RestClient
import requests
from configParser import ConfigParser
from Auth import Auth

class Pipeline:
    def __init__(self):
        data = ConfigParser('config.yaml','pipeline').get_data()
        self.integrations = data['integrations']

    def create_inegrations(self):     
        method = 'post'
        api_path = ''

        for inter in self.integrations:
            if inter['masterIntegrationName'] == 'artifactory':
                pass

    def create_pipeline_source(self):
        method = 'post' 
        api_path = 'api/v1/pipelinesources'
        payload = {}

    def trigger_pipeline():
        pass
        
    def report_status():
        pass
