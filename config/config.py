import os
from pydantic_settings import BaseSettings
from dotenv import load_file

ENV = os.getenv("ENV", "dev")
env_path = os.path.join(os.path.dirname(__file__), f"environments/{ENV}.env")

class Settings(BaseSettings):
    BASE_URL: str
    BROWSER: str = "chromium"
    HEADLESS: bool = True
    TIMEOUT: int = 30000
    LOG_LEVEL: str = "INFO"

    class Config:
        env_file = env_path

settings = Settings()
