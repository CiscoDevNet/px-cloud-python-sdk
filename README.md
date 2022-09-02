# openapi-client
CX Partner Portal APIs for the Partners - LA Release

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.9.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://cisco.com](https://cisco.com)

## Requirements.

Python >=3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from pprint import pprint
from openapi_client.api import contracts_data_api
from openapi_client.model.contracts_error_response import ContractsErrorResponse
from openapi_client.model.data_pagination_response import DataPaginationResponse
# Defining the host is optional and defaults to https://api.pxcloud-stg.cisco.com/torii
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth2
configuration = openapi_client.Configuration(
    host = "https://api.pxcloud-stg.cisco.com/torii"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = contracts_data_api.ContractsDataApi(api_client)
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
*ContractsDataApi* | [**fetch_contracts_summary_using_get**](docs/ContractsDataApi.md#fetch_contracts_summary_using_get) | **GET** /v2/contracts | Get the list of contracts summary
*CustomerDataApi* | [**fetch_contracts_details_using_get**](docs/CustomerDataApi.md#fetch_contracts_details_using_get) | **GET** /v1/contract/details | Get the list of contracts Details from flat table. It supports pagination , filtering and sorting
*CustomerDataApi* | [**get_customer_report**](docs/CustomerDataApi.md#get_customer_report) | **GET** /v1/customers/{customerId}/reports/{reportId} | Get the report
*CustomerDataApi* | [**get_customers_life_cycle**](docs/CustomerDataApi.md#get_customers_life_cycle) | **GET** /v1/customers/{customerId}/lifecycle | Get customer lifecycle
*CustomerDataApi* | [**request_customer_report**](docs/CustomerDataApi.md#request_customer_report) | **POST** /v1/customers/{customerId}/reports | Request customer data reports as bulk files
*PartnerDataApi* | [**get_contracts**](docs/PartnerDataApi.md#get_contracts) | **GET** /v1/contracts | List of contracts
*PartnerDataApi* | [**get_customers**](docs/PartnerDataApi.md#get_customers) | **GET** /v1/customers | List of customers
*PartnerDataApi* | [**get_success_tracks**](docs/PartnerDataApi.md#get_success_tracks) | **GET** /v1/successTracks | Success Tracks
*PartnerOffersDataApi* | [**get_partner_offers**](docs/PartnerOffersDataApi.md#get_partner_offers) | **GET** /v1/partnerOffers | Get Partner Offers
*PartnerOffersSessionsDataApi* | [**get_partner_offers_sessions**](docs/PartnerOffersSessionsDataApi.md#get_partner_offers_sessions) | **GET** /v1/partnerOffersSessions | Get Info about Partner Offers Sessions


## Documentation For Models

 - [AccSessionAttendees](docs/AccSessionAttendees.md)
 - [AssetError](docs/AssetError.md)
 - [AssetSession](docs/AssetSession.md)
 - [ContractInfo](docs/ContractInfo.md)
 - [ContractResponse](docs/ContractResponse.md)
 - [ContractsErrorResponse](docs/ContractsErrorResponse.md)
 - [Customer](docs/Customer.md)
 - [CustomerInfo](docs/CustomerInfo.md)
 - [CustomerResponse](docs/CustomerResponse.md)
 - [DataPaginationResponse](docs/DataPaginationResponse.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Pagination](docs/Pagination.md)
 - [PartnerAsset](docs/PartnerAsset.md)
 - [PartnerAssetResponse](docs/PartnerAssetResponse.md)
 - [PartnerOffer](docs/PartnerOffer.md)
 - [PartnerOfferAttendee](docs/PartnerOfferAttendee.md)
 - [PartnerOfferSession](docs/PartnerOfferSession.md)
 - [PartnerOfferWithSessions](docs/PartnerOfferWithSessions.md)
 - [PartnerOffersInfo](docs/PartnerOffersInfo.md)
 - [RacetrackBuid](docs/RacetrackBuid.md)
 - [RacetrackBuidPitstop](docs/RacetrackBuidPitstop.md)
 - [RacetrackBuidPitstopAction](docs/RacetrackBuidPitstopAction.md)
 - [RacetrackBuidSolution](docs/RacetrackBuidSolution.md)
 - [RacetrackTooltip](docs/RacetrackTooltip.md)
 - [RacetrackUsecase](docs/RacetrackUsecase.md)
 - [Reason](docs/Reason.md)
 - [Report](docs/Report.md)
 - [ReportStatus](docs/ReportStatus.md)
 - [SolutionMapping](docs/SolutionMapping.md)
 - [SuccessTrackChecklistMapping](docs/SuccessTrackChecklistMapping.md)
 - [SuccessTrackMapping](docs/SuccessTrackMapping.md)


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

