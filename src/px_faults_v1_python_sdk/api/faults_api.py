"""
    CX Partner Portal APIs

    PX Cloud APIs for the Partners  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: partner-support@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from px_faults_v1_python_sdk.model.affected_assets_response import AffectedAssetsResponse
from px_faults_v1_python_sdk.model.assets_fault_history_response import AssetsFaultHistoryResponse
from px_faults_v1_python_sdk.model.error_response import ErrorResponse
from px_faults_v1_python_sdk.model.faults_response import FaultsResponse
from px_faults_v1_python_sdk.model.faults_summary_response import FaultsSummaryResponse


class FaultsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_affected_assets_details_using_get_endpoint = _Endpoint(
            settings={
                'response_type': (AssetsFaultHistoryResponse,),
                'auth': [
                    'oAuth2'
                ],
                
                'endpoint_path': '/v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets',
                'operation_id': 'get_affected_assets_details_using_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'success_track_id',
                    'customer_id',
                    'fault_id',
                    'days',
                ],
                'required': [
                    'success_track_id',
                    'customer_id',
                    'fault_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'days',
                ]
            },
            root_map={
                'validations': {
                    ('days',): {

                        'inclusive_maximum': 30,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'success_track_id':
                        (str,),
                    'customer_id':
                        (str,),
                    'fault_id':
                        (int,),
                    'days':
                        (int,),
                },
                'attribute_map': {
                    'success_track_id': 'successTrackId',
                    'customer_id': 'customerId',
                    'fault_id': 'faultId',
                    'days': 'days',
                },
                'location_map': {
                    'success_track_id': 'query',
                    'customer_id': 'path',
                    'fault_id': 'path',
                    'days': 'query',
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
        self.get_affected_assets_using_get_endpoint = _Endpoint(
            settings={
                'response_type': (AffectedAssetsResponse,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/faults/{faultId}/affectedAssets',
                'operation_id': 'get_affected_assets_using_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'success_track_id',
                    'customer_id',
                    'fault_id',
                    'days',
                    'offset',
                    'max',
                ],
                'required': [
                    'success_track_id',
                    'customer_id',
                    'fault_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'days',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('days',): {

                        'inclusive_maximum': 30,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'success_track_id':
                        (str,),
                    'customer_id':
                        (str,),
                    'fault_id':
                        (int,),
                    'days':
                        (int,),
                    'offset':
                        (int,),
                    'max':
                        (int,),
                },
                'attribute_map': {
                    'success_track_id': 'successTrackId',
                    'customer_id': 'customerId',
                    'fault_id': 'faultId',
                    'days': 'days',
                    'offset': 'offset',
                    'max': 'max',
                },
                'location_map': {
                    'success_track_id': 'query',
                    'customer_id': 'path',
                    'fault_id': 'path',
                    'days': 'query',
                    'offset': 'query',
                    'max': 'query',
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
        self.get_faults_summary_using_get_endpoint = _Endpoint(
            settings={
                'response_type': (FaultsSummaryResponse,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/faults/{faultId}/summary',
                'operation_id': 'get_faults_summary_using_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'success_track_id',
                    'customer_id',
                    'fault_id',
                ],
                'required': [
                    'success_track_id',
                    'customer_id',
                    'fault_id',
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
                    'fault_id':
                        (int,),
                },
                'attribute_map': {
                    'success_track_id': 'successTrackId',
                    'customer_id': 'customerId',
                    'fault_id': 'faultId',
                },
                'location_map': {
                    'success_track_id': 'query',
                    'customer_id': 'path',
                    'fault_id': 'path',
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
        self.get_faults_using_get_endpoint = _Endpoint(
            settings={
                'response_type': (FaultsResponse,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/insights/faults',
                'operation_id': 'get_faults_using_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'success_track_id',
                    'customer_id',
                    'days',
                    'offset',
                    'max',
                ],
                'required': [
                    'success_track_id',
                    'customer_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'days',
                    'offset',
                ]
            },
            root_map={
                'validations': {
                    ('days',): {

                        'inclusive_maximum': 30,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'success_track_id':
                        (str,),
                    'customer_id':
                        (str,),
                    'days':
                        (int,),
                    'offset':
                        (int,),
                    'max':
                        (int,),
                },
                'attribute_map': {
                    'success_track_id': 'successTrackId',
                    'customer_id': 'customerId',
                    'days': 'days',
                    'offset': 'offset',
                    'max': 'max',
                },
                'location_map': {
                    'success_track_id': 'query',
                    'customer_id': 'path',
                    'days': 'query',
                    'offset': 'query',
                    'max': 'query',
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

    def get_affected_assets_details_using_get(
        self,
        success_track_id,
        customer_id,
        fault_id,
        #asset_name,
        **kwargs
    ):
        """Assets Fault History  # noqa: E501

        Returns information about the occurrences of a fault on an asset based on the fault signatureId, asset name, and customerId provided  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_affected_assets_details_using_get(success_track_id, customer_id, fault_id, asset_name, async_req=True)
        >>> result = thread.get()

        Args:
            success_track_id (str):
            customer_id (str): Unique identifier of the customer
            fault_id (int): Unique identifier used in CX Cloud to identify the fault

        Keyword Args:
            days (int): The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1.. [optional] if omitted the server will use the default value of 1
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
            AssetsFaultHistoryResponse
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
        kwargs['fault_id'] = \
            fault_id
        # kwargs['asset_name'] = \
        #     asset_name
        return self.get_affected_assets_details_using_get_endpoint.call_with_http_info(**kwargs)

    def get_affected_assets_using_get(
        self,
        success_track_id,
        customer_id,
        fault_id,
        **kwargs
    ):
        """Affected Assets  # noqa: E501

        Returns information about the customer assets affected by the fault, based on the fault signatureId and customerId provided  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_affected_assets_using_get(success_track_id, customer_id, fault_id, async_req=True)
        >>> result = thread.get()

        Args:
            success_track_id (str):
            customer_id (str): Unique identifier of the customer
            fault_id (int): Unique identifier used in CX Cloud to identify the fault

        Keyword Args:
            days (int): The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1.. [optional] if omitted the server will use the default value of 1
            offset (int): The number of items to skip before starting to collect the result set. The default value is 1.. [optional] if omitted the server will use the default value of 1
            max (int): The maximum number of items to return.. [optional] if omitted the server will use the default value of 10
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
            AffectedAssetsResponse
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
        kwargs['fault_id'] = \
            fault_id
        return self.get_affected_assets_using_get_endpoint.call_with_http_info(**kwargs)

    def get_faults_summary_using_get(
        self,
        success_track_id,
        customer_id,
        fault_id,
        **kwargs
    ):
        """Fault summary  # noqa: E501

        Returns detailed information for a fault based on the fault signatureId and customerId provided  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_faults_summary_using_get(success_track_id, customer_id, fault_id, async_req=True)
        >>> result = thread.get()

        Args:
            success_track_id (str):
            customer_id (str): Unique identifier of the customer
            fault_id (int): Unique identifier used in CX Cloud to identify the fault

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
            FaultsSummaryResponse
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
        kwargs['fault_id'] = \
            fault_id
        return self.get_faults_summary_using_get_endpoint.call_with_http_info(**kwargs)

    def get_faults_using_get(
        self,
        success_track_id,
        customer_id,
        **kwargs
    ):
        """Faults details  # noqa: E501

        Returns fault information for the customerId provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_faults_using_get(success_track_id, customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            success_track_id (str):
            customer_id (str): Unique identifier of the customer

        Keyword Args:
            days (int): The number of days to retrieve fault data for. This value can be 1, 7, 15, 30. The default is 1.. [optional] if omitted the server will use the default value of 1
            offset (int): The number of items to skip before starting to collect the result set. The default value is 1.. [optional] if omitted the server will use the default value of 1
            max (int): The maximum number of items to return. [optional] if omitted the server will use the default value of 10
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
            FaultsResponse
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
        return self.get_faults_using_get_endpoint.call_with_http_info(**kwargs)

