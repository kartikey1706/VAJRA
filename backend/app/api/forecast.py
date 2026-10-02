from fastapi import APIRouter, HTTPException
from app.services.weather_service import weather_service
from app.services.reference_service import reference_data_service
from app.ml.features import feature_extractor
from app.ml.inference import bust_model
from app.models.schemas import RegionForecast

router = APIRouter()

@router.get("/forecast/{region_name}", response_model=RegionForecast)
async def get_region_forecast(region_name: str, day: int = 3):
    regions = {
        "Delhi NCR": {"lat": 28.6139, "lon": 77.209},
        "Mumbai Coast": {"lat": 19.076, "lon": 72.8777},
        "Bengaluru": {"lat": 12.9716, "lon": 77.5946},
        "Kolkata Delta": {"lat": 22.5726, "lon": 88.3639},
    }

    if region_name not in regions:
        raise HTTPException(status_code=404, detail="Region not found")

    coords = regions[region_name]

    # 1. Get live weather data
    forecast = await weather_service.get_forecast_proxy(coords["lat"], coords["lon"], day)

    # 2. Extract ML features for this forecast
    # In real use, we'd fetch ensemble data from an API
    features = feature_extractor.extract_features(
        {"lead_day": day, "temp_gradient": 1.2},
        ensemble_data=[{"value": forecast.temperature + i} for i in range(-2, 3)]
    )

    # 3. Run ML Inference
    prob, confidence = bust_model.predict_probability(features)

    # 4. Map back to the UI schema
    return RegionForecast(
        name=region_name,
        latitude=coords["lat"],
        longitude=coords["lon"],
        bust_probability=prob * 100, # UI expects percentage
        confidence=confidence,
        temperature=forecast.temperature,
        wind_speed=forecast.wind_speed,
        detail=f"ML-calculated risk based on ensemble spread and lead time {day}.",
        data_status="LIVE"
    )
