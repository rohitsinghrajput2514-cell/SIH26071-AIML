from pathlib import Path
import pickle

import joblib
import numpy as np

from app.config import MODEL_PATH


class ModelService:

    def __init__(self):
        self.model = None
        self.model_path = Path(MODEL_PATH)
        self.load_model()

    def load_model(self):
        if not self.model_path.exists():
            print(f"Model not found: {self.model_path}")
            self.model = None
            return

        try:
            if self.model_path.suffix.lower() == ".joblib":
                self.model = joblib.load(self.model_path)

            elif self.model_path.suffix.lower() in [".pkl", ".pickle"]:
                with open(self.model_path, "rb") as file:
                    self.model = pickle.load(file)

            else:
                print("Unsupported model format.")
                self.model = None

            print("ML model loaded successfully.")

        except Exception as error:
            print(f"Error loading ML model: {error}")
            self.model = None

    def predict(self, values):

        if self.model is None:
            return None

        try:
            data = np.array([values], dtype=float)

            prediction = self.model.predict(data)

            result = prediction[0]

            if hasattr(result, "item"):
                result = result.item()

            confidence = None

            if hasattr(self.model, "predict_proba"):
                try:
                    probabilities = self.model.predict_proba(data)[0]
                    confidence = float(max(probabilities))
                except Exception:
                    confidence = None

            return {
                "prediction": result,
                "confidence": confidence
            }

        except Exception as error:
            raise RuntimeError(
                f"Model prediction failed: {str(error)}"
            )


model_service = ModelService()
