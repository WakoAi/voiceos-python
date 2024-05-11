# coding: utf-8

"""
    VoiceOS

    VoiceOS API

    The version of the OpenAPI document: 0.8.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from voiceos.models.agent_configuration import AgentConfiguration
from voiceos.models.conversation_cost import ConversationCost
from voiceos.models.conversation_status import ConversationStatus
from voiceos.models.conversation_type import ConversationType
from voiceos.models.ended_reasons import EndedReasons
from voiceos.models.message import Message
from voiceos.models.twilio_phone_call import TwilioPhoneCall
from typing import Optional, Set
from typing_extensions import Self

class ConversationResponse(BaseModel):
    """
    ConversationResponse
    """ # noqa: E501
    uri: StrictStr = Field(description="The uri of the conversation.")
    type: ConversationType = Field(description="The type of conversation.")
    account_id: StrictStr = Field(description="The account id associated with of the conversation.")
    status: ConversationStatus = Field(description="The status of the conversation.")
    started_at: Optional[datetime] = Field(default=None, description="The start time of the conversation.")
    ended_at: Optional[datetime] = Field(default=None, description="The end time of the conversation. Returns null if the conversation is has not ended.")
    agent_config: AgentConfiguration = Field(description="The agent configuration used for the conversation.")
    agent_id: Optional[StrictStr] = Field(default=None, description="The id of the agent used in the conversation. Returns null if the conversation did not use an existing agent.")
    messages: Optional[List[Message]] = Field(default=None, description="The messages of the conversation.")
    phone_call: Optional[TwilioPhoneCall] = Field(default=None, description="The phone call details of the conversation. Returns null if the conversation was over web.")
    ended_reason: Optional[EndedReasons] = Field(default=None, description="The reasons the conversation ended.")
    cost_breakdown: Optional[ConversationCost] = Field(default=None, description="The cost breakdown of the conversation.")
    id: StrictStr = Field(description="The id of the conversation.")
    __properties: ClassVar[List[str]] = ["uri", "type", "account_id", "status", "started_at", "ended_at", "agent_config", "agent_id", "messages", "phone_call", "ended_reason", "cost_breakdown", "id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConversationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of agent_config
        if self.agent_config:
            _dict['agent_config'] = self.agent_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in messages (list)
        _items = []
        if self.messages:
            for _item in self.messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['messages'] = _items
        # override the default output from pydantic by calling `to_dict()` of phone_call
        if self.phone_call:
            _dict['phone_call'] = self.phone_call.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cost_breakdown
        if self.cost_breakdown:
            _dict['cost_breakdown'] = self.cost_breakdown.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConversationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uri": obj.get("uri"),
            "type": obj.get("type"),
            "account_id": obj.get("account_id"),
            "status": obj.get("status"),
            "started_at": obj.get("started_at"),
            "ended_at": obj.get("ended_at"),
            "agent_config": AgentConfiguration.from_dict(obj["agent_config"]) if obj.get("agent_config") is not None else None,
            "agent_id": obj.get("agent_id"),
            "messages": [Message.from_dict(_item) for _item in obj["messages"]] if obj.get("messages") is not None else None,
            "phone_call": TwilioPhoneCall.from_dict(obj["phone_call"]) if obj.get("phone_call") is not None else None,
            "ended_reason": obj.get("ended_reason"),
            "cost_breakdown": ConversationCost.from_dict(obj["cost_breakdown"]) if obj.get("cost_breakdown") is not None else None,
            "id": obj.get("id")
        })
        return _obj

