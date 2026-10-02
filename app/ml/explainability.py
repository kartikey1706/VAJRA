from typing import Dict, List, Any

class ExplainabilityService:
    """
    Provides human-readable explanations for the ML model's bust probability.
    """
    def get_explanation(self, features: Dict[str, float], prob: float) -> List[str]:
        reasons = []

        if prob > 0.6:
            if features["ensemble_spread"] > 2.0:
                reasons.append("High ensemble spread indicates significant model disagreement.")
            if features["lead_time"] > 5:
                reasons.append(f"Forecast lead time (Day {int(features['lead_time'])}) is in the high-uncertainty zone.")
            if features["temp_gradient"] > 1.0:
                reasons.append("Rapid temperature transitions detected in the short term.")
        else:
            reasons.append("Consistent ensemble members and low temporal gradients suggest high reliability.")

        if not reasons:
            reasons.append("Atmospheric signals are within normal operational bounds.")

        return reasons

explainability_service = ExplainabilityService()
