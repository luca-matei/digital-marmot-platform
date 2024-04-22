from fastapi import APIRouter

from v1.clients.weather import Weather

router = APIRouter(prefix="/weather")


@router.get("")
async def get_weather(city: str):
    return {"location":{"name":"Bucharest","region":"Bucuresti","country":"Romania","lat":44.43,"lon":26.1,"tz_id":"Europe/Bucharest","localtime_epoch":1710717083,"localtime":"2024-03-18 1:11"},"current":{"last_updated_epoch":1710716400,"last_updated":"2024-03-18 01:00","temp_c":9.0,"temp_f":48.2,"is_day":0,"condition":{"text":"Clear","icon":"//cdn.weatherapi.com/weather/64x64/night/113.png","code":1000},"wind_mph":3.8,"wind_kph":6.1,"wind_degree":260,"wind_dir":"W","pressure_mb":1015.0,"pressure_in":29.97,"precip_mm":0.0,"precip_in":0.0,"humidity":81,"cloud":0,"feelslike_c":6.8,"feelslike_f":44.2,"vis_km":10.0,"vis_miles":6.0,"uv":1.0,"gust_mph":13.4,"gust_kph":21.5}}

    weather = await Weather(city).get_weather()
    return weather
