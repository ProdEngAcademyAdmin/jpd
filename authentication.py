import configparser
import urllib3
from urllib.parse import urlencode #For splitting a URL string into its components
import sys
import json
import jwt



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
HTTP = urllib3.PoolManager() #creating ConnectionPool instances for each host as needed.

auth_data=configparser.data("authentication")['authentication']

base_url=auth_data["baseUrl"]
user=auth_data["user"]
password=auth_data["password"]


def login(server,username,password,token_expiration_time=0):
    options = {'username': username, 'scope': 'member-of-groups:*', 'expires_in': token_expiration_time}
    encoded_options = urlencode(options)
    headers_dict = urllib3.make_headers(basic_auth=f"{username}:{password}")
    headers_dict['Content-Type'] = 'application/x-www-form-urlencoded'
    url = f"https://{server}/artifactory/api/security/token?{encoded_options}"
    resp = HTTP.request('POST', url , headers=headers_dict)
    if resp.status == 200:
        print("Success generating token")
        output = json.loads(resp.data.decode('utf-8'))
        return output["access_token"]
    else:
        sys.exit(f"ERROR retriving token from server\n{resp.data.decode('utf-8')}")


token=login(base_url,user,password)
#encoded = jwt.encode({"some": "payload"}, token, algorithm="RS256")
print(token)
