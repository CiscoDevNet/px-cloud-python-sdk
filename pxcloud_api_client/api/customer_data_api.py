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
from pxcloud_api_client.model.error_response import ErrorResponse
from pxcloud_api_client.model.racetrack_buid import RacetrackBuid
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
        self.lifecycle_endpoint = _Endpoint(settings={
            'response_type': (RacetrackBuid, ),
            'auth': ['oAuth2'],
            'endpoint_path': '/v1/customers/{customerId}/lifecycle',
            'operation_id': 'lifecycle',
            'http_method': 'GET',
            'servers': None,
        },
                                            params_map={
                                                'all': [
                                                    'success_track_id',
                                                    'customer_id',
                                                ],
                                                'required': [
                                                    'success_track_id',
                                                    'customer_id',
                                                ],
                                                'nullable': [],
                                                'enum': [],
                                                'validation': []
                                            },
                                            root_map={
                                                'validations': {},
                                                'allowed_values': {},
                                                'openapi_types': {
                                                    'success_track_id':
                                                    (str, ),
                                                    'customer_id': (str, ),
                                                },
                                                'attribute_map': {
                                                    'success_track_id':
                                                    'successTrackId',
                                                    'customer_id':
                                                    'customerId',
                                                },
                                                'location_map': {
                                                    'success_track_id':
                                                    'query',
                                                    'customer_id': 'path',
                                                },
                                                'collection_format_map': {}
                                            },
                                            headers_map={
                                                'accept': ['application/json'],
                                                'content_type': [],
                                            },
                                            api_client=api_client)
        self.report_summary_endpoint = _Endpoint(settings={
            'response_type': ([ReportStatus], ),
            'auth': ['oAuth2'],
            'endpoint_path':
            '/v1/customers/{customerId}/reports/{reportId}',
            'operation_id':
            'report_summary',
            'http_method':
            'GET',
            'servers':
            None,
        },
                                                 params_map={
                                                     'all': [
                                                         'report_id',
                                                         'customer_id',
                                                     ],
                                                     'required': [
                                                         'report_id',
                                                         'customer_id',
                                                     ],
                                                     'nullable': [],
                                                     'enum': [],
                                                     'validation': []
                                                 },
                                                 root_map={
                                                     'validations': {},
                                                     'allowed_values': {},
                                                     'openapi_types': {
                                                         'report_id': (str, ),
                                                         'customer_id':
                                                         (str, ),
                                                     },
                                                     'attribute_map': {
                                                         'report_id':
                                                         'reportId',
                                                         'customer_id':
                                                         'customerId',
                                                     },
                                                     'location_map': {
                                                         'report_id': 'path',
                                                         'customer_id': 'path',
                                                     },
                                                     'collection_format_map':
                                                     {}
                                                 },
                                                 headers_map={
                                                     'accept':
                                                     ['application/json'],
                                                     'content_type': [],
                                                 },
                                                 api_client=api_client)
        self.reports_endpoint = _Endpoint(settings={
            'response_type': None,
            'auth': ['oAuth2'],
            'endpoint_path': '/v1/customers/{customerId}/reports',
            'operation_id': 'reports',
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
                                              'nullable': [],
                                              'enum': [],
                                              'validation': []
                                          },
                                          root_map={
                                              'validations': {},
                                              'allowed_values': {},
                                              'openapi_types': {
                                                  'customer_id': (str, ),
                                                  'report': (Report, ),
                                              },
                                              'attribute_map': {
                                                  'customer_id': 'customerId',
                                              },
                                              'location_map': {
                                                  'customer_id': 'path',
                                                  'report': 'body',
                                              },
                                              'collection_format_map': {}
                                          },
                                          headers_map={
                                              'accept': ['application/json'],
                                              'content_type':
                                              ['application/json']
                                          },
                                          api_client=api_client)

    def lifecycle(self, success_track_id, customer_id, **kwargs):
        """Get customer lifecycle  # noqa: E501

        Get customer lifecycle which will provide the CX solution, use case and pitstop information for the customer  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lifecycle(success_track_id, customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            success_track_id (str):
            customer_id (str): Unique identifier for the Customer

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
            RacetrackBuid
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
        kwargs['success_track_id'] = \
            success_track_id
        kwargs['customer_id'] = \
            customer_id
        return self.lifecycle_endpoint.call_with_http_info(**kwargs)

    def report_summary(self, report_id, customer_id, **kwargs):
        """Get the report  # noqa: E501

        Provides the status of resource. The status API provides additional info about the progress of the report. Partner application should poll periodically to get status of the report. When the report is complete the API responds with the 303 status pointing to final report in the Location header.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.report_summary(report_id, customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            report_id (str): Report id
            customer_id (str): Unique identifier for the Customer

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
            [ReportStatus]
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
        kwargs['report_id'] = \
            report_id
        kwargs['customer_id'] = \
            customer_id
        return self.report_summary_endpoint.call_with_http_info(**kwargs)

    def reports(self, customer_id, **kwargs):
        """Request customer data reports as bulk files  # noqa: E501

        Request customer data report. Creating a request for customer data sets like Assets, Hardware, Software and Advisories bulk json files  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reports(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Unique identifier for the Customer

        Keyword Args:
            report (Report): report infromation. [optional]
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
        kwargs['customer_id'] = \
            customer_id
        return self.reports_endpoint.call_with_http_info(**kwargs)
