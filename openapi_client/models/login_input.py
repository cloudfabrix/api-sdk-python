# coding: utf-8

"""
    CloudFabrix RDA Platform API

    CloudFabrix RDA Platform API  # noqa: E501

    The version of the OpenAPI document: 3.2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, StrictStr

class LoginInput(BaseModel):
    """
    LoginInput
    """
    user: StrictStr = Field(...)
    password: StrictStr = Field(...)
    __properties = ["user", "password"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> LoginInput:
        """Create an instance of LoginInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LoginInput:
        """Create an instance of LoginInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LoginInput.parse_obj(obj)

        _obj = LoginInput.parse_obj({
            "user": obj.get("user"),
            "password": obj.get("password")
        })
        return _obj

