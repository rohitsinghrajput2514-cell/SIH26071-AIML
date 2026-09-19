from typing import Optional
from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    rainfall: float = Field(..., ge=0)
    temperature: float = Field(..., ge=-50, le=70)
    humidity: float = Field(..., ge=0, le=100)

    pressure: Optional[float] = None
    wind_speed: Optional[float] = Field(default=None, ge=0)
    latitude: Optional[float] = Field(default=None, ge=-90, le=90)
    longitude: Optional[float] = Field(default=None, ge=-180, le=180)

    soil_moisture: Optional[float] = Field(default=None, ge=0, le=100)
    elevation: Optional[float] = None


class PredictionResponse(BaseModel):
    success: bool
    rainfall: float
    risk_level: str
    risk_score: float
    warning: str
    inundation_risk: str
    prediction: Optional[object] = None
