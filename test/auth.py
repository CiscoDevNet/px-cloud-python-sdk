import json
import urllib3
#### TAKES AN ENV_DICT AND RETURNS TOKEN FOR IT
def getToken(envInfo: dict):
    http = urllib3.PoolManager()
    req_url = "{}?{}&client_id={}&client_secret={}".format(
        envInfo['authURL'], envInfo['authPARAMS'], envInfo['clientId'], envInfo['clientSecret'])
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = http.request("POST", req_url, headers=headers)
    print('new token generated for: {} environment'.format(
        envInfo['key']))
    return json.loads(response.data.decode('utf-8'))['access_token']

class Env:
    def __init__(self) -> None:
        self.envInfo = {
            'key': 'SANDBOX',
            'clientId': '576b46e1-6c84-42b5-9f93-b69c7eecf05c',
            'clientSecret': 'H4cBqxqZu6VLzvp8sIc6G8z-xuuS7dCMDPIfrKE-',
            'host': 'https://api-cx.cisco.com/sandbox/px',
            'reqURL': 'https://api-cx.cisco.com/sandbox/px/v1',
            'authURL': 'https://id.cisco.com/oauth2/aus1o4emxorc3wkEe5d7/v1/token',
            'authPARAMS': 'grant_type=client_credentials&cache-control=no-cache&scope=api.customer.assets.manage',
            'accessToken': 'NOT-GENERATED'
            }       
        self.envInfo['accessToken'] = getToken(self.envInfo) 