import base64
from typing import Any, Dict, Literal, Tuple
from core.service.config_service import ConfigService
from core.service.history_service import HistoryService
from core.service.text_generator_service import TextGeneratorService
from core.service.image_generator_service import ImageGeneratorService

import re


class PromptSystemService:

    def __init__(
        self,
        text_generator_service: TextGeneratorService,
        image_generator_service: ImageGeneratorService,
        history_service: HistoryService,
        config_service: ConfigService,
    ) -> None:

        self.text_generator_service = text_generator_service
        self.image_generator_service = image_generator_service
        self.history_service = history_service
        self.config_service = config_service

    def _contains_nsfw(self, prompt: str) -> bool:
        prompt_lower = prompt.lower()
        nsfw_keywords = self.config_service.get_config("filters", "nsfw_keywords")
        whitelist = self.config_service.get_config("filters", "whitelist")

        contains_whitelisted = any(
            re.search(r"\b" + re.escape(term) + r"\b", prompt_lower)
            for term in whitelist
        )

        if contains_whitelisted:
            return False

        pattern = r"\b(?:" + "|".join(re.escape(kw) for kw in nsfw_keywords) + r")\w*"

        return bool(re.search(pattern, prompt_lower))

    def _requires_image(self, prompt: str) -> bool:
        prompt_lower = prompt.lower()
        image_triggers = self.config_service.get_config("triggers", "image_triggers")
        return any(trigger in prompt_lower for trigger in image_triggers)

    def process_prompt(
        self, prompt: str
    ) -> Tuple[Literal["text", "image", "rejected"], Dict[str, Any]]:

        if self._contains_nsfw(prompt):
            return "rejected", {
                "message": "NSFW Content Detected. I can't generate inappropiate content."
            }

        if self._requires_image(prompt):
            img_bytes = self.image_generator_service.generate_image_response(prompt)
            image_base64 = base64.b64encode(img_bytes).decode("utf-8")
            self.history_service.add_interaction(
                prompt=prompt, response=image_base64, response_type="image"
            )
            return "image", {"image_base64": image_base64}

        else:
            answer = self.text_generator_service.generate_text_response(prompt)
            self.history_service.add_interaction(
                prompt=prompt, response=answer, response_type="text"
            )
            return "text", {"answer": answer}
