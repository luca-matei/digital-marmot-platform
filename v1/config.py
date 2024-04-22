from uuid import UUID

from pydantic_settings import BaseSettings

LOCALHOST = "127.0.0.1"


class Settings(BaseSettings):
    version: str = "0.0.1"

    host_ip: str = LOCALHOST
    host_port: int = 4096

    db_user: str = "postgres"
    db_password: str = ""
    db_host: str = LOCALHOST
    db_port: int = 5432
    db_name: str = "postgres"
    db_url: str = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

    redis_host: str = LOCALHOST
    redis_port: int = 6379
    redis_user: str = "default"
    redis_password: str = ""

    weather_api_url: str = "https://api.weatherapi.com/v1"
    weather_api_key: str

    superuser_id: UUID

    class Config:
        env_file = ".env"


settings = Settings()
