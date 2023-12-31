# coding: utf-8

"""
    CloudFabrix RDA Platform API

    CloudFabrix RDA Platform API  # noqa: E501

    The version of the OpenAPI document: 3.2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DashboardsEnum(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    CATEGORY = 'category'
    MINUS_CATEGORY = '-category'
    DESCRIPTION = 'description'
    MINUS_DESCRIPTION = '-description'
    FOLDER = 'folder'
    MINUS_FOLDER = '-folder'
    NAME = 'name'
    MINUS_NAME = '-name'
    SAVED_TIME = 'saved_time'
    MINUS_SAVED_TIME = '-saved_time'
    TIMESTAMP = 'timestamp'
    MINUS_TIMESTAMP = '-timestamp'
    USECASE = 'usecase'
    MINUS_USECASE = '-usecase'
    VERSION = 'version'
    MINUS_VERSION = '-version'
    VERSIONS_COUNT = 'versions_count'
    MINUS_VERSIONS_COUNT = '-versions_count'

    @classmethod
    def from_json(cls, json_str: str) -> DashboardsEnum:
        """Create an instance of DashboardsEnum from a JSON string"""
        return DashboardsEnum(json.loads(json_str))


