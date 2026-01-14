from enum import Enum
from typing import Optional, Union


class ResponseType(Enum):
    TEXT = "text"
    IMAGE = "image"
    ERROR = "error"


class ChatResponse:
    def __init__(
        self,
        response_type: ResponseType,
        content: Optional[Union[str, bytes]] = None,
        error_message: str = "",
    ):
        self.response_type = (response_type,)
        self.content = (content,)
        self.error_message = error_message
