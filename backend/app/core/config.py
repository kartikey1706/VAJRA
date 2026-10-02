from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "VAJRA"
    API_V1_STR: str = "/api/v1"

    # Weather API Config
    OPEN_METEO_API_URL: str = "https://api.open-meteo.com/v1/forecast"

    # Future settings
    DATABASE_URL: Optional[str] = None
    MODEL_PATH: Optional[str] = None

    class Config:
        env_file = ".env"

settings = Settings()
