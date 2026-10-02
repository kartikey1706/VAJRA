from pydantic import BaseModel
from typing import List, Optional

class WeatherData(BaseModel):
    temperature: float
    wind_speed: float
    pressure: float
    timestamp: str

class RegionForecast(BaseModel):
    name: str
    latitude: float
    longitude: float
    bust_probability: float
    confidence: str
    temperature: Optional[float] = None
    wind_speed: Optional[float] = None
    data_status: str = "LIVE"
    detail: str
