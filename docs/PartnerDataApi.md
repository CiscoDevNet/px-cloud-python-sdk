# pxcloud_api_client.PartnerDataApi

All URIs are relative to *https://api.pxcloud.cisco.com/sandbox*

Method | HTTP request | Description
------------- | ------------- | -------------
[**success_tracks**](PartnerDataApi.md#success_tracks) | **GET** /v1/successTracks | Success Tracks


# **success_tracks**
> success_tracks()

Success Tracks

Partner Success Tracks

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import partner_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.pxcloud.cisco.com/sandbox
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/sandbox"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api.pxcloud.cisco.com/sandbox"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = partner_data_api.PartnerDataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Success Tracks
        api_instance.success_tracks()
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling PartnerDataApi->success_tracks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response |  * Date -  <br>  |
**400** | Bad Request |  * Date -  <br>  |
**403** | Forbidden |  * Date -  <br>  |
**500** | Internal server error |  * Date -  <br>  |
**503** | Service Unavailable |  * Date -  <br>  |
**504** | Gateway timeout |  * Date -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

