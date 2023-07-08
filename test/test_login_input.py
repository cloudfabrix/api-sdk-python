# coding: utf-8

"""
    CloudFabrix RDA Platform API

    CloudFabrix RDA Platform API  # noqa: E501

    The version of the OpenAPI document: 3.2.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import openapi_client
from openapi_client.models.login_input import LoginInput  # noqa: E501
from openapi_client.rest import ApiException

class TestLoginInput(unittest.TestCase):
    """LoginInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoginInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginInput`
        """
        model = openapi_client.models.login_input.LoginInput()  # noqa: E501
        if include_optional :
            return LoginInput(
                user = '', 
                password = ''
            )
        else :
            return LoginInput(
                user = '',
                password = '',
        )
        """

    def testLoginInput(self):
        """Test LoginInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
