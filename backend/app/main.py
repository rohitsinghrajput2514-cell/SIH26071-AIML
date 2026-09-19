from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.health import router as health_router
from app.routes.prediction import router as prediction_router
from app.routes.weather import router as weather_router

app = FastAPI(
    title="SIH26071 Weather & Rainfall Prediction API",
    description="Backend API for heavy rainfall early warning and inundation prediction",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(health_router, prefix="/api")
app.include_router(prediction_router, prefix="/api")
app.include_router(weather_router, prefix="/api")


@app.get("/")
def root():
    return {
        "success": True,
        "message": "SIH26071 Backend is running",
        "docs": "/docs"
    }
