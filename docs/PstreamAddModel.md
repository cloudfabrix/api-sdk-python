# PstreamAddModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**attributes** | **object** |  | [optional] 

## Example

```python
from cfx_rda_api.models.pstream_add_model import PstreamAddModel

# TODO update the JSON string below
json = "{}"
# create an instance of PstreamAddModel from a JSON string
pstream_add_model_instance = PstreamAddModel.from_json(json)
# print the JSON string representation of the object
print PstreamAddModel.to_json()

# convert the object into a dict
pstream_add_model_dict = pstream_add_model_instance.to_dict()
# create an instance of PstreamAddModel from a dict
pstream_add_model_form_dict = pstream_add_model.from_dict(pstream_add_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


