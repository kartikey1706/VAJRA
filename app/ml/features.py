import numpy as np
from typing import List, Dict, Any
from datetime import datetime

class FeatureExtractor:
    """
    Extracts ML features from forecast and ensemble data.
    These features are used by the Bust Model to predict the probability of a forecast bust.
    """
    def extract_features(self, forecast_data: Dict[str, Any], ensemble_data: List[Dict[str, Any]] = None) -> Dict[str, float]:
        # 1. Lead Time Feature (Standardized)
        lead_time = forecast_data.get("lead_day", 1)

        # 2. Temporal Gradient (Change from previous day)
        # In real scenario, we'd fetch D(n-1) and D(n)
        temp_gradient = forecast_data.get("temp_gradient", 0.0)

        # 3. Ensemble Features (The most critical signal for uncertainty)
        ensemble_spread = 0.0
        member_disagreement = 0.0

        if ensemble_data:
            values = [m.get("value", 0) for m in ensemble_data]
            ensemble_spread = np.std(values)
            member_disagreement = np.var(values)

        # 4. Regime Features (Simplified for MVP)
        # 0: Neutral, 1: Active Monsoon, 2: Break Monsoon, 3: Cyclonic
        regime_code = forecast_data.get("regime_code", 0)

        return {
            "lead_time": float(lead_time),
            "temp_gradient": float(temp_gradient),
            "ensemble_spread": float(ensemble_spread),
            "member_disagreement": float(member_disagreement),
            "regime_code": float(regime_code),
        }

feature_extractor = FeatureExtractor()
