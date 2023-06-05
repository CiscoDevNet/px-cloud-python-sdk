"""
    Partner Experience Cloud API Python SDK

    Partner Experience Cloud API Python SDK - LA Release  # noqa: E501

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
from pxcloud_api_client.model.customer_response import CustomerResponse
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.report import Report
from pxcloud_api_client.model.report_status import ReportStatus


class CustomerDataApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_customers_endpoint = _Endpoint(
            settings={
                'response_type': (CustomerResponse,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers',
                'operation_id': 'get_customers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'max',
                    'offset',
                ],
                'required': [],
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

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'max':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'max': 'max',
                    'offset': 'offset',
                },
                'location_map': {
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
        self.get_report_status_endpoint = _Endpoint(
            settings={
                'response_type': (ReportStatus,),
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/reports/{reportId}',
                'operation_id': 'get_report_status',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'report_id',
                ],
                'required': [
                    'customer_id',
                    'report_id',
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
                    'report_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                    'report_id': 'reportId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'report_id': 'path',
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
        self.post_reports_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oAuth2'
                ],
                'endpoint_path': '/v1/customers/{customerId}/reports',
                'operation_id': 'post_reports',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'report',
                ],
                'required': [
                    'customer_id',
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
                    'report':
                        (Report,),
                },
                'attribute_map': {
                    'customer_id': 'customerId',
                },
                'location_map': {
                    'customer_id': 'path',
                    'report': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def get_customers(
        self,
        **kwargs
    ):
        """List customers  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_customers(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            max (int): Maximum number of items to return. [optional]
            offset (int): Number of items to skip. [optional]
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
            CustomerResponse
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
        return self.get_customers_endpoint.call_with_http_info(**kwargs)

    def get_report_status(
        self,
        customer_id,
        report_id,
        **kwargs
    ):
        """Get report status and location  # noqa: E501

        If report is in-progress (`200 OK`), body will include status description and suggested poll/retry interval.  If ready (`303 See Other`), `Location` header will contain the final report download URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_report_status(customer_id, report_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str):
            report_id (str): reportId returned by a report generation request.

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
            ReportStatus
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
        kwargs['report_id'] = \
            report_id
        return self.get_report_status_endpoint.call_with_http_info(**kwargs)

    def post_reports(
        self,
        customer_id,
        **kwargs
    ):
        """Request customer data report  # noqa: E501

        Report generation is asynchronous. The response `Location` header will contain the report status URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_reports(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str):

        Keyword Args:
            report (Report): Report request details.. [optional]
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
            None
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
        return self.post_reports_endpoint.call_with_http_info(**kwargs)

