# cfx-rda-api
CloudFabrix RDA Platform API

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.2.2
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import cfx_rda_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cfx_rda_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = cfx_rda_api.AuthenticationApi(api_client)
    login_input = cfx_rda_api.LoginInput() # LoginInput | 

    try:
        # Login into api server. (Run this first)
        api_response = api_instance.login(login_input)
        print("The response of AuthenticationApi->login:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthenticationApi->login: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**login**](docs/AuthenticationApi.md#login) | **POST** /api/v2/login | Login into api server. (Run this first)
*DashboardsApi* | [**get_dashboards**](docs/DashboardsApi.md#get_dashboards) | **GET** /api/v2/dashboards | Fetch meta data for dashboards
*DatasetsApi* | [**add_dataset**](docs/DatasetsApi.md#add_dataset) | **POST** /api/v2/datasets | Add a dataset
*DatasetsApi* | [**delete_dataset**](docs/DatasetsApi.md#delete_dataset) | **DELETE** /api/v2/datasets/dataset/{name} | Delete a dataset
*DatasetsApi* | [**delete_dataset_all_data**](docs/DatasetsApi.md#delete_dataset_all_data) | **DELETE** /api/v2/datasets/dataset/{name}/data/all | Delete enitre data of a dataset
*DatasetsApi* | [**delete_dataset_rows**](docs/DatasetsApi.md#delete_dataset_rows) | **DELETE** /api/v2/datasets/dataset/{name}/data | Delete matching dataset rows
*DatasetsApi* | [**get_dataset_data**](docs/DatasetsApi.md#get_dataset_data) | **GET** /api/v2/datasets/dataset/{name}/data | Get data of a dataset
*DatasetsApi* | [**get_datasets**](docs/DatasetsApi.md#get_datasets) | **GET** /api/v2/datasets | Fetch meta data about datasets
*DatasetsApi* | [**update_dataset_data**](docs/DatasetsApi.md#update_dataset_data) | **PUT** /api/v2/datasets/dataset/{name}/data | Update rows of a dataset
*PersistentStreamsApi* | [**add_pstream**](docs/PersistentStreamsApi.md#add_pstream) | **POST** /api/v2/pstreams | Add a pstream
*PersistentStreamsApi* | [**delete_pstream**](docs/PersistentStreamsApi.md#delete_pstream) | **DELETE** /api/v2/pstreams/pstream/{name} | Delete a pstream.
*PersistentStreamsApi* | [**edit_pstream**](docs/PersistentStreamsApi.md#edit_pstream) | **PUT** /api/v2/pstreams/pstream/{name} | Edit attributes of a pstream
*PersistentStreamsApi* | [**get_pstream_data**](docs/PersistentStreamsApi.md#get_pstream_data) | **GET** /api/v2/pstreams/pstream/{name}/data | Get data of a pstream
*PersistentStreamsApi* | [**get_pstreams**](docs/PersistentStreamsApi.md#get_pstreams) | **GET** /api/v2/pstreams | Fetch meta data about pstreams
*UsersApi* | [**get_current_user**](docs/UsersApi.md#get_current_user) | **GET** /api/v2/current_user | Get current logged in user details


## Documentation For Models

 - [DashboardsEnum](docs/DashboardsEnum.md)
 - [DatasetAddModel](docs/DatasetAddModel.md)
 - [DatasetsEnum](docs/DatasetsEnum.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [LocationInner](docs/LocationInner.md)
 - [LoginInput](docs/LoginInput.md)
 - [PstreamAddModel](docs/PstreamAddModel.md)
 - [PstreamEditModel](docs/PstreamEditModel.md)
 - [PstreamsEnum](docs/PstreamsEnum.md)
 - [TableReportResponse](docs/TableReportResponse.md)
 - [UserDetails](docs/UserDetails.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




