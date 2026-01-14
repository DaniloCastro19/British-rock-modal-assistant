import json
import os
from typing import Any, Dict
from data.prompt_keywords.nsfw import nsfw_keywords
from data.prompt_keywords.white_list import white_list
from data.prompt_keywords.image_triggers import image_triggers
from data.prompt_keywords.role_prompts import TEXT_GENERATION_ROLE
from data.prompt_keywords.role_prompts import IMAGE_GENERATION_ROLE


class ConfigService:

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config = self._load_default_config()
        self.load_config()

    def _load_default_config(self) -> Dict[str, Any]:

        return {
            "system_prompts": {
                "text_generation": TEXT_GENERATION_ROLE,
                "image_generation": IMAGE_GENERATION_ROLE,
            },
            "filters": {
                "whitelist": white_list,
                "nsfw_keywords": nsfw_keywords,
            },
            "triggers": {"image_triggers": image_triggers},
        }

    def load_config(self) -> None:
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    self.config = json.load(f)
            except:
                pass

    def save_config(self) -> None:
        with open(self.config_path, "w") as f:
            json.dump(self.config, f)

    def update_config(self, section: str, key: str, value: Any) -> None:

        if section not in self.config:
            self.config[section] = {}

        self.config[section][key] = value
        self.save_config()

    def get_config(self, section: str, key: str) -> Any:

        if section is None:
            return self.config

        section_data = self.config.get(section, {})

        if key is None:
            return section_data

        return section_data.get(key)
