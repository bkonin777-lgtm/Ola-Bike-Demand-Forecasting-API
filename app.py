from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI(title="Ola Bike Demand API")

# Load the model you saved from Jupyter
payload = joblib.load('ola_model.pkl')
model = payload['model']
feature_names = payload['feature_names']


class DemandRequest(BaseModel):
    hour: int
    mins: int
    day: int
    month: int
    dayofweek: int
    pickup_cluster: int
    lag_1: float
    lag_2: float
    lag_48: float


@app.post("/predict")
def predict_demand(data: DemandRequest):
    input_data = pd.DataFrame([data.dict()])[feature_names]
    prediction = model.predict(input_data)[0]
    predicted_count = max(0, int(np.round(prediction)))

    return {
        "cluster_id": data.pickup_cluster,
        "predicted_bikes_needed": predicted_count
    }