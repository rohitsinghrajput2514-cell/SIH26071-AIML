def calculate_risk(
    rainfall: float,
    humidity: float,
    pressure: float | None = None,
    soil_moisture: float | None = None
):
    score = 0.0

    # Rainfall risk
    if rainfall >= 150:
        score += 70
    elif rainfall >= 100:
        score += 55
    elif rainfall >= 64:
        score += 40
    elif rainfall >= 20:
        score += 20
    else:
        score += 5

    # Humidity risk
    if humidity >= 90:
        score += 15
    elif humidity >= 75:
        score += 10
    elif humidity >= 60:
        score += 5

    # Soil moisture risk
    if soil_moisture is not None:
        if soil_moisture >= 80:
            score += 15
        elif soil_moisture >= 60:
            score += 10
        elif soil_moisture >= 40:
            score += 5

    # Atmospheric pressure risk
    if pressure is not None and pressure < 1000:
        score += 5

    # Maximum risk score
    score = min(score, 100)

    # Risk classification
    if score >= 75:
        level = "EXTREME"
        warning = "Extreme rainfall and flood risk detected."
        inundation = "VERY_HIGH"

    elif score >= 55:
        level = "HIGH"
        warning = "Heavy rainfall conditions detected. Flood risk is high."
        inundation = "HIGH"

    elif score >= 35:
        level = "MODERATE"
        warning = "Moderate rainfall risk. Continue monitoring weather conditions."
        inundation = "MODERATE"

    else:
        level = "LOW"
        warning = "No immediate heavy rainfall threat detected."
        inundation = "LOW"

    return {
        "risk_level": level,
        "risk_score": round(score, 2),
        "warning": warning,
        "inundation_risk": inundation
    }
