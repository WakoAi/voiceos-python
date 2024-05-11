# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.conversation_response import ConversationResponse

class TestConversationResponse(unittest.TestCase):
    """ConversationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConversationResponse:
        """Test ConversationResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConversationResponse`
        """
        model = ConversationResponse()
        if include_optional:
            return ConversationResponse(
                uri = '',
                type = 'inbound_phone_call',
                account_id = '',
                status = 'started',
                started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                ended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                agent_config = voiceos.models.agent_configuration.AgentConfiguration(
                    initial_message = '', 
                    prompt = '', 
                    voice = null, 
                    language_model = null, 
                    transcriber = null, 
                    max_duration_seconds = 56, 
                    webhooks = [
                        voiceos.models.webhook.Webhook(
                            events = [
                                'phone_call:connection_requested'
                                ], 
                            url = '', 
                            method = null, 
                            headers = {
                                'key' : ''
                                }, 
                            filter = '', )
                        ], 
                    metadata = {
                        'key' : ''
                        }, ),
                agent_id = '',
                messages = [
                    voiceos.models.message.Message(
                        role = null, 
                        content = '', )
                    ],
                phone_call = voiceos.models.twilio_phone_call.TwilioPhoneCall(
                    provider = 'twilio', 
                    to_number = '', 
                    from_number = '', ),
                ended_reason = 'agent_ended',
                cost_breakdown = voiceos.models.conversation_cost.ConversationCost(
                    total = 1.337, 
                    voice = null, 
                    transcriber = null, 
                    language_model = null, 
                    telephony = null, 
                    agent = null, ),
                id = ''
            )
        else:
            return ConversationResponse(
                uri = '',
                type = 'inbound_phone_call',
                account_id = '',
                status = 'started',
                agent_config = voiceos.models.agent_configuration.AgentConfiguration(
                    initial_message = '', 
                    prompt = '', 
                    voice = null, 
                    language_model = null, 
                    transcriber = null, 
                    max_duration_seconds = 56, 
                    webhooks = [
                        voiceos.models.webhook.Webhook(
                            events = [
                                'phone_call:connection_requested'
                                ], 
                            url = '', 
                            method = null, 
                            headers = {
                                'key' : ''
                                }, 
                            filter = '', )
                        ], 
                    metadata = {
                        'key' : ''
                        }, ),
                id = '',
        )
        """

    def testConversationResponse(self):
        """Test ConversationResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()