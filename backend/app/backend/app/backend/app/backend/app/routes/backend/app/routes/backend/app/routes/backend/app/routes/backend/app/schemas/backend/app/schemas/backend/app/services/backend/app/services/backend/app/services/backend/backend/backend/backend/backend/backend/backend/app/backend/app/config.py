import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "models"

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    str(MODEL_DIR / "model.pkl")
)

FRONTEND_URL = os.getenv(
    "FRONTEND_URL",
    "*"
)
