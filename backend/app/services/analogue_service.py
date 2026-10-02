from typing import List, Dict, Any
from app.services.error_db_service import error_db
import numpy as np

class AnalogueEngine:
    """
    Finds historical weather situations similar to the current one
    and returns their verified outcomes.
    """
    def find_analogues(self, current_features: Dict[str, float], top_n: int = 3) -> List[Dict[str, Any]]:
        # 1. Get all historical errors from DB
        records = error_db.get_historical_errors("temperature")
        if not records:
            return []

        # 2. Calculate Euclidean distance between current features and historical records
        # For the MVP, we use the 'error' and 'value' as proxy features
        analogues = []
        for rec in records:
            # rec: (id, forecast_id, valid_time, variable, forecast_val, obs_val, error, is_bust, timestamp)
            dist = abs(rec[6] - 0.0) # Simplification: comparing error magnitude
            analogues.append({
                "date": rec[2],
                "similarity": 1 / (1 + dist),
                "forecast_error": rec[6],
                "is_bust": bool(rec[7]),
                "variable": rec[3]
            })

        # Sort by similarity descending
        analogues.sort(key=lambda x: x["similarity"], reverse=True)
        return analogues[:top_n]

analogue_engine = AnalogueEngine()
