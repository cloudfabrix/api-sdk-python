# LoginInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from cfx_rda_api.models.login_input import LoginInput

# TODO update the JSON string below
json = "{}"
# create an instance of LoginInput from a JSON string
login_input_instance = LoginInput.from_json(json)
# print the JSON string representation of the object
print LoginInput.to_json()

# convert the object into a dict
login_input_dict = login_input_instance.to_dict()
# create an instance of LoginInput from a dict
login_input_form_dict = login_input.from_dict(login_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


