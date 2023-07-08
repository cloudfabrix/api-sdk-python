# cfx_rda_api.DatasetsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_dataset**](DatasetsApi.md#add_dataset) | **POST** /api/v2/datasets | Add a dataset
[**delete_dataset**](DatasetsApi.md#delete_dataset) | **DELETE** /api/v2/datasets/dataset/{name} | Delete a dataset
[**delete_dataset_all_data**](DatasetsApi.md#delete_dataset_all_data) | **DELETE** /api/v2/datasets/dataset/{name}/data/all | Delete enitre data of a dataset
[**delete_dataset_rows**](DatasetsApi.md#delete_dataset_rows) | **DELETE** /api/v2/datasets/dataset/{name}/data | Delete matching dataset rows
[**get_dataset_data**](DatasetsApi.md#get_dataset_data) | **GET** /api/v2/datasets/dataset/{name}/data | Get data of a dataset
[**get_datasets**](DatasetsApi.md#get_datasets) | **GET** /api/v2/datasets | Fetch meta data about datasets
[**update_dataset_data**](DatasetsApi.md#update_dataset_data) | **PUT** /api/v2/datasets/dataset/{name}/data | Update rows of a dataset


# **add_dataset**
> object add_dataset(dataset_add_model)

Add a dataset

Add a dataset.

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.models.dataset_add_model import DatasetAddModel
from cfx_rda_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cfx_rda_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cfx_rda_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfx_rda_api.DatasetsApi(api_client)
    dataset_add_model = cfx_rda_api.DatasetAddModel() # DatasetAddModel | 

    try:
        # Add a dataset
        api_response = api_instance.add_dataset(dataset_add_model)
        print("The response of DatasetsApi->add_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->add_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_add_model** | [**DatasetAddModel**](DatasetAddModel.md)|  | 

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

# **delete_dataset**
> object delete_dataset(name)

Delete a dataset

Delete a dataset. Please note that all the data of the dataset will be deleted and can not be undone.

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cfx_rda_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cfx_rda_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfx_rda_api.DatasetsApi(api_client)
    name = 'name_example' # str | Dataset name to be deleted.

    try:
        # Delete a dataset
        api_response = api_instance.delete_dataset(name)
        print("The response of DatasetsApi->delete_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->delete_dataset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Dataset name to be deleted. | 

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

# **delete_dataset_all_data**
> object delete_dataset_all_data(name)

Delete enitre data of a dataset

Delete entire data of a dataset

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cfx_rda_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cfx_rda_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfx_rda_api.DatasetsApi(api_client)
    name = 'name_example' # str | Name of the dataset

    try:
        # Delete enitre data of a dataset
        api_response = api_instance.delete_dataset_all_data(name)
        print("The response of DatasetsApi->delete_dataset_all_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->delete_dataset_all_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the dataset | 

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

# **delete_dataset_rows**
> object delete_dataset_rows(name, keys, request_body)

Delete matching dataset rows

Delete dataset rows matching the input data     All the rows in existing dataset that match all the keys in input data are deleted.     NOTE: This directly updates the dataset and all drafts are removed.

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cfx_rda_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cfx_rda_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfx_rda_api.DatasetsApi(api_client)
    name = 'name_example' # str | Name of the dataset
    keys = ['keys_example'] # List[str] | Array of keys to match for updating rows
    request_body = None # List[object] | 

    try:
        # Delete matching dataset rows
        api_response = api_instance.delete_dataset_rows(name, keys, request_body)
        print("The response of DatasetsApi->delete_dataset_rows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->delete_dataset_rows: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the dataset | 
 **keys** | [**List[str]**](str.md)| Array of keys to match for updating rows | 
 **request_body** | [**List[object]**](object.md)|  | 

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

# **get_dataset_data**
> TableReportResponse get_dataset_data(name, cfxql_query=cfxql_query, search=search, sort=sort, offset=offset, limit=limit)

Get data of a dataset

Get data of a dataset

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.models.table_report_response import TableReportResponse
from cfx_rda_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cfx_rda_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cfx_rda_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfx_rda_api.DatasetsApi(api_client)
    name = 'name_example' # str | Name of the dataset
    cfxql_query = 'cfxql_query_example' # str | <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results (optional)
    search = 'search_example' # str | search across fields: ['name'] (optional)
    sort = ['sort_example'] # List[str] | Sort the output based on given fields. Prepend '-' to sort descending (optional)
    offset = 0 # int | Offset to start the results from. (optional) (default to 0)
    limit = 100 # int | Maximum number of results to return (optional) (default to 100)

    try:
        # Get data of a dataset
        api_response = api_instance.get_dataset_data(name, cfxql_query=cfxql_query, search=search, sort=sort, offset=offset, limit=limit)
        print("The response of DatasetsApi->get_dataset_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_dataset_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the dataset | 
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

# **get_datasets**
> TableReportResponse get_datasets(cfxql_query=cfxql_query, search=search, offset=offset, limit=limit, sort=sort)

Fetch meta data about datasets

Fetch meta data about datasets

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.models.datasets_enum import DatasetsEnum
from cfx_rda_api.models.table_report_response import TableReportResponse
from cfx_rda_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cfx_rda_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cfx_rda_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfx_rda_api.DatasetsApi(api_client)
    cfxql_query = 'cfxql_query_example' # str | <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results (optional)
    search = 'search_example' # str | search across fields: ['name', 'schema'] (optional)
    offset = 0 # int | Offset to start the results from. (optional) (default to 0)
    limit = 100 # int | Maximum number of results to return (optional) (default to 100)
    sort = ["-timestamp"] # List[DatasetsEnum] | Sort the output based on given fields (optional) (default to ["-timestamp"])

    try:
        # Fetch meta data about datasets
        api_response = api_instance.get_datasets(cfxql_query=cfxql_query, search=search, offset=offset, limit=limit, sort=sort)
        print("The response of DatasetsApi->get_datasets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->get_datasets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cfxql_query** | **str**| &lt;a href&#x3D;&#39;https://bot-docs.cloudfabrix.io/reference_guides/cfxql/&#39;&gt;cfxql query&lt;/a&gt; string to filter the results | [optional] 
 **search** | **str**| search across fields: [&#39;name&#39;, &#39;schema&#39;] | [optional] 
 **offset** | **int**| Offset to start the results from. | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return | [optional] [default to 100]
 **sort** | [**List[DatasetsEnum]**](DatasetsEnum.md)| Sort the output based on given fields | [optional] [default to [&quot;-timestamp&quot;]]

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

# **update_dataset_data**
> object update_dataset_data(name, request_body, replace=replace, keys=keys)

Update rows of a dataset

Update (merge or replace) existing dataset data.     This function currently does not support deleting rows.<br/>     If replace is true, entire existing dataset data is replaced with the new data in input.<br/>     If replace is false, <br/>     <ul>         <li>If keys are not given, the input data is appened to the existing dataset.         <li>If keys are given then the following flow explains the operation<br/>             For each row in the input data:             <ul>                 <li>The rows with same values for all the keys are replaced with input row.                 <li>Other rows are appended to the existing dataset             </ul>         Error raised when:             <ul>                 <li>If there are duplicate rows in input data with same key values                 <li>If any key passed in keys is not present as a column in the input data             </ul>     </ul>     NOTE: This directly updates the dataset and all drafts are removed.

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = cfx_rda_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with cfx_rda_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfx_rda_api.DatasetsApi(api_client)
    name = 'name_example' # str | Name of the dataset
    request_body = None # List[object] | 
    replace = False # bool | If set to true, replace the existing data with new data (optional) (default to False)
    keys = ['keys_example'] # List[str] | Array of keys to match for updating rows (optional)

    try:
        # Update rows of a dataset
        api_response = api_instance.update_dataset_data(name, request_body, replace=replace, keys=keys)
        print("The response of DatasetsApi->update_dataset_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetsApi->update_dataset_data: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the dataset | 
 **request_body** | [**List[object]**](object.md)|  | 
 **replace** | **bool**| If set to true, replace the existing data with new data | [optional] [default to False]
 **keys** | [**List[str]**](str.md)| Array of keys to match for updating rows | [optional] 

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

