import os
from data.client_builder import (
    build_text_generator_client,
    build_image_generator_client,
)
from core.service.prompt_system_service import PromptSystemService

from core.service.text_generator_service import TextGeneratorService
from core.service.image_generator_service import ImageGeneratorService

from core.service.history_service import HistoryService
from core.service.config_service import ConfigService

text_generation_model_name = str(os.getenv("TEXT_GENERATION_MODEL_NAME"))
image_generation_model_name = str(os.getenv("IMAGE_GENERATION_MODEL_NAME"))

text_generator_client = build_text_generator_client()
image_generator_client = build_image_generator_client()

config_service = ConfigService()

text_model_service = TextGeneratorService(
    text_generator_client, text_generation_model_name, config_service
)
image_model_service = ImageGeneratorService(
    image_generator_client, image_generation_model_name, config_service
)
history_service = HistoryService()

prompt_system_service = PromptSystemService(
    text_model_service, image_model_service, history_service, config_service
)
