from typing import Dict
from app.models.verification import VerificationRecord, Observation
import numpy as np

class VerificationEngine:
    def __init__(self):
        # Configurable thresholds for 'Bust' definition
        # variable -> absolute_error_threshold
        self.thresholds = {
            "temperature": 3.0,    # Bust if error > 3°C
            "precipitation": 10.0, # Bust if error > 10mm
            "wind_speed": 5.0,     # Bust if error > 5km/h
        }

    def calculate_error(self, forecast_val: float, obs_val: float) -> float:
        return abs(forecast_val - obs_val)

    async def verify_forecast(
        self,
        forecast_id: str,
        variable: str,
        forecast_val: float,
        obs: Observation
    ) -> VerificationRecord:
        error = self.calculate_error(forecast_val, obs.value)

        # Determine if it's a bust based on the variable-specific threshold
        threshold = self.thresholds.get(variable, 5.0)
        is_bust = error > threshold

        return VerificationRecord(
            forecast_id=forecast_id,
            valid_time=obs.timestamp,
            variable=variable,
            forecast_value=forecast_val,
            observed_value=obs.value,
            error=error,
            is_bust=is_bust
        )

verification_engine = VerificationEngine()
