from __future__ import print_function
import time
from pprint import pprint
import os

import openapi_client
import px_v1_python_sdk.api.partner_data_api as sdk

configuration = openapi_client.Configuration()

api_instance = sdk.PartnerDataApi(openapi_client.ApiClient(configuration))
response = api_instance.get_customers()   #api_instance.get_contracts()
pprint(response)



