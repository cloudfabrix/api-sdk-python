# cfx_rda_api.AuthenticationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /api/v2/login | Login into api server. (Run this first)


# **login**
> UserDetails login(login_input)

Login into api server. (Run this first)

Login into api server. (Run this first)

### Example

```python
import time
import os
import cfx_rda_api
from cfx_rda_api.models.login_input import LoginInput
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
    api_instance = cfx_rda_api.AuthenticationApi(api_client)
    login_input = cfx_rda_api.LoginInput() # LoginInput | 

    try:
        # Login into api server. (Run this first)
        api_response = api_instance.login(login_input)
        print("The response of AuthenticationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_input** | [**LoginInput**](LoginInput.md)|  | 

### Return type

[**UserDetails**](UserDetails.md)

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

