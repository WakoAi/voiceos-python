# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AzureModel(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    EN_MINUS_US_MINUS_STEFFAN_NEURAL = 'en-US-SteffanNeural'
    EN_MINUS_US_MINUS_JENNY_NEURAL = 'en-US-JennyNeural'
    EN_MINUS_US_MINUS_ANDREW_NEURAL = 'en-US-AndrewNeural'
    EN_MINUS_US_MINUS_EMMA_NEURAL = 'en-US-EmmaNeural'
    EN_MINUS_US_MINUS_AVA_NEURAL = 'en-US-AvaNeural'
    EN_MINUS_US_MINUS_BRIAN_NEURAL = 'en-US-BrianNeural'
    EN_MINUS_US_MINUS_AVA_MULTILINGUAL_NEURAL = 'en-US-AvaMultilingualNeural'
    EN_MINUS_US_MINUS_JENNY_MULTILINGUAL_NEURAL = 'en-US-JennyMultilingualNeural'
    EN_MINUS_US_MINUS_RYAN_MULTILINGUAL_NEURAL = 'en-US-RyanMultilingualNeural'
    EN_MINUS_US_MINUS_ANDREW_MULTILINGUAL_NEURAL = 'en-US-AndrewMultilingualNeural'
    EN_MINUS_US_MINUS_BRIAN_MULTILINGUAL_NEURAL = 'en-US-BrianMultilingualNeural'
    EN_MINUS_US_MINUS_EMMA_MULTILINGUAL_NEURAL = 'en-US-EmmaMultilingualNeural'
    EN_MINUS_US_MINUS_ALLOY_MULTILINGUAL_NEURAL = 'en-US-AlloyMultilingualNeural'
    EN_MINUS_US_MINUS_ECHO_MULTILINGUAL_NEURAL = 'en-US-EchoMultilingualNeural'
    EN_MINUS_US_MINUS_FABLE_MULTILINGUAL_NEURAL = 'en-US-FableMultilingualNeural'
    EN_MINUS_US_MINUS_NOVA_MULTILINGUAL_NEURAL = 'en-US-NovaMultilingualNeural'
    EN_MINUS_US_MINUS_ONYX_MULTILINGUAL_NEURAL = 'en-US-OnyxMultilingualNeural'
    EN_MINUS_US_MINUS_SHIMMER_MULTILINGUAL_NEURAL = 'en-US-ShimmerMultilingualNeural'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AzureModel from a JSON string"""
        return cls(json.loads(json_str))

