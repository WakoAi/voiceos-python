# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.webhook import Webhook

class TestWebhook(unittest.TestCase):
    """Webhook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Webhook:
        """Test Webhook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Webhook`
        """
        model = Webhook()
        if include_optional:
            return Webhook(
                event = None,
                url = '',
                method = 'GET',
                headers = {
                    'key' : ''
                    },
                filter = {
                    'key' : 56
                    }
            )
        else:
            return Webhook(
                event = None,
                url = '',
                method = 'GET',
        )
        """

    def testWebhook(self):
        """Test Webhook"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
