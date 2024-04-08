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


class EventName(str, Enum):
    """
    An enumeration.
    """

    """
    allowed enum values
    """
    OPENAI_FUNCTION_CALL_TRIGGERED = 'openai_function_call_triggered'
    CALL_STARTED = 'call_started'
    MESSAGE = 'message'
    CALL_ENDED = 'call_ended'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventName from a JSON string"""
        return cls(json.loads(json_str))


