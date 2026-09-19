from fastapi import APIRouter

router = APIRouter(tags=["Weather"])


@router.get("/weather")
def get_weather():
    return {
        "success": True,
        "weather": {
            "temperature": None,
            "humidity": None,
            "pressure": None,
            "wind_speed": None,
            "rainfall": None
        },
        "message": "Weather data endpoint is ready."
    }


@router.get("/alerts")
def get_alerts():
    return {
        "success": True,
        "alerts": []
    }
}
