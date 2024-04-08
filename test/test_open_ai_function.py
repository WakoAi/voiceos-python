# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.open_ai_function import OpenAIFunction

class TestOpenAIFunction(unittest.TestCase):
    """OpenAIFunction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OpenAIFunction:
        """Test OpenAIFunction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OpenAIFunction`
        """
        model = OpenAIFunction()
        if include_optional:
            return OpenAIFunction(
                name = '',
                wait = True,
                description = '',
                parameters = voiceos.models.open_ai_function_parameter.OpenAIFunctionParameter(
                    type = null, 
                    properties = voiceos.models.properties.Properties(), 
                    required = [
                        ''
                        ], )
            )
        else:
            return OpenAIFunction(
                name = '',
                description = '',
                parameters = voiceos.models.open_ai_function_parameter.OpenAIFunctionParameter(
                    type = null, 
                    properties = voiceos.models.properties.Properties(), 
                    required = [
                        ''
                        ], ),
        )
        """

    def testOpenAIFunction(self):
        """Test OpenAIFunction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
