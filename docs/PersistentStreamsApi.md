# openapi_client.PersistentStreamsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pstream**](PersistentStreamsApi.md#add_pstream) | **POST** /api/v2/pstreams | Add a pstream
[**delete_pstream**](PersistentStreamsApi.md#delete_pstream) | **DELETE** /api/v2/pstreams/pstream/{name} | Delete a pstream.
[**edit_pstream**](PersistentStreamsApi.md#edit_pstream) | **PUT** /api/v2/pstreams/pstream/{name} | Edit attributes of a pstream
[**get_pstream_data**](PersistentStreamsApi.md#get_pstream_data) | **GET** /api/v2/pstreams/pstream/{name}/data | Get data of a pstream
[**get_pstreams**](PersistentStreamsApi.md#get_pstreams) | **GET** /api/v2/pstreams | Fetch meta data about pstreams


# **add_pstream**
> object add_pstream(pstream_add_model)

Add a pstream

Add a new pstream to the system

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.pstream_add_model import PstreamAddModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PersistentStreamsApi(api_client)
    pstream_add_model = openapi_client.PstreamAddModel() # PstreamAddModel | 

    try:
        # Add a pstream
        api_response = api_instance.add_pstream(pstream_add_model)
        print("The response of PersistentStreamsApi->add_pstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStreamsApi->add_pstream: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pstream_add_model** | [**PstreamAddModel**](PstreamAddModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pstream**
> object delete_pstream(name, delete_data=delete_data)

Delete a pstream.

Delete a persistent stream.

### Example

```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PersistentStreamsApi(api_client)
    name = 'name_example' # str | Name of the pstream to be deleted
    delete_data = False # bool | Delete data as well. If data is not deleted, adding the same pstream again will add the old data back. (optional) (default to False)

    try:
        # Delete a pstream.
        api_response = api_instance.delete_pstream(name, delete_data=delete_data)
        print("The response of PersistentStreamsApi->delete_pstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStreamsApi->delete_pstream: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the pstream to be deleted | 
 **delete_data** | **bool**| Delete data as well. If data is not deleted, adding the same pstream again will add the old data back. | [optional] [default to False]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_pstream**
> object edit_pstream(name, pstream_edit_model)

Edit attributes of a pstream

Edit the attributes of a persistent stream

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.pstream_edit_model import PstreamEditModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PersistentStreamsApi(api_client)
    name = 'name_example' # str | Name of the pstream to be edited
    pstream_edit_model = openapi_client.PstreamEditModel() # PstreamEditModel | 

    try:
        # Edit attributes of a pstream
        api_response = api_instance.edit_pstream(name, pstream_edit_model)
        print("The response of PersistentStreamsApi->edit_pstream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStreamsApi->edit_pstream: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the pstream to be edited | 
 **pstream_edit_model** | [**PstreamEditModel**](PstreamEditModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pstream_data**
> TableReportResponse get_pstream_data(name, cfxql_query=cfxql_query, search=search, sort=sort, offset=offset, limit=limit)

Get data of a pstream

Get data of a persistent stream

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.table_report_response import TableReportResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PersistentStreamsApi(api_client)
    name = 'name_example' # str | Name of the pstream
    cfxql_query = 'cfxql_query_example' # str | <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results (optional)
    search = 'search_example' # str | search across fields: ['name'] (optional)
    sort = ['sort_example'] # List[str] | Sort the output based on given fields. Prepend '-' to sort descending (optional)
    offset = 0 # int | Offset to start the results from. (optional) (default to 0)
    limit = 100 # int | Maximum number of results to return (optional) (default to 100)

    try:
        # Get data of a pstream
        api_response = api_instance.get_pstream_data(name, cfxql_query=cfxql_query, search=search, sort=sort, offset=offset, limit=limit)
        print("The response of PersistentStreamsApi->get_pstream_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStreamsApi->get_pstream_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the pstream | 
 **cfxql_query** | **str**| &lt;a href&#x3D;&#39;https://bot-docs.cloudfabrix.io/reference_guides/cfxql/&#39;&gt;cfxql query&lt;/a&gt; string to filter the results | [optional] 
 **search** | **str**| search across fields: [&#39;name&#39;] | [optional] 
 **sort** | [**List[str]**](str.md)| Sort the output based on given fields. Prepend &#39;-&#39; to sort descending | [optional] 
 **offset** | **int**| Offset to start the results from. | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return | [optional] [default to 100]

### Return type

[**TableReportResponse**](TableReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pstreams**
> TableReportResponse get_pstreams(cfxql_query=cfxql_query, search=search, offset=offset, limit=limit, sort=sort)

Fetch meta data about pstreams

Fetch meta data about pstreams

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.pstreams_enum import PstreamsEnum
from openapi_client.models.table_report_response import TableReportResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PersistentStreamsApi(api_client)
    cfxql_query = 'cfxql_query_example' # str | <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results (optional)
    search = 'search_example' # str | search across fields: ['name'] (optional)
    offset = 0 # int | Offset to start the results from. (optional) (default to 0)
    limit = 100 # int | Maximum number of results to return (optional) (default to 100)
    sort = ["-timestamp"] # List[PstreamsEnum] | Sort the output based on given fields (optional) (default to ["-timestamp"])

    try:
        # Fetch meta data about pstreams
        api_response = api_instance.get_pstreams(cfxql_query=cfxql_query, search=search, offset=offset, limit=limit, sort=sort)
        print("The response of PersistentStreamsApi->get_pstreams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PersistentStreamsApi->get_pstreams: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cfxql_query** | **str**| &lt;a href&#x3D;&#39;https://bot-docs.cloudfabrix.io/reference_guides/cfxql/&#39;&gt;cfxql query&lt;/a&gt; string to filter the results | [optional] 
 **search** | **str**| search across fields: [&#39;name&#39;] | [optional] 
 **offset** | **int**| Offset to start the results from. | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return | [optional] [default to 100]
 **sort** | [**List[PstreamsEnum]**](PstreamsEnum.md)| Sort the output based on given fields | [optional] [default to [&quot;-timestamp&quot;]]

### Return type

[**TableReportResponse**](TableReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

