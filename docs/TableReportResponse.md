# TableReportResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_sort_results** | **List[str]** | Last sort tags used for internal puposes | [optional] 
**report_meta_data** | **object** | Meta information about the report, including columns and types etc | [optional] 
**offset** | **int** | Starting offset in the filtered results | [optional] 
**limit** | **int** | Maximum number of results to be returned per page | [optional] 
**sort** | **List[str]** | Sort order passed as part of request | [optional] 
**total_count** | **int** | Total number of results that matched the query | [optional] 
**num_items** | **int** | Number of results returned in this page | [optional] 
**is_first** | **bool** | True if this page is first page | [optional] [default to True]
**is_last** | **bool** | True if this page is last page | [optional] [default to True]

## Example

```python
from openapi_client.models.table_report_response import TableReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TableReportResponse from a JSON string
table_report_response_instance = TableReportResponse.from_json(json)
# print the JSON string representation of the object
print TableReportResponse.to_json()

# convert the object into a dict
table_report_response_dict = table_report_response_instance.to_dict()
# create an instance of TableReportResponse from a dict
table_report_response_form_dict = table_report_response.from_dict(table_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


