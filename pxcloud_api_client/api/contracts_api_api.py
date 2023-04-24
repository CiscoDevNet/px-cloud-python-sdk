"""
    Partner Experience Cloud API Python SDK

    Partner Experience Cloud API Python SDK - LA Release  # noqa: E501

    The version of the OpenAPI document: 0.9.0
    Contact: partner-support@cisco.com
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from pxcloud_api_client.api_client import ApiClient, Endpoint as _Endpoint
from pxcloud_api_client.model_utils import (  # noqa: F401
    check_allowed_values, check_validations, date, datetime, file_type,
    none_type, validate_and_convert_types)
from pxcloud_api_client.model.contract_details_response import ContractDetailsResponse
from pxcloud_api_client.model.contract_response import ContractResponse
from pxcloud_api_client.model.error_response import ErrorResponse


class ContractsAPIApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.contract_details_endpoint = _Endpoint(
            settings={
                'response_type': (ContractDetailsResponse, ),
                'auth': ['oAuth2'],
                'endpoint_path': '/v1/contract/details',
                'operation_id': 'contract_details',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'contract_number',
                    'max',
                    'offset',
                    'customer_id',
                    'component_type',
                    'success_track_id',
                ],
                'required': [
                    'contract_number',
                ],
                'nullable': [],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'contract_number': (int, ),
                    'max': (int, ),
                    'offset': (int, ),
                    'customer_id': (str, ),
                    'component_type': (str, ),
                    'success_track_id': (str, ),
                },
                'attribute_map': {
                    'contract_number': 'contractNumber',
                    'max': 'max',
                    'offset': 'offset',
                    'customer_id': 'customerId',
                    'component_type': 'componentType',
                    'success_track_id': 'successTrackId',
                },
                'location_map': {
                    'contract_number': 'query',
                    'max': 'query',
                    'offset': 'query',
                    'customer_id': 'query',
                    'component_type': 'query',
                    'success_track_id': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)
        self.contracts_endpoint = _Endpoint(settings={
            'response_type': (ContractResponse, ),
            'auth': ['oAuth2'],
            'endpoint_path':
            '/v1/contracts',
            'operation_id':
            'contracts',
            'http_method':
            'GET',
            'servers':
            None,
        },
                                            params_map={
                                                'all': [
                                                    'max',
                                                    'offset',
                                                ],
                                                'required': [],
                                                'nullable': [],
                                                'enum': [],
                                                'validation': []
                                            },
                                            root_map={
                                                'validations': {},
                                                'allowed_values': {},
                                                'openapi_types': {
                                                    'max': (int, ),
                                                    'offset': (int, ),
                                                },
                                                'attribute_map': {
                                                    'max': 'max',
                                                    'offset': 'offset',
                                                },
                                                'location_map': {
                                                    'max': 'query',
                                                    'offset': 'query',
                                                },
                                                'collection_format_map': {}
                                            },
                                            headers_map={
                                                'accept': ['application/json'],
                                                'content_type': [],
                                            },
                                            api_client=api_client)

    def contract_details(self, contract_number, **kwargs):
        """Get the list of contracts Details from flat table. It supports pagination , filtering and sorting  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.contract_details(contract_number, async_req=True)
        >>> result = thread.get()

        Args:
            contract_number (int): contractNumber

        Keyword Args:
            max (int): [optional]
            offset (int): [optional]
            customer_id (str): customerId. [optional]
            component_type (str): componentType. [optional]
            success_track_id (str): successTrackId. [optional]
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
            ContractDetailsResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_spec_property_naming'] = kwargs.get('_spec_property_naming',
                                                     False)
        kwargs['_content_type'] = kwargs.get('_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['contract_number'] = \
            contract_number
        return self.contract_details_endpoint.call_with_http_info(**kwargs)

    def contracts(self, **kwargs):
        """Get the list of customer contracts for a particular partner. It supports pagination with offset and limit parameters , filtering and sorting  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.contracts(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            max (int): [optional]
            offset (int): [optional]
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
            ContractResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_spec_property_naming'] = kwargs.get('_spec_property_naming',
                                                     False)
        kwargs['_content_type'] = kwargs.get('_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.contracts_endpoint.call_with_http_info(**kwargs)
