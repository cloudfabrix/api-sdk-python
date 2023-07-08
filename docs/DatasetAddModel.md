# DatasetAddModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**folder** | **str** |  | [optional] [default to 'Default']
**schema_name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.dataset_add_model import DatasetAddModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetAddModel from a JSON string
dataset_add_model_instance = DatasetAddModel.from_json(json)
# print the JSON string representation of the object
print DatasetAddModel.to_json()

# convert the object into a dict
dataset_add_model_dict = dataset_add_model_instance.to_dict()
# create an instance of DatasetAddModel from a dict
dataset_add_model_form_dict = dataset_add_model.from_dict(dataset_add_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


