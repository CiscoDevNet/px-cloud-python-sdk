CX Partner Portal APIs for the Partners

For more information, please visit [https://cisco.com](https://cisco.com)

## Requirements

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/CiscoDevNet/px-cloud-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/CiscoDevNet/px-cloud-python-sdk.git`)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import openapi_client
from pprint import pprint
from px_v1_python_sdk.api import contracts_data_api
from px_v1_python_sdk.model.contracts_error_response import ContractsErrorResponse
from px_v1_python_sdk.model.data_pagination_response import DataPaginationResponse

# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Configure OAuth2 access token for authorization: oAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contracts_data_api.ContractsDataApi(api_client)

    # Set parameters for response
    success_track_id = 1 # int | successTrackId
    puid = 1 # int | puid
    customer_id = "customerId_example" # str | customerId (optional)
    gu_name = "guName_example" # str | guName (optional)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)

    try:
        # Get the list of contracts summary
        api_response = api_instance.fetch_contracts_summary_using_get(success_track_id, puid, customer_id=customer_id, gu_name=gu_name, limit=limit, offset=offset)
        pprint(api_response)
        
    except openapi_client.ApiException as e:
        print("Exception when calling ContractsDataApi->fetch_contracts_summary_using_get: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.pxcloud-stg.cisco.com/torii*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContractsDataApi* | [**fetch_contracts_summary_using_get**](docs/px_v1_python_sdk/ContractsDataApi.md#fetch_contracts_summary_using_get) | **GET** /v2/contracts | Get the list of contracts summary
*CustomerDataApi* | [**fetch_contracts_details_using_get**](docs/px_v1_python_sdk/CustomerDataApi.md#fetch_contracts_details_using_get) | **GET** /v1/contract/details | Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
*CustomerDataApi* | [**get_customer_report**](docs/px_v1_python_sdk/CustomerDataApi.md#get_customer_report) | **GET** /v1/customers/{customerId}/reports/{reportId} | Get the report
*CustomerDataApi* | [**get_customers_life_cycle**](docs/px_v1_python_sdk/CustomerDataApi.md#get_customers_life_cycle) | **GET** /v1/customers/{customerId}/lifecycle | Get customer lifecycle
*CustomerDataApi* | [**request_customer_report**](docs/px_v1_python_sdk/CustomerDataApi.md#request_customer_report) | **POST** /v1/customers/{customerId}/reports | Request customer data reports as bulk files
*PartnerDataApi* | [**get_contracts**](docs/px_v1_python_sdk/PartnerDataApi.md#get_contracts) | **GET** /v1/contracts | List of contracts
*PartnerDataApi* | [**get_customers**](docs/px_v1_python_sdk/PartnerDataApi.md#get_customers) | **GET** /v1/customers | List of customers
*PartnerDataApi* | [**get_success_tracks**](docs/px_v1_python_sdk/PartnerDataApi.md#get_success_tracks) | **GET** /v1/successTracks | Success Tracks
*PartnerOffersDataApi* | [**get_partner_offers**](docs/px_v1_python_sdk/PartnerOffersDataApi.md#get_partner_offers) | **GET** /v1/partnerOffers | Get Partner Offers
*PartnerOffersSessionsDataApi* | [**get_partner_offers_sessions**](docs/px_v1_python_sdk/PartnerOffersSessionsDataApi.md#get_partner_offers_sessions) | **GET** /v1/partnerOffersSessions | Get Info about Partner Offers Sessions


## Documentation For Models

 - [AccSessionAttendees](docs/px_v1_python_sdk/AccSessionAttendees.md)
 - [AssetError](docs/px_v1_python_sdk/AssetError.md)
 - [AssetSession](docs/px_v1_python_sdk/AssetSession.md)
 - [ContractInfo](docs/px_v1_python_sdk/ContractInfo.md)
 - [ContractResponse](docs/px_v1_python_sdk/ContractResponse.md)
 - [ContractsErrorResponse](docs/px_v1_python_sdk/ContractsErrorResponse.md)
 - [Customer](docs/px_v1_python_sdk/Customer.md)
 - [CustomerInfo](docs/px_v1_python_sdk/CustomerInfo.md)
 - [CustomerResponse](docs/px_v1_python_sdk/CustomerResponse.md)
 - [DataPaginationResponse](docs/px_v1_python_sdk/DataPaginationResponse.md)
 - [ErrorResponse](docs/px_v1_python_sdk/ErrorResponse.md)
 - [Pagination](docs/px_v1_python_sdk/Pagination.md)
 - [PartnerAsset](docs/px_v1_python_sdk/PartnerAsset.md)
 - [PartnerAssetResponse](docs/px_v1_python_sdkPartnerAssetResponse.md)
 - [PartnerOffer](docs/px_v1_python_sdkPartnerOffer.md)
 - [PartnerOfferAttendee](docs/px_v1_python_sdkPartnerOfferAttendee.md)
 - [PartnerOfferSession](docs/px_v1_python_sdkPartnerOfferSession.md)
 - [PartnerOfferWithSessions](docs/px_v1_python_sdkPartnerOfferWithSessions.md)
 - [PartnerOffersInfo](docs/px_v1_python_sdkPartnerOffersInfo.md)
 - [RacetrackBuid](docs/px_v1_python_sdkRacetrackBuid.md)
 - [RacetrackBuidPitstop](docs/px_v1_python_sdkRacetrackBuidPitstop.md)
 - [RacetrackBuidPitstopAction](docs/px_v1_python_sdkRacetrackBuidPitstopAction.md)
 - [RacetrackBuidSolution](docs/px_v1_python_sdkRacetrackBuidSolution.md)
 - [RacetrackTooltip](docs/px_v1_python_sdkRacetrackTooltip.md)
 - [RacetrackUsecase](docs/px_v1_python_sdkRacetrackUsecase.md)
 - [Reason](docs/px_v1_python_sdkReason.md)
 - [Report](docs/px_v1_python_sdkReport.md)
 - [ReportStatus](docs/px_v1_python_sdkReportStatus.md)
 - [SolutionMapping](docs/px_v1_python_sdkSolutionMapping.md)
 - [SuccessTrackChecklistMapping](docs/px_v1_python_sdkSuccessTrackChecklistMapping.md)
 - [SuccessTrackMapping](docs/px_v1_python_sdk/SuccessTrackMapping.md)


## Documentation For Authorization


## oAuth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author

developer-support-pxcloud@cisco.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in openapi_client.apis and openapi_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from openapi_client.api.default_api import DefaultApi`
- `from openapi_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import openapi_client
from openapi_client.apis import *
from openapi_client.models import *
```

