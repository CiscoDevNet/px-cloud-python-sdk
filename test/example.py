import pxcloud_api_client
from pprint import pprint
from pxcloud_api_client.api import compliance_api
from pxcloud_api_client.model.asset_violations_response import AssetViolationsResponse
from pxcloud_api_client.model.assets_violations_response import AssetsViolationsResponse
from pxcloud_api_client.model.assets_with_violations_response import AssetsWithViolationsResponse
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.opt_in_response import OptInResponse
from pxcloud_api_client.model.policy_rule_details import PolicyRuleDetails
from pxcloud_api_client.model.suggestions_response import SuggestionsResponse
from pxcloud_api_client.model.violation_summary_response import ViolationSummaryResponse
from auth import Env

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
envInfo = Env().envInfo

configuration = pxcloud_api_client.Configuration(
    host = envInfo['host']
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = envInfo['host']
)
configuration.access_token = envInfo['accessToken']


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
        pprint(api_response["items"][-1]["violation_age"])
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling ComplianceApi->asset_violations: %s\n" % e)