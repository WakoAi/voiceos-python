# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from voiceos.models.conversations_pagination import ConversationsPagination

class TestConversationsPagination(unittest.TestCase):
    """ConversationsPagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConversationsPagination:
        """Test ConversationsPagination
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConversationsPagination`
        """
        model = ConversationsPagination()
        if include_optional:
            return ConversationsPagination(
                items = [
                    voiceos.models.conversation_response.ConversationResponse(
                        uri = '', 
                        type = null, 
                        account_id = '', 
                        status = null, 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        ended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        agent_config = null, 
                        agent_id = '', 
                        messages = [
                            voiceos.models.message.Message(
                                role = null, 
                                content = '', )
                            ], 
                        phone_call = null, 
                        ended_reason = null, 
                        cost_breakdown = null, 
                        id = '', )
                    ],
                index = 56,
                has_more = True
            )
        else:
            return ConversationsPagination(
                items = [
                    voiceos.models.conversation_response.ConversationResponse(
                        uri = '', 
                        type = null, 
                        account_id = '', 
                        status = null, 
                        started_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        ended_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        agent_config = null, 
                        agent_id = '', 
                        messages = [
                            voiceos.models.message.Message(
                                role = null, 
                                content = '', )
                            ], 
                        phone_call = null, 
                        ended_reason = null, 
                        cost_breakdown = null, 
                        id = '', )
                    ],
                index = 56,
                has_more = True,
        )
        """

    def testConversationsPagination(self):
        """Test ConversationsPagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
