# 🚖 Fare Amount Predictor Web App (ML + Streamlit)

This web application allows users to **predict the fare amount for a taxi-uber ride** based on specific ride details.  
It combines **machine learning (XGBOOST)** with a **Streamlit web interface** for end-to-end interaction.

---

## 📚 Table of Contents

- [🎥 Demo](#-demo)
- [✅ What the App Does](#-what-the-app-does)
- [📊 Features Used in the Model](#-features-used-in-the-model)
- [📁 Project Structure](#-project-structure)
- [🧼 Data Exploration & Preprocessing](#-data-exploration--preprocessing)
- [📈 Model Training](#-model-training)
- [🌐 Web App With Streamlit](#-web-app-with-streamlit)
- [📥 Downloads](#-downloads)

---

## 🎥 Demo
🚀 [Live Demo: Uber Fare Predictor App](https://uberfareamountpredictor.streamlit.app/)


https://github.com/user-attachments/assets/08462f5d-2191-4614-a888-2451dc19907f


---

## ✅ What the App Does

1. 🎯 **Predicts Fare Amount of the Ride**  
   Based on input features like:
   - Pickup & dropoff location.
   - Date & time of ride.
   - Distance.
   - Bearing.

2. 📈 **Processes User Input**  
   - Extracts time-based features.
   - Calculates Haversine distance to NYC landmarks.
   - Handles missing or unexpected inputs.

3. 🧠 **Uses a Trained ML Model**  
   A `XGBRegressor` trained on historical taxi-uber data with enriched features.

4. 🌐 **Interactive Web Interface**  
   Users can input ride details and get instant fare prediction via a user-friendly Streamlit app.

---

## 📊 Features Used in the Model.

The model uses the following features:

- `Pickup Longtuide, Pickup Latetitude`.
- `Dropoff Longtuide , Dropoff Latetitude`.
- `hour`, `day`, `month`, `weekday`, `year`.
- `distance` (distance in (miles)).
- `bearing` (direction angle).
- `fare_amount` (target).

---

## 📁 Project Structure.

<img width="390" height="220" alt="Untitled" src="https://github.com/user-attachments/assets/2f0376f0-43c0-4778-a87a-fedb0a1eded5" />


---

## 🧼 Data Exploration & Preprocessing.

- **Exploratory Data Analysis (EDA)** done using `pandas`, `matplotlib`, and `seaborn`.
- Outlier removal for extreme distances and fare values.
- Haversine distance and Fare Amount.

---

## 📈 Model Training

- Algorithm: `XGBRegressor`.
- Framework: `scikit-learn`.
- Steps:
  - Train/test split (80/20).
  - GridSearch for tuning hyperparameters.
  - Model evaluation using RMSE, MAE, and R² score.
- Final model serialized using `pkl` (`Fare_Amount_model.pkl`).

---

## 🌐 Web App with Streamlit.

- Streamlit form takes user inputs for ride parameters.
- Backend loads the trained model and processes features.
- Prediction returned and displayed in results page.

---
### 📥 Downloads

- 📁 **Dataset** (for training & testing):  
  [Download from Google Drive](https://drive.google.com/file/d/1jXXDHk1yST-jvb0q4WCyZtX1bRBV1Hwu/view).
  
- 🎯 **Trained Model & Scaler** you can get them from the Deployment Folder (for predictions):  
  [Download from Google Drive](https://drive.google.com/drive/folders/1s_XpCaOpHuFJbPcdc7uHEx-p2vmo1FoH?usp=sharing).
