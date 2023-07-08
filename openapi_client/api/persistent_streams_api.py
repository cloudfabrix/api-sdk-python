# coding: utf-8

"""
    CloudFabrix RDA Platform API

    CloudFabrix RDA Platform API  # noqa: E501

    The version of the OpenAPI document: 3.2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictStr, conint, conlist

from typing import Any, Optional

from openapi_client.models.pstream_add_model import PstreamAddModel
from openapi_client.models.pstream_edit_model import PstreamEditModel
from openapi_client.models.pstreams_enum import PstreamsEnum
from openapi_client.models.table_report_response import TableReportResponse

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class PersistentStreamsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_pstream(self, pstream_add_model : PstreamAddModel, **kwargs) -> object:  # noqa: E501
        """Add a pstream  # noqa: E501

        Add a new pstream to the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_pstream(pstream_add_model, async_req=True)
        >>> result = thread.get()

        :param pstream_add_model: (required)
        :type pstream_add_model: PstreamAddModel
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_pstream_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_pstream_with_http_info(pstream_add_model, **kwargs)  # noqa: E501

    @validate_arguments
    def add_pstream_with_http_info(self, pstream_add_model : PstreamAddModel, **kwargs) -> ApiResponse:  # noqa: E501
        """Add a pstream  # noqa: E501

        Add a new pstream to the system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_pstream_with_http_info(pstream_add_model, async_req=True)
        >>> result = thread.get()

        :param pstream_add_model: (required)
        :type pstream_add_model: PstreamAddModel
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'pstream_add_model'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_pstream" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['pstream_add_model'] is not None:
            _body_params = _params['pstream_add_model']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "object",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/api/v2/pstreams', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_pstream(self, name : Annotated[StrictStr, Field(..., description="Name of the pstream to be deleted")], delete_data : Annotated[Optional[StrictBool], Field(description="Delete data as well. If data is not deleted, adding the same pstream again will add the old data back.")] = None, **kwargs) -> object:  # noqa: E501
        """Delete a pstream.  # noqa: E501

        Delete a persistent stream.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_pstream(name, delete_data, async_req=True)
        >>> result = thread.get()

        :param name: Name of the pstream to be deleted (required)
        :type name: str
        :param delete_data: Delete data as well. If data is not deleted, adding the same pstream again will add the old data back.
        :type delete_data: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_pstream_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_pstream_with_http_info(name, delete_data, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_pstream_with_http_info(self, name : Annotated[StrictStr, Field(..., description="Name of the pstream to be deleted")], delete_data : Annotated[Optional[StrictBool], Field(description="Delete data as well. If data is not deleted, adding the same pstream again will add the old data back.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Delete a pstream.  # noqa: E501

        Delete a persistent stream.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_pstream_with_http_info(name, delete_data, async_req=True)
        >>> result = thread.get()

        :param name: Name of the pstream to be deleted (required)
        :type name: str
        :param delete_data: Delete data as well. If data is not deleted, adding the same pstream again will add the old data back.
        :type delete_data: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'name',
            'delete_data'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_pstream" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['name']:
            _path_params['name'] = _params['name']


        # process the query parameters
        _query_params = []
        if _params.get('delete_data') is not None:  # noqa: E501
            _query_params.append(('delete_data', _params['delete_data']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "object",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/api/v2/pstreams/pstream/{name}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def edit_pstream(self, name : Annotated[StrictStr, Field(..., description="Name of the pstream to be edited")], pstream_edit_model : PstreamEditModel, **kwargs) -> object:  # noqa: E501
        """Edit attributes of a pstream  # noqa: E501

        Edit the attributes of a persistent stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_pstream(name, pstream_edit_model, async_req=True)
        >>> result = thread.get()

        :param name: Name of the pstream to be edited (required)
        :type name: str
        :param pstream_edit_model: (required)
        :type pstream_edit_model: PstreamEditModel
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the edit_pstream_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.edit_pstream_with_http_info(name, pstream_edit_model, **kwargs)  # noqa: E501

    @validate_arguments
    def edit_pstream_with_http_info(self, name : Annotated[StrictStr, Field(..., description="Name of the pstream to be edited")], pstream_edit_model : PstreamEditModel, **kwargs) -> ApiResponse:  # noqa: E501
        """Edit attributes of a pstream  # noqa: E501

        Edit the attributes of a persistent stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.edit_pstream_with_http_info(name, pstream_edit_model, async_req=True)
        >>> result = thread.get()

        :param name: Name of the pstream to be edited (required)
        :type name: str
        :param pstream_edit_model: (required)
        :type pstream_edit_model: PstreamEditModel
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'name',
            'pstream_edit_model'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method edit_pstream" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['name']:
            _path_params['name'] = _params['name']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['pstream_edit_model'] is not None:
            _body_params = _params['pstream_edit_model']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "object",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/api/v2/pstreams/pstream/{name}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_pstream_data(self, name : Annotated[StrictStr, Field(..., description="Name of the pstream")], cfxql_query : Annotated[Optional[StrictStr], Field(description="<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results")] = None, search : Annotated[Optional[StrictStr], Field(description="search across fields: ['name']")] = None, sort : Annotated[Optional[conlist(StrictStr)], Field(description="Sort the output based on given fields. Prepend '-' to sort descending")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset to start the results from.")] = None, limit : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Maximum number of results to return")] = None, **kwargs) -> TableReportResponse:  # noqa: E501
        """Get data of a pstream  # noqa: E501

        Get data of a persistent stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pstream_data(name, cfxql_query, search, sort, offset, limit, async_req=True)
        >>> result = thread.get()

        :param name: Name of the pstream (required)
        :type name: str
        :param cfxql_query: <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results
        :type cfxql_query: str
        :param search: search across fields: ['name']
        :type search: str
        :param sort: Sort the output based on given fields. Prepend '-' to sort descending
        :type sort: List[str]
        :param offset: Offset to start the results from.
        :type offset: int
        :param limit: Maximum number of results to return
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TableReportResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_pstream_data_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_pstream_data_with_http_info(name, cfxql_query, search, sort, offset, limit, **kwargs)  # noqa: E501

    @validate_arguments
    def get_pstream_data_with_http_info(self, name : Annotated[StrictStr, Field(..., description="Name of the pstream")], cfxql_query : Annotated[Optional[StrictStr], Field(description="<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results")] = None, search : Annotated[Optional[StrictStr], Field(description="search across fields: ['name']")] = None, sort : Annotated[Optional[conlist(StrictStr)], Field(description="Sort the output based on given fields. Prepend '-' to sort descending")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset to start the results from.")] = None, limit : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Maximum number of results to return")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get data of a pstream  # noqa: E501

        Get data of a persistent stream  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pstream_data_with_http_info(name, cfxql_query, search, sort, offset, limit, async_req=True)
        >>> result = thread.get()

        :param name: Name of the pstream (required)
        :type name: str
        :param cfxql_query: <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results
        :type cfxql_query: str
        :param search: search across fields: ['name']
        :type search: str
        :param sort: Sort the output based on given fields. Prepend '-' to sort descending
        :type sort: List[str]
        :param offset: Offset to start the results from.
        :type offset: int
        :param limit: Maximum number of results to return
        :type limit: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TableReportResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'name',
            'cfxql_query',
            'search',
            'sort',
            'offset',
            'limit'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pstream_data" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['name']:
            _path_params['name'] = _params['name']


        # process the query parameters
        _query_params = []
        if _params.get('cfxql_query') is not None:  # noqa: E501
            _query_params.append(('cfxql_query', _params['cfxql_query']))

        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))
            _collection_formats['sort'] = 'multi'

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "TableReportResponse",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/api/v2/pstreams/pstream/{name}/data', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_pstreams(self, cfxql_query : Annotated[Optional[StrictStr], Field(description="<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results")] = None, search : Annotated[Optional[StrictStr], Field(description="search across fields: ['name']")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset to start the results from.")] = None, limit : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Maximum number of results to return")] = None, sort : Annotated[Optional[conlist(PstreamsEnum)], Field(description="Sort the output based on given fields")] = None, **kwargs) -> TableReportResponse:  # noqa: E501
        """Fetch meta data about pstreams  # noqa: E501

        Fetch meta data about pstreams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pstreams(cfxql_query, search, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param cfxql_query: <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results
        :type cfxql_query: str
        :param search: search across fields: ['name']
        :type search: str
        :param offset: Offset to start the results from.
        :type offset: int
        :param limit: Maximum number of results to return
        :type limit: int
        :param sort: Sort the output based on given fields
        :type sort: List[PstreamsEnum]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TableReportResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_pstreams_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_pstreams_with_http_info(cfxql_query, search, offset, limit, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_pstreams_with_http_info(self, cfxql_query : Annotated[Optional[StrictStr], Field(description="<a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results")] = None, search : Annotated[Optional[StrictStr], Field(description="search across fields: ['name']")] = None, offset : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset to start the results from.")] = None, limit : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Maximum number of results to return")] = None, sort : Annotated[Optional[conlist(PstreamsEnum)], Field(description="Sort the output based on given fields")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Fetch meta data about pstreams  # noqa: E501

        Fetch meta data about pstreams  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pstreams_with_http_info(cfxql_query, search, offset, limit, sort, async_req=True)
        >>> result = thread.get()

        :param cfxql_query: <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results
        :type cfxql_query: str
        :param search: search across fields: ['name']
        :type search: str
        :param offset: Offset to start the results from.
        :type offset: int
        :param limit: Maximum number of results to return
        :type limit: int
        :param sort: Sort the output based on given fields
        :type sort: List[PstreamsEnum]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TableReportResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'cfxql_query',
            'search',
            'offset',
            'limit',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pstreams" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('cfxql_query') is not None:  # noqa: E501
            _query_params.append(('cfxql_query', _params['cfxql_query']))

        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))
            _collection_formats['sort'] = 'multi'

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "TableReportResponse",
            '422': "HTTPValidationError",
        }

        return self.api_client.call_api(
            '/api/v2/pstreams', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
