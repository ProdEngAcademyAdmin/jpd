#from RESTClinet import RestClient
import json
from venv import create
from configParser import ConfigParser
from RESTClient import RESTClient

class Pipeline:

    def __init__(self):
        self.data = ConfigParser('config.yaml','pipeline').get_data() #Get data about pipeline from config YAML 
        self.integrations = self.data['integrations']
        self.source = self.data['source']

    def create_inegrations(self):     
        http_method = 'POST'
        api_path = 'pipelines/api/v1/projectIntegrations'
        try:
            for integration in self.integrations:
                payload = json.dumps(integration)

                if integration['masterIntegrationName'] == 'artifactory':
                    api_key = self.create_rt_apikey()
                    base_url = RESTClient(api_path, http_method).base_url
                    JsonD = json.loads(payload)
                    JsonD['formJSONValues'][0]['value'] = api_key
                    JsonD['formJSONValues'][1]['value'] = base_url
                    payload = json.dumps(JsonD)
  
                response = RESTClient(api_path, http_method, payload).api_call()

        except BaseException as err:
            raise err

    def create_rt_apikey(self):
        http_method = 'POST'
        api_path = 'artifactory/api/security/apiKey'
        response = RESTClient(api_path, http_method).api_call()
        return response

    def create_pipeline_source(self):
        http_method = 'POST' 
        api_path = 'pipelines/api/v1/pipelinesources'
        try:
            payload = json.dumps(self.source)
            response = RESTClient(api_path, http_method, payload).api_call()
            print(response.text)
        except BaseException as err:
            raise err

    def get_first_pipeline_steps(self):
        http_method = 'GET'
        api_path = 'api/v1/steps?limit=1'
        try:
            step_ip = RESTClient(api_path, http_method).api_call()
            return step_ip["id"]
        except BaseException as err:
            raise err 
    
    def trigger_pipeline(self):
        http_method = 'POST'
        api_path = 'api/v1/pipelineSteps/:pipelineStepId/trigger'
        step_ip = self.get_first_pipeline_steps()
        payload = {"piplimneStepId": step_ip, "reset": 'true'}
        try:
            response = RESTClient(api_path, http_method, payload).api_call()
            return response
        except BaseException as err:
            raise err

    def report_status():
        pass

    
if __name__ == "__main__":
    c1 = Pipeline().create_inegrations()
    print(c1)
    
