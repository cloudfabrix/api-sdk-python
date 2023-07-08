# BrowseApiResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed** | **str** | Datetime representing when the request was completed | [optional] 
**created** | **str** | Datetime representing when the request was createed | [optional] 
**service_error** | **str** | If there is error while processing request. &#39;none&#39; means no error | [optional] 
**service_result** | [**Serviceresult**](Serviceresult.md) |  | [optional] 

## Example

```python
from openapi_client.models.browse_api_response import BrowseApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BrowseApiResponse from a JSON string
browse_api_response_instance = BrowseApiResponse.from_json(json)
# print the JSON string representation of the object
print BrowseApiResponse.to_json()

# convert the object into a dict
browse_api_response_dict = browse_api_response_instance.to_dict()
# create an instance of BrowseApiResponse from a dict
browse_api_response_form_dict = browse_api_response.from_dict(browse_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


