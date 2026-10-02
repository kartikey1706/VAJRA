from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Observation(BaseModel):
    timestamp: datetime
    latitude: float
    longitude: float
    variable: str
    value: float
    source: str
    quality_flag: int = 0

class VerificationRecord(BaseModel):
    forecast_id: str
    valid_time: datetime
    variable: str
    forecast_value: float
    observed_value: float
    error: float
    is_bust: bool
    regime: Optional[str] = None
