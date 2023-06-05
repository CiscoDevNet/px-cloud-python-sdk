# pxcloud_api_client.CXMetaDataApi

All URIs are relative to *https://api-cx.cisco.com/px/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_success_tracks**](CXMetaDataApi.md#get_success_tracks) | **GET** /v1/successTracks | List success tracks


# **get_success_tracks**
> SuccessTracksResponse get_success_tracks()

List success tracks

### Example

* OAuth Authentication (oAuth2):

```python
import time
import pxcloud_api_client
from pxcloud_api_client.api import cx_meta_data_api
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.success_tracks_response import SuccessTracksResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/px/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/px/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pxcloud_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cx_meta_data_api.CXMetaDataApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List success tracks
        api_response = api_instance.get_success_tracks()
        pprint(api_response)
    except pxcloud_api_client.ApiException as e:
        print("Exception when calling CXMetaDataApi->get_success_tracks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SuccessTracksResponse**](SuccessTracksResponse.md)

### Authorization

[oAuth2](../README.md#oAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |
**503** | Service Unavailable |  -  |
**504** | Gateway timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

