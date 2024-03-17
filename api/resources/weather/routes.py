from fastapi import APIRouter

from api.clients.weather import Weather

router = APIRouter(prefix="/weather")


@router.get("")
async def get_weather(city: str):
    weather = await Weather(city).get_weather()
    return weather
