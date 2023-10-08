import os

from dotenv import load_dotenv

load_dotenv()

config_list = [{"model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY")}]

llm_config = {"config_list": config_list, "seed": 42, "temperature": 0}