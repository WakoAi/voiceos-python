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


class ChatGPT(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    GPT_MINUS_4_MINUS_1106_MINUS_PREVIEW = 'gpt-4-1106-preview'
    GPT_MINUS_3_DOT_5_MINUS_TURBO_MINUS_1106 = 'gpt-3.5-turbo-1106'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ChatGPT from a JSON string"""
        return cls(json.loads(json_str))


