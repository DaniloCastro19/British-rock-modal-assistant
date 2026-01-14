from typing import Any
from src.models.response_schemas import ChatResponse, ResponseType
import requests
from config.settings import GENERATE_RESPONSE_ENDPOINT, GET_HISTORY_ENDPOINT
import base64


def get_chat_response(prompt: str) -> ChatResponse:
    try:
        response = requests.post(
            GENERATE_RESPONSE_ENDPOINT,
            json={"prompt": prompt},
        )

        if response.status_code != 200:
            error_detail = response.json().get("detail", response.text)
            return ChatResponse(
                response_type=ResponseType.ERROR,
                error_message=f"HTTP error {response.status_code}: {error_detail}",
            )

        data = response.json()

        if "answer" in data:
            return ChatResponse(response_type=ResponseType.TEXT, content=data["answer"])

        if "image_base64" in data:
            try:
                image_bytes = base64.b64decode(data["image_base64"])
                return ChatResponse(
                    response_type=ResponseType.IMAGE, content=image_bytes
                )

            except Exception as e:
                return ChatResponse(
                    response_type=ResponseType.ERROR,
                    error_message=f"Image decoding failed: {str(e)}",
                )

    except requests.exceptions.RequestException as e:
        return ChatResponse(
            response_type=ResponseType.ERROR,
            error_message=f"Unexpected error: {str(e)}",
        )


def get_chat_history() -> Any:
    try:
        response = requests.get(GET_HISTORY_ENDPOINT)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching history: {e}")
        return []
