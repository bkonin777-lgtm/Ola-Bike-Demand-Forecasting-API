# Ola Bike Demand Forecasting & API Deployment

## 📌 Project Overview
An end-to-end Machine Learning pipeline that predicts 30-minute ride request demand for Ola bike-sharing clusters in real-time. Built using Python, Scikit-Learn, and FastAPI.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Random Forest Regressor)
* **API Framework:** FastAPI, Uvicorn
* **Visualization:** Seaborn, Matplotlib

## 📊 Pipeline Overview
1. **Spatial & Temporal Structuring:** Clustered pickup coordinates into geographic zones and engineered 30-minute and 24-hour historical demand lag features.
2. **Model Training:** Trained a Random Forest Regressor to predict demand count per zone.
3. **Deployment:** Packaged the model into a REST API endpoint serving real-time JSON predictions.

## 🚀 How to Run the API
1. Install dependencies:
```bash
pip install -r requirements.txt

**The Command to start the server:**

```bash
uvicorn app:app --reload

```

**The Endpoint Link for the interactive API documentation:**
`(http://127.0.0.1:8000/docs)`
