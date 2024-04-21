from fastapi import APIRouter

from v1.clients.weather import Weather

router = APIRouter(prefix="/weather")


@router.get("")
async def get_weather(city: str):
    weather = await Weather(city).get_weather()
    return weather
