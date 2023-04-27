import pxcloud_api_client
from pprint import pprint
from pxcloud_api_client.api import compliance_api
from auth import Env

# Configuring the environment to either prod or sandbox along with the appropriate Client ID and client Secret
env_info = Env('sandbox', 'YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET')


configuration = pxcloud_api_client.Configuration(
    host = env_info.host
)
configuration.access_token = env_info.get_token()


# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compliance_api.ComplianceApi(api_client)
    success_track_id = "successTrackId_example" # str | 
    source_system_id = "sourceSystemId_example" # str | 
    customer_id = "customerId_example" # str | 
    asset_id = "assetId_example" # str | 
    offset = 1 # int |  (optional) (default to 1)
    max = 10 # int |  (optional) (default to 10)

    try:
        # Get the violations of the asset
        api_response = api_instance.asset_violations(success_track_id, source_system_id, customer_id, asset_id, offset=offset, max=max)
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->asset_violations: %s\n" % e)