# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.elevenlabs_voice import ElevenlabsVoice

class TestElevenlabsVoice(unittest.TestCase):
    """ElevenlabsVoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ElevenlabsVoice:
        """Test ElevenlabsVoice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ElevenlabsVoice`
        """
        model = ElevenlabsVoice()
        if include_optional:
            return ElevenlabsVoice(
                provider = 'elevenlabs',
                voice_id = None,
                model_id = 'eleven_multilingual_v2',
                optimize_latency = 0.0,
                use_speaker_boost = True,
                similarity_boost = 0.0,
                stability = 0.0
            )
        else:
            return ElevenlabsVoice(
        )
        """

    def testElevenlabsVoice(self):
        """Test ElevenlabsVoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
