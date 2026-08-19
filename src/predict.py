from pathlib import Path
import joblib
import pandas as pd


# Find the project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Find the saved model
MODEL_PATH = BASE_DIR / "models" / "house_price_model.pkl"

# Load model
model = joblib.load(MODEL_PATH)


def predict_house_price(
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishingstatus
):
    user_data = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus": [furnishingstatus]
    })

    prediction = model.predict(user_data)

    return prediction[0]