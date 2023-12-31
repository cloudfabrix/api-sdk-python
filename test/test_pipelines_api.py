# coding: utf-8

"""
    CloudFabrix RDA Platform API

    CloudFabrix RDA Platform API  # noqa: E501

    The version of the OpenAPI document: 3.2.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import openapi_client
from openapi_client.api.pipelines_api import PipelinesApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPipelinesApi(unittest.TestCase):
    """PipelinesApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.pipelines_api.PipelinesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_draft_pipeline_list_studio(self):
        """Test case for get_draft_pipeline_list_studio

        Get list of all pipelines in draft stage  # noqa: E501
        """
        pass

    def test_get_pipeline_jobs_report(self):
        """Test case for get_pipeline_jobs_report

        Get job details of a pipeline execution  # noqa: E501
        """
        pass

    def test_get_pipeline_list_studio(self):
        """Test case for get_pipeline_list_studio

        Get list of all pipelines  # noqa: E501
        """
        pass

    def test_get_pipeline_tabular_report(self):
        """Test case for get_pipeline_tabular_report

        Get details of a pipeline  # noqa: E501
        """
        pass

    def test_get_pipeline_tabular_report_0(self):
        """Test case for get_pipeline_tabular_report_0

        Get dependencies of a pipeline  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
