# cfx_rda_api.DashboardsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dashboards**](DashboardsApi.md#get_dashboards) | **GET** /api/v2/dashboards | Fetch meta data for dashboards


# **get_dashboards**
> TableReportResponse get_dashboards(cfxql_query=cfxql_query, search=search, offset=offset, limit=limit, sort=sort)

Fetch meta data for dashboards

Fetch meta data for dashboards

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.models.dashboards_enum import DashboardsEnum
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
    api_instance = cfx_rda_api.DashboardsApi(api_client)
    cfxql_query = 'cfxql_query_example' # str | <a href='https://bot-docs.cloudfabrix.io/reference_guides/cfxql/'>cfxql query</a> string to filter the results (optional)
    search = 'search_example' # str | search across fields: ['name', 'description', 'usecase', 'category', 'version'] (optional)
    offset = 0 # int | Offset to start the results from. (optional) (default to 0)
    limit = 100 # int | Maximum number of results to return (optional) (default to 100)
    sort = ["-timestamp"] # List[DashboardsEnum] | Sort the output based on given fields (optional) (default to ["-timestamp"])

    try:
        # Fetch meta data for dashboards
        api_response = api_instance.get_dashboards(cfxql_query=cfxql_query, search=search, offset=offset, limit=limit, sort=sort)
        print("The response of DashboardsApi->get_dashboards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DashboardsApi->get_dashboards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cfxql_query** | **str**| &lt;a href&#x3D;&#39;https://bot-docs.cloudfabrix.io/reference_guides/cfxql/&#39;&gt;cfxql query&lt;/a&gt; string to filter the results | [optional] 
 **search** | **str**| search across fields: [&#39;name&#39;, &#39;description&#39;, &#39;usecase&#39;, &#39;category&#39;, &#39;version&#39;] | [optional] 
 **offset** | **int**| Offset to start the results from. | [optional] [default to 0]
 **limit** | **int**| Maximum number of results to return | [optional] [default to 100]
 **sort** | [**List[DashboardsEnum]**](DashboardsEnum.md)| Sort the output based on given fields | [optional] [default to [&quot;-timestamp&quot;]]

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

