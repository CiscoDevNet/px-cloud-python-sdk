from pprint import pprint
import openapi_client
import px_v1_python_sdk.api.partner_data_api as sdk

configuration = openapi_client.Configuration(
    # host = 'ENTER_HOST_HERE'
)
configuration.access_token = 'ENTER_ACCESS_TOKEN_HERE'
api_instance = sdk.PartnerDataApi(openapi_client.ApiClient(configuration))
response = api_instance.get_customers()
pprint(response)

