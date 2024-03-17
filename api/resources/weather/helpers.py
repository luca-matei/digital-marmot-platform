from enum import Enum

from api.config import settings
from api.clients.http import HTTPClient


class APIMethod(str, Enum):
    current = "current"
    forecast = "forecast"


class Weather:
    def __init__(self, city):
        self.weather_api_url = settings.weather_api_url
        self.weather_api_key = settings.weather_api_key
        self.city = city

    def _get_params(self, p: dict = None):
        p = p or {}
        return {
            "key": self.weather_api_key,
            "q": self.city,
            **p,
        }

    async def _get(self, api_method: APIMethod, params: dict = None):
        params = self._get_params(params)
        async with HTTPClient(self.weather_api_url) as client:
            response = await client.get(
                f"/{api_method.value}.json",
                params=params,
            )
            return response.json

    async def get_weather(self):
        return await self._get(APIMethod.current)
