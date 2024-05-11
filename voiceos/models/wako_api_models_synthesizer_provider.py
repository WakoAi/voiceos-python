# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class WakoApiModelsSynthesizerProvider(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    AZURE = 'azure'
    ELEVENLABS = 'elevenlabs'
    RIME = 'rime'
    DEEPGRAM = 'deepgram'
    PLAYHT = 'playht'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WakoApiModelsSynthesizerProvider from a JSON string"""
        return cls(json.loads(json_str))


