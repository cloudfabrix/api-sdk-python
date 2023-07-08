# openapi_client.PipelinesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_draft_pipeline_list_studio**](PipelinesApi.md#get_draft_pipeline_list_studio) | **GET** /api/v2/pipelines/draft | Get list of all pipelines in draft stage
[**get_pipeline_jobs_report**](PipelinesApi.md#get_pipeline_jobs_report) | **GET** /api/v2/pipelines/pipeline/{name}/jobs | Get job details of a pipeline execution
[**get_pipeline_list_studio**](PipelinesApi.md#get_pipeline_list_studio) | **GET** /api/v2/pipelines | Get list of all pipelines
[**get_pipeline_tabular_report**](PipelinesApi.md#get_pipeline_tabular_report) | **GET** /api/v2/pipelines/pipeline/{name} | Get details of a pipeline
[**get_pipeline_tabular_report_0**](PipelinesApi.md#get_pipeline_tabular_report_0) | **GET** /api/v2/pipelines/pipeline/{name}/dependencies | Get dependencies of a pipeline


# **get_draft_pipeline_list_studio**
> BrowseApiResponse get_draft_pipeline_list_studio()

Get list of all pipelines in draft stage

Get list of all pipelines in draft stage

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.browse_api_response import BrowseApiResponse
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
    api_instance = openapi_client.PipelinesApi(api_client)

    try:
        # Get list of all pipelines in draft stage
        api_response = api_instance.get_draft_pipeline_list_studio()
        print("The response of PipelinesApi->get_draft_pipeline_list_studio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_draft_pipeline_list_studio: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BrowseApiResponse**](BrowseApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_jobs_report**
> BrowseApiResponse get_pipeline_jobs_report(name, is_draft=is_draft)

Get job details of a pipeline execution

Get job details of a pipeline execution

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.browse_api_response import BrowseApiResponse
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
    api_instance = openapi_client.PipelinesApi(api_client)
    name = 'name_example' # str | 
    is_draft = False # bool |  (optional) (default to False)

    try:
        # Get job details of a pipeline execution
        api_response = api_instance.get_pipeline_jobs_report(name, is_draft=is_draft)
        print("The response of PipelinesApi->get_pipeline_jobs_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipeline_jobs_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **is_draft** | **bool**|  | [optional] [default to False]

### Return type

[**BrowseApiResponse**](BrowseApiResponse.md)

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

# **get_pipeline_list_studio**
> BrowseApiResponse get_pipeline_list_studio()

Get list of all pipelines

Get list of all pipelines

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.browse_api_response import BrowseApiResponse
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
    api_instance = openapi_client.PipelinesApi(api_client)

    try:
        # Get list of all pipelines
        api_response = api_instance.get_pipeline_list_studio()
        print("The response of PipelinesApi->get_pipeline_list_studio:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipeline_list_studio: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BrowseApiResponse**](BrowseApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pipeline_tabular_report**
> BrowseApiResponse get_pipeline_tabular_report(name, is_draft=is_draft)

Get details of a pipeline

Get details of a pipeline

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.browse_api_response import BrowseApiResponse
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
    api_instance = openapi_client.PipelinesApi(api_client)
    name = 'name_example' # str | 
    is_draft = False # bool |  (optional) (default to False)

    try:
        # Get details of a pipeline
        api_response = api_instance.get_pipeline_tabular_report(name, is_draft=is_draft)
        print("The response of PipelinesApi->get_pipeline_tabular_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipeline_tabular_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **is_draft** | **bool**|  | [optional] [default to False]

### Return type

[**BrowseApiResponse**](BrowseApiResponse.md)

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

# **get_pipeline_tabular_report_0**
> BrowseApiResponse get_pipeline_tabular_report_0(name, is_draft=is_draft)

Get dependencies of a pipeline

Get dependencies of a pipeline

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.browse_api_response import BrowseApiResponse
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
    api_instance = openapi_client.PipelinesApi(api_client)
    name = 'name_example' # str | 
    is_draft = False # bool |  (optional) (default to False)

    try:
        # Get dependencies of a pipeline
        api_response = api_instance.get_pipeline_tabular_report_0(name, is_draft=is_draft)
        print("The response of PipelinesApi->get_pipeline_tabular_report_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesApi->get_pipeline_tabular_report_0: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **is_draft** | **bool**|  | [optional] [default to False]

### Return type

[**BrowseApiResponse**](BrowseApiResponse.md)

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

