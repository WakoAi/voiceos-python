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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from voiceos.models.wako_api_models_language_model_provider import WakoApiModelsLanguageModelProvider
from typing import Optional, Set
from typing_extensions import Self

class LanguageModelCost(BaseModel):
    """
    LanguageModelCost
    """ # noqa: E501
    provider: WakoApiModelsLanguageModelProvider = Field(description="The provider of the language model.")
    cost: Union[StrictFloat, StrictInt] = Field(description="The cost for the language model usage (USD).")
    input_tokens: StrictInt = Field(description="The number of input tokens used for the language model.")
    output_tokens: StrictInt = Field(description="The number of output tokens used for the language model.")
    __properties: ClassVar[List[str]] = ["provider", "cost", "input_tokens", "output_tokens"]

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
        """Create an instance of LanguageModelCost from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LanguageModelCost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "provider": obj.get("provider"),
            "cost": obj.get("cost"),
            "input_tokens": obj.get("input_tokens"),
            "output_tokens": obj.get("output_tokens")
        })
        return _obj


