import numpy as np
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from typing import Dict, Any, Tuple

MODEL_PATH = "backend/app/ml/bust_model.pkl"

class BustModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
        self.is_trained = False

    def train(self, X: np.ndarray, y: np.ndarray):
        """
        X: feature matrix (lead_time, gradient, spread, disagreement, regime)
        y: binary labels (1 for Bust, 0 for Reliable)
        """
        self.model.fit(X, y)
        self.is_trained = True
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(self.model, f)

    def load(self):
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, 'rb') as f:
                self.model = pickle.load(f)
                self.is_trained = True

    def predict_probability(self, features: Dict[str, float]) -> Tuple[float, str]:
        if not self.is_trained:
            self.load()
            if not self.is_trained:
                # Fallback if model is not yet trained
                return 0.15, "LOW"

        # Convert feature dict to array in correct order
        feature_vector = np.array([[
            features["lead_time"],
            features["temp_gradient"],
            features["ensemble_spread"],
            features["member_disagreement"],
            features["regime_code"]
        ]])

        # Get probability of class 1 (Bust)
        prob = self.model.predict_proba(feature_vector)[0][1]

        # Confidence mapping
        confidence = "LOW"
        if prob > 0.7: confidence = "HIGH"
        elif prob > 0.4: confidence = "MODERATE"

        return float(prob), confidence

bust_model = BustModel()
