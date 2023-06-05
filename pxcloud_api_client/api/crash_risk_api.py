"""
    PX Cloud for Success Tracks API

    PX Cloud for Success Tracks API  # noqa: E501

    The version of the OpenAPI document: 0.9.11
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pxcloud_api_client.api_client import ApiClient, Endpoint as _Endpoint
from pxcloud_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pxcloud_api_client.model.crash_risk_devices import CrashRiskDevices
from pxcloud_api_client.model.device_crash_detail import DeviceCrashDetail
from pxcloud_api_client.model.device_risk_factors_response import DeviceRiskFactorsResponse
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.inventory_crash_details import InventoryCrashDetails
from pxcloud_api_client.model.similar_devices import SimilarDevices


class CrashRiskApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_crash_asset_crash_history_endpoint = _Endpoint(
            settings={
                'response_type': (DeviceCrashDetail,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/crashRisk/asset/{assetIdBase64}/crashHistory',
                'operation_id': 'get_crash_asset_crash_history',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'asset_id_base64',
                    'success_track_id',
                ],
                'required': [
                    'customer_id',
                    'asset_id_base64',
                    'success_track_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                    'asset_id_base64':
                        (str,),
                    'success_track_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'asset_id_base64': 'assetIdBase64',
                    'success_track_id': 'successTrackId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'asset_id_base64': 'path',
                    'success_track_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_crash_risk_asset_risk_factors_endpoint = _Endpoint(
            settings={
                'response_type': (DeviceRiskFactorsResponse,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/riskFactors',
                'operation_id': 'get_crash_risk_asset_risk_factors',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'success_track_id',
                    'customer_id',
                    'asset_id_base64',
                ],
                'required': [
                    'success_track_id',
                    'customer_id',
                    'asset_id_base64',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'success_track_id':
                        (str,),
                    'customer_id':
                        (str,),
                    'asset_id_base64':
                        (str,),
                },
                'attribute_map': {
                    'success_track_id': 'successTrackId',
                    'customer_id': 'customerId',
                    'asset_id_base64': 'assetIdBase64',
                },
                'location_map': {
                    'success_track_id': 'query',
                    'customer_id': 'path',
                    'asset_id_base64': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_crash_risk_asset_similar_assets_endpoint = _Endpoint(
            settings={
                'response_type': (SimilarDevices,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/crashRisk/assets/{assetIdBase64}/similarAssets',
                'operation_id': 'get_crash_risk_asset_similar_assets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'asset_id_base64',
                    'success_track_id',
                    'similarity_criteria',
                    'max',
                    'offset',
                ],
                'required': [
                    'customer_id',
                    'asset_id_base64',
                    'success_track_id',
                    'similarity_criteria',
                ],
                'nullable': [
                ],
                'enum': [
                    'similarity_criteria',
                ],
                'validation': [
                    'max',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('max',): {

                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('similarity_criteria',): {

                        "FEATURES": "features",
                        "FINGERPRINT": "fingerprint",
                        "SOFTWARE_FEATURES": "software_features"
                    },
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                    'asset_id_base64':
                        (str,),
                    'success_track_id':
                        (str,),
                    'similarity_criteria':
                        (str,),
                    'max':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'asset_id_base64': 'assetIdBase64',
                    'success_track_id': 'successTrackId',
                    'similarity_criteria': 'similarityCriteria',
                    'max': 'max',
                    'offset': 'offset',
                },
                'location_map': {
                    'customer_id': 'path',
                    'asset_id_base64': 'path',
                    'success_track_id': 'query',
                    'similarity_criteria': 'query',
                    'max': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_crash_risk_assets_endpoint = _Endpoint(
            settings={
                'response_type': (CrashRiskDevices,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/crashRisk/assets',
                'operation_id': 'get_crash_risk_assets',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'success_track_id',
                    'max',
                    'offset',
                ],
                'required': [
                    'customer_id',
                    'success_track_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'max',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('max',): {

                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                    'success_track_id':
                        (str,),
                    'max':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'success_track_id': 'successTrackId',
                    'max': 'max',
                    'offset': 'offset',
                },
                'location_map': {
                    'customer_id': 'path',
                    'success_track_id': 'query',
                    'max': 'query',
                    'offset': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_crash_risk_assets_crashed_endpoint = _Endpoint(
            settings={
                'response_type': (InventoryCrashDetails,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/crashRisk/assetsCrashed',
                'operation_id': 'list_crash_risk_assets_crashed',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'success_track_id',
                    'time_period',
                ],
                'required': [
                    'customer_id',
                    'success_track_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'time_period',
                ]
            },
            root_map={
                'validations': {
                    ('time_period',): {

                        'inclusive_maximum': 99,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                    'success_track_id':
                        (str,),
                    'time_period':
                        (int,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'success_track_id': 'successTrackId',
                    'time_period': 'timePeriod',
                },
                'location_map': {
                    'customer_id': 'path',
                    'success_track_id': 'query',
                    'time_period': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_crash_asset_crash_history(
        self,
        customer_id,
        asset_id_base64,
        success_track_id,
        **kwargs
    ):
        """List asset crash history incidents  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_crash_asset_crash_history(customer_id, asset_id_base64, success_track_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Unique identifier of the customer
            asset_id_base64 (str): Base64 encoded value of the `assetId`.
            success_track_id (str):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DeviceCrashDetail
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['customer_id'] = \
            customer_id
        kwargs['asset_id_base64'] = \
            asset_id_base64
        kwargs['success_track_id'] = \
            success_track_id
        return self.get_crash_asset_crash_history_endpoint.call_with_http_info(**kwargs)

    def get_crash_risk_asset_risk_factors(
        self,
        success_track_id,
        customer_id,
        asset_id_base64,
        **kwargs
    ):
        """List crash risk asset risk factors  # noqa: E501

        List factors that contribute to an asset's crash risk score.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_crash_risk_asset_risk_factors(success_track_id, customer_id, asset_id_base64, async_req=True)
        >>> result = thread.get()

        Args:
            success_track_id (str):
            customer_id (str): Unique identifier of the customer
            asset_id_base64 (str): Base64 encoded value of the `assetId`.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DeviceRiskFactorsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['success_track_id'] = \
            success_track_id
        kwargs['customer_id'] = \
            customer_id
        kwargs['asset_id_base64'] = \
            asset_id_base64
        return self.get_crash_risk_asset_risk_factors_endpoint.call_with_http_info(**kwargs)

    def get_crash_risk_asset_similar_assets(
        self,
        customer_id,
        asset_id_base64,
        success_track_id,
        similarity_criteria,
        **kwargs
    ):
        """List crash risk asset similar assets  # noqa: E501

        List other devices in the network that are similar to a device in terms of features , product family, and hardware.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_crash_risk_asset_similar_assets(customer_id, asset_id_base64, success_track_id, similarity_criteria, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Unique identifier of the customer
            asset_id_base64 (str): Base64 encoded value of the `assetId`.
            success_track_id (str):
            similarity_criteria (str): Criteria used to determine whether an asset is similar to the specified asset.

        Keyword Args:
            max (int): The maximum number of items to return. The default value is 10.. [optional] if omitted the server will use the default value of 10
            offset (int): The number of items to skip before starting to collect the result set. The default value is 1.. [optional] if omitted the server will use the default value of 1
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            SimilarDevices
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['customer_id'] = \
            customer_id
        kwargs['asset_id_base64'] = \
            asset_id_base64
        kwargs['success_track_id'] = \
            success_track_id
        kwargs['similarity_criteria'] = \
            similarity_criteria
        return self.get_crash_risk_asset_similar_assets_endpoint.call_with_http_info(**kwargs)

    def get_crash_risk_assets(
        self,
        customer_id,
        success_track_id,
        **kwargs
    ):
        """List assets at risk of crashing  # noqa: E501

        List devices that have a probability of crash, including risk score rating (`High`, `Medium`, `Low`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_crash_risk_assets(customer_id, success_track_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Unique identifier of the customer
            success_track_id (str):

        Keyword Args:
            max (int): The maximum number of items to return. The default value is 10.. [optional] if omitted the server will use the default value of 10
            offset (int): The number of items to skip before starting to collect the result set. The default value is 1.. [optional] if omitted the server will use the default value of 1
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            CrashRiskDevices
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['customer_id'] = \
            customer_id
        kwargs['success_track_id'] = \
            success_track_id
        return self.get_crash_risk_assets_endpoint.call_with_http_info(**kwargs)

    def list_crash_risk_assets_crashed(
        self,
        customer_id,
        success_track_id,
        **kwargs
    ):
        """List assets which have crashed  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_crash_risk_assets_crashed(customer_id, success_track_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Unique identifier of the customer
            success_track_id (str):

        Keyword Args:
            time_period (int): Filter results by X number of days in the past - valid range 1-99.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            InventoryCrashDetails
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['customer_id'] = \
            customer_id
        kwargs['success_track_id'] = \
            success_track_id
        return self.list_crash_risk_assets_crashed_endpoint.call_with_http_info(**kwargs)

