from fastapi import APIRouter, HTTPException

from app.schemas.prediction import (
    PredictionRequest,
    PredictionResponse
)

from app.services.risk_service import calculate_risk
from app.services.model_service import model_service

router = APIRouter(tags=["Prediction"])


@router.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(request: PredictionRequest):

    risk = calculate_risk(
        rainfall=request.rainfall,
        humidity=request.humidity,
        pressure=request.pressure,
        soil_moisture=request.soil_moisture
    )

    model_prediction = None

    values = [
        request.rainfall,
        request.temperature,
        request.humidity,
        request.pressure or 0,
        request.wind_speed or 0
    ]

    try:
        model_prediction = model_service.predict(values)
    except RuntimeError as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

    return {
        "success": True,
        "rainfall": request.rainfall,
        "risk_level": risk["risk_level"],
        "risk_score": risk["risk_score"],
        "warning": risk["warning"],
        "inundation_risk": risk["inundation_risk"],
        "prediction": model_prediction
    }


@router.post("/rainfall/predict")
def rainfall_prediction(request: PredictionRequest):

    risk = calculate_risk(
        rainfall=request.rainfall,
        humidity=request.humidity,
        pressure=request.pressure,
        soil_moisture=request.soil_moisture
    )

    return {
        "success": True,
        "type": "rainfall_prediction",
        "rainfall": request.rainfall,
        **risk
    }


@router.post("/inundation/predict")
def inundation_prediction(request: PredictionRequest):

    risk = calculate_risk(
        rainfall=request.rainfall,
        humidity=request.humidity,
        pressure=request.pressure,
        soil_moisture=request.soil_moisture
    )

    return {
        "success": True,
        "type": "inundation_prediction",
        "inundation_risk": risk["inundation_risk"],
        "risk_score": risk["risk_score"],
        "risk_level": risk["risk_level"]
    }
