from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    version: str = "0.0.1"

    class Config:
        env_file = ".env"


settings = Settings()
