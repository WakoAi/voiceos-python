# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.voice_id import VoiceId

class TestVoiceId(unittest.TestCase):
    """VoiceId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VoiceId:
        """Test VoiceId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VoiceId`
        """
        model = VoiceId()
        if include_optional:
            return VoiceId(
            )
        else:
            return VoiceId(
        )
        """

    def testVoiceId(self):
        """Test VoiceId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
