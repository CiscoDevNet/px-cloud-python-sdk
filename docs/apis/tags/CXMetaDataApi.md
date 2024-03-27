<a id="__pageTop"></a>
# pxcloud_api_client.apis.tags.cx_meta_data_api.CXMetaDataApi

All URIs are relative to *https://api-cx.cisco.com/sandbox/px*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_success_tracks**](#get_success_tracks) | **get** /v1/successTracks | List success tracks

# **get_success_tracks**
<a id="get_success_tracks"></a>
> SuccessTracksResponse get_success_tracks()

List success tracks

### Example

* OAuth Authentication (oAuth2):
```python
import pxcloud_api_client
from pxcloud_api_client.apis.tags import cx_meta_data_api
from pxcloud_api_client.pxcloud_api_client.error_response import ErrorResponse
from pxcloud_api_client.pxcloud_api_client.success_tracks_response import SuccessTracksResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-cx.cisco.com/sandbox/px
# See configuration.py for a list of all supported configuration parameters.
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = pxcloud_api_client.Configuration(
    host = "https://api-cx.cisco.com/sandbox/px",
    access_token = 'YOUR_ACCESS_TOKEN'
)
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_success_tracks.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_success_tracks.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_success_tracks.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_success_tracks.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_success_tracks.ApiResponseFor404) | Not found
500 | [ApiResponseFor500](#get_success_tracks.ApiResponseFor500) | Internal server error
503 | [ApiResponseFor503](#get_success_tracks.ApiResponseFor503) | Service Unavailable
504 | [ApiResponseFor504](#get_success_tracks.ApiResponseFor504) | Gateway timeout

#### get_success_tracks.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SuccessTracksResponse**](../../models/SuccessTracksResponse.md) |  | 


#### get_success_tracks.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_success_tracks.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_success_tracks.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_success_tracks.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_success_tracks.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_success_tracks.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


#### get_success_tracks.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 


### Authorization

[oAuth2](../../../README.md#oAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

