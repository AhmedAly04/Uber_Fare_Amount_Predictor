import streamlit as st
import pandas as pd
import numpy as np
import pickle
import math
from datetime import date
from xgboost import XGBRegressor

model_path = r'X:\ML\Projects\Fare Amount Project\Deployment\Fare_Amount_model.pkl'
pre_path = r'X:\ML\Projects\Fare Amount Project\Deployment\model_preprocessing.pkl'

with open(model_path, 'rb') as f:
    loaded_model = pickle.load(f)
with open(pre_path, 'rb') as f:
    preprocess = pickle.load(f)

scaler = preprocess['scaler']
feature_order = preprocess['feature_order']

def calculate_bearing(lat1, lon1, lat2, lon2, is_radians=False):
    if not is_radians:
        lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(dlon))
    bearing = math.atan2(x, y)
    return -1 * bearing

st.title("🚖 Uber Fare Predictor")

use_raw_radians = st.checkbox("My coordinates are already Radians", value=True)
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.subheader("📍 Pickup")
    pick_lon = st.number_input("Pickup Longitude", value=0.00, format="%.6f")
    pick_lat = st.number_input("Pickup Latitude", value=0.00, format="%.6f")
with col2:
    st.subheader("📍 Dropoff")
    drop_lon = st.number_input("Dropoff Longitude", value=0.00, format="%.6f")
    drop_lat = st.number_input("Dropoff Latitude", value=0.00, format="%.6f")

st.divider()

st.subheader("📅 Time & Date")
d1, d2, d3, d4 = st.columns(4)

with d1:
    hour = st.number_input("Hour", value=12, min_value=0, max_value=23)
with d2:
    day = st.number_input("Day", value=15, min_value=1, max_value=31)
with d3:
    month = st.number_input("Month", value=6, min_value=1, max_value=12)
with d4:
    year = st.number_input("Year", value=2010, min_value=2000, max_value=2050)

curr_date = date(int(year), int(month), int(day))
weekday = curr_date.weekday()
day_name = curr_date.strftime("%A")
st.caption(f"ℹ️ Auto-detected Weekday: **{day_name}**")

st.divider()

st.subheader("📏 Trip Statistics")
m1, m2 = st.columns(2)

with m1:
    distance = st.number_input("Distance (Miles)", value=0.00, format="%.3f")
    
with m2:
    live_bearing = calculate_bearing(pick_lat, pick_lon, drop_lat, drop_lon, is_radians=use_raw_radians)
    st.metric("🧭 Bearing (Auto)", value=f"{live_bearing:.4f} rad")

if st.button("Predict Fare 🚀", type="primary", use_container_width=True):
    try:
        
        bearing_val = calculate_bearing(pick_lat, pick_lon, drop_lat, drop_lon, is_radians=use_raw_radians)

        if use_raw_radians:
            p_lon_final, p_lat_final = pick_lon, pick_lat
            d_lon_final, d_lat_final = drop_lon, drop_lat
        else:
            p_lon_final = np.radians(pick_lon)
            p_lat_final = np.radians(pick_lat)
            d_lon_final = np.radians(drop_lon)
            d_lat_final = np.radians(drop_lat)

        input_data = pd.DataFrame([{
            'pickup_longitude': p_lon_final,
            'pickup_latitude': p_lat_final,
            'dropoff_longitude': d_lon_final,
            'dropoff_latitude': d_lat_final,
            'hour': hour,
            'day': day,
            'month': month,
            'year': year,
            'distance': distance,    
            'bearing': bearing_val   
        }])

        input_encoded = input_data.reindex(columns=feature_order, fill_value=0)

        input_scaled = scaler.transform(input_encoded)
        prediction = loaded_model.predict(input_scaled)
        
        final_fare = abs(prediction[0])
        
        st.success(f"💰 Estimated Fare: ${final_fare:.2f}")

    except Exception as e:

        st.error(f"Prediction Error: {e}")
