from pprint import pprint
from px_v1_python_sdk import (
    ApiClient, Configuration, PartnerDataApi, model_to_dict
)

configuration = Configuration(
    # host = 'ENTER_HOST_HERE'
)
configuration.access_token = 'ENTER_ACCESS_TOKEN_HERE'
api_instance = PartnerDataApi(ApiClient(configuration))
response = api_instance.get_customers()
responseDict = model_to_dict(response)
pprint(response)
