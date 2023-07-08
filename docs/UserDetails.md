# UserDetails

Response for isUserAuthenticated request. This response contains all the user information that is currently logged in.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **bool** | Whether user is authenticated | [optional] 
**company** | **str** | Company the user belongs to | [optional] 
**first_name** | **str** | First name | [optional] 
**id** | **str** | Id of the user (email address) | [optional] 
**is_authenticated** | **bool** | Alias to &#39;authenticated&#39; | [optional] 
**is_workspaceadmin** | **bool** | Is the user a workspace admin | [optional] 
**is_workspacecreator** | **bool** | Is the user a workspace creator | [optional] 
**last_name** | **bool** | Last Name | [optional] 
**lastname** | **bool** | Alias to last_name | [optional] 
**login_time** | **str** | Login time in ISO format | [optional] 
**rdac_auth_token** | **str** | Authentication Token | [optional] 
**remote_user** | **bool** | Whether user is a remote user or a local user | [optional] 
**role** | **str** | User Role | [optional] 
**session_id** | **str** | Current session id | [optional] 
**status** | **str** | Current status of the user | [optional] 
**tenantid** | **str** | Tenant ID of the user | [optional] 
**user** | **str** | alias to &#39;id&#39; | [optional] 
**workspace** | **str** | Name of the workspace | [optional] 
**workspaceid** | **str** | ID of the workspace | [optional] 

## Example

```python
from cfx_rda_api.models.user_details import UserDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UserDetails from a JSON string
user_details_instance = UserDetails.from_json(json)
# print the JSON string representation of the object
print UserDetails.to_json()

# convert the object into a dict
user_details_dict = user_details_instance.to_dict()
# create an instance of UserDetails from a dict
user_details_form_dict = user_details.from_dict(user_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


