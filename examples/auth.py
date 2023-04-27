import json
import urllib3

class Env:
    def __init__(self, env:str = 'SANDBOX', client_id:str = '', client_secret:str = '') -> None:
        '''
            Configures the environment and generates authorization tokens to use the PXCloud API

            :param env: Envirnment for the Authorization token to be generated either "SANDBOX" or "PROD"
            :param client_id: Client ID for generating the Authorization token
            :param client_secret: Client Secret for generating the Authorization token
        '''
        _envs = {'SANDBOX':{'key': 'SANDBOX',
                    'clientId': '',
                    'clientSecret': '',
                    'host': 'https://api-cx.cisco.com/sandbox/px',
                    'reqURL': 'https://api-cx.cisco.com/sandbox/px/v1',
                    'authURL': 'https://id.cisco.com/oauth2/aus1o4emxorc3wkEe5d7/v1/token',
                    'authPARAMS': 'grant_type=client_credentials&cache-control=no-cache&scope=api.customer.assets.manage'},

                'PROD':{'key': 'PROD',
                    'clientId': '',
                    'clientSecret': '',
                    'host': 'https://api-cx.cisco.com/px',
                    'reqURL': 'https://api-cx.cisco.com/px/v1',
                    'authURL': 'https://id.cisco.com/oauth2/aus1o4emxorc3wkEe5d7/v1/token',
                    'authPARAMS': 'grant_type=client_credentials&cache-control=no-cache&scope=api.authz.iam.manage'}
            }
        assert env.upper() in ['SANDBOX', 'PROD']

        self.env_info = _envs[env.upper()]  
        self.env_info['clientId'] = client_id    
        self.env_info['clientSecret'] = client_secret
        self.host = self.env_info['host']

    def get_token(self):
        '''
            Returns a Authorization token or raise an Error with the environment info
        '''
        http = urllib3.PoolManager()
        req_url = "{}?{}&client_id={}&client_secret={}".format(self.env_info['authURL'], self.env_info['authPARAMS'], self.env_info['clientId'], self.env_info['clientSecret'])
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = http.request("POST", req_url, headers=headers)
        if (response.status == 200):
            print('new token generated for: {} environment'.format(self.env_info['key']))
            return json.loads(response.data.decode('utf-8'))['access_token']
        raise RuntimeError("Invalid client_id or client_secret")