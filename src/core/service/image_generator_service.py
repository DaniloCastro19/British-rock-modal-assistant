from typing import Any
from google.genai import types

from core.service.config_service import ConfigService


class ImageGeneratorService:

    def __init__(
        self, model_client: Any, model_name: str, config_service: ConfigService
    ):
        self.model_client = model_client
        self.model_name = model_name
        self.config_service = config_service

    def generate_image_response(self, prompt: str) -> Any:
        system_prompt = self.config_service.get_config(
            "system_prompts", "image_generation"
        )

        system_prompt = f"{system_prompt} {prompt}"

        response = self.model_client.models.generate_content(
            model=self.model_name,
            contents=system_prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"], candidate_count=1
            ),
        )

        content = response.candidates[0].content

        for part in content.parts:
            if part.inline_data is not None:
                return part.inline_data.data
