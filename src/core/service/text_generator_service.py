from typing import Any

from core.service.config_service import ConfigService


class TextGeneratorService:

    def __init__(self, model_client: Any, model: str, config_service: ConfigService):

        self.model_client = model_client
        self.text_generation_model = model
        self.config_service = config_service

    def generate_text_response(self, prompt: str) -> Any:
        system_prompt = self.config_service.get_config(
            "system_prompts", "text_generation"
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ]

        chat = self.model_client.chat.completions.create(
            model=self.text_generation_model,
            messages=messages,
            temperature=0.7,
            max_tokens=1000,
        )

        return chat.choices[0].message.content
