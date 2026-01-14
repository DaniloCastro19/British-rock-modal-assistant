from typing import Any
from openai import OpenAI
from google import genai
import os


def build_text_generator_client() -> Any:
    api_key = str(os.getenv("TEXT_MODEL_API_KEY"))
    base_url = str(os.getenv("KEY_PROVIDER_BASE_URL"))
    client = OpenAI(api_key=api_key, base_url=base_url)
    return client


def build_image_generator_client() -> Any:
    api_key = str(os.getenv("IMAGE_GENERATION_API_KEY"))
    client = genai.Client(api_key=api_key)
    return client
