from typing import Any
from pydantic import BaseModel


class TextRequest(BaseModel):
    prompt: str


class ImageRequest(BaseModel):
    prompt: str


class UpdateConfigRequest(BaseModel):
    section: str
    key: str
    value: Any
