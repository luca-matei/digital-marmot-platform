from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    version: str = "0.0.1"

    host_ip: str = "127.0.0.1"
    host_port: int = 4096

    weather_api_url: str = "https://api.weatherapi.com/v1"
    weather_api_key: str

    class Config:
        env_file = ".env"


settings = Settings()
