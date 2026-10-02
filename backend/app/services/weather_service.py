import httpx
from app.core.config import settings
from app.models.schemas import RegionForecast

class WeatherService:
    async def get_forecast_proxy(self, lat: float, lon: float, day: int) -> RegionForecast:
        # This replaces the frontend logic with a backend service
        # For now, it maintains the 'proxy' logic to ensure UI continuity,
        # but it's now encapsulated in the backend.
        async with httpx.AsyncClient() as client:
            params = {
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m,surface_pressure,wind_speed_10m",
                "forecast_days": 10,
                "timezone": "auto"
            }
            response = await client.get(settings.OPEN_METEO_API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # Proxy logic: calculate temp spread for the specific day
            start = (day - 1) * 24
            temps = data["hourly"]["temperature_2m"][start : start + 12]
            temps = [t for t in temps if t is not None]

            spread = max(temps) - min(temps) if temps else 0
            bust_prob = round(min(96.0, max(8.0, 18.0 + spread * 12.0)), 2)

            tone = "low"
            if bust_prob >= 70: tone = "high"
            elif bust_prob >= 40: tone = "moderate"

            return RegionForecast(
                name="Unknown", # Will be set by API
                latitude=lat,
                longitude=lon,
                bust_probability=bust_prob,
                confidence=tone.upper(),
                temperature=temps[0] if temps else None,
                wind_speed=data["hourly"]["wind_speed_10m"][start] if data["hourly"]["wind_speed_10m"] else None,
                detail=f"{spread:.1f}°C temperature range across the next 12 hours from live forecast",
                data_status="LIVE"
            )

weather_service = WeatherService()
