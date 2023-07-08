# cfx_rda_api.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_current_user**](UsersApi.md#get_current_user) | **GET** /api/v2/current_user | Get current logged in user details


# **get_current_user**
> UserDetails get_current_user()

Get current logged in user details

Get the details of the current user

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.models.user_details import UserDetails
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
    api_instance = cfx_rda_api.UsersApi(api_client)

    try:
        # Get current logged in user details
        api_response = api_instance.get_current_user()
        print("The response of UsersApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserDetails**](UserDetails.md)

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

