# openapi_client.BlueprintsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_blueprints_list**](BlueprintsApi.md#get_blueprints_list) | **GET** /api/v2/blueprints | List all Service Blueprints
[**get_deploymentspec_activity_report**](BlueprintsApi.md#get_deploymentspec_activity_report) | **GET** /api/v2/blueprints/{id}/activity | Gete blueprint service activity report
[**get_deploymentspec_audit_report**](BlueprintsApi.md#get_deploymentspec_audit_report) | **GET** /api/v2/blueprints/{id}/audit | Gete blueprint audit report
[**get_deploymentspec_dependencies_report**](BlueprintsApi.md#get_deploymentspec_dependencies_report) | **GET** /api/v2/blueprints/{id}/dependencies | Get blueprint service dependencies report
[**get_deploymentspec_import_list**](BlueprintsApi.md#get_deploymentspec_import_list) | **GET** /api/v2/blueprints/{id}/imports | Gete blueprint service import list
[**get_deploymentspec_pipeline_report**](BlueprintsApi.md#get_deploymentspec_pipeline_report) | **GET** /api/v2/blueprints/{id}/pipelines | Get blueprint service pipelines report
[**get_deploymentspec_service_map**](BlueprintsApi.md#get_deploymentspec_service_map) | **GET** /api/v2/blueprints/{id}/map | Get blueprint service topology mapping
[**get_deploymentspec_services_status**](BlueprintsApi.md#get_deploymentspec_services_status) | **GET** /api/v2/blueprints/{id}/status | Gete blueprint service status
[**get_deploymentspec_summary_report**](BlueprintsApi.md#get_deploymentspec_summary_report) | **GET** /api/v2/blueprints/{id}/summary | Gete blueprint service summary report
[**get_pipeline_job_report**](BlueprintsApi.md#get_pipeline_job_report) | **GET** /api/v2/blueprints/{id}/jobs | Get blueprint service jobs report


# **get_blueprints_list**
> BrowseApiResponse get_blueprints_list()

List all Service Blueprints

List all Service Blueprints

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
    api_instance = openapi_client.BlueprintsApi(api_client)

    try:
        # List all Service Blueprints
        api_response = api_instance.get_blueprints_list()
        print("The response of BlueprintsApi->get_blueprints_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_blueprints_list: %s\n" % e)
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

# **get_deploymentspec_activity_report**
> BrowseApiResponse get_deploymentspec_activity_report(id, name)

Gete blueprint service activity report

Gete blueprint service activity report

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Gete blueprint service activity report
        api_response = api_instance.get_deploymentspec_activity_report(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_activity_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_activity_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_deploymentspec_audit_report**
> BrowseApiResponse get_deploymentspec_audit_report(id, name)

Gete blueprint audit report

Gete blueprint audit report

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Gete blueprint audit report
        api_response = api_instance.get_deploymentspec_audit_report(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_audit_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_audit_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_deploymentspec_dependencies_report**
> BrowseApiResponse get_deploymentspec_dependencies_report(id, name)

Get blueprint service dependencies report

Get blueprint service dependencies report

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get blueprint service dependencies report
        api_response = api_instance.get_deploymentspec_dependencies_report(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_dependencies_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_dependencies_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_deploymentspec_import_list**
> BrowseApiResponse get_deploymentspec_import_list(id, name)

Gete blueprint service import list

Gete blueprint service import list

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Gete blueprint service import list
        api_response = api_instance.get_deploymentspec_import_list(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_import_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_import_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_deploymentspec_pipeline_report**
> BrowseApiResponse get_deploymentspec_pipeline_report(id, name)

Get blueprint service pipelines report

Get blueprint service pipelines report

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get blueprint service pipelines report
        api_response = api_instance.get_deploymentspec_pipeline_report(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_pipeline_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_pipeline_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_deploymentspec_service_map**
> BrowseApiResponse get_deploymentspec_service_map(id, name)

Get blueprint service topology mapping

Get blueprint service topology mapping

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get blueprint service topology mapping
        api_response = api_instance.get_deploymentspec_service_map(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_service_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_service_map: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_deploymentspec_services_status**
> BrowseApiResponse get_deploymentspec_services_status(id, name)

Gete blueprint service status

Gete blueprint service status

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Gete blueprint service status
        api_response = api_instance.get_deploymentspec_services_status(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_services_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_services_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_deploymentspec_summary_report**
> BrowseApiResponse get_deploymentspec_summary_report(id, name)

Gete blueprint service summary report

Gete blueprint service summary report

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Gete blueprint service summary report
        api_response = api_instance.get_deploymentspec_summary_report(id, name)
        print("The response of BlueprintsApi->get_deploymentspec_summary_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_deploymentspec_summary_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

# **get_pipeline_job_report**
> BrowseApiResponse get_pipeline_job_report(id, name)

Get blueprint service jobs report

Get blueprint service jobs report

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
    api_instance = openapi_client.BlueprintsApi(api_client)
    id = 'id_example' # str | 
    name = 'name_example' # str | 

    try:
        # Get blueprint service jobs report
        api_response = api_instance.get_pipeline_job_report(id, name)
        print("The response of BlueprintsApi->get_pipeline_job_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlueprintsApi->get_pipeline_job_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

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

