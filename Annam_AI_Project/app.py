import streamlit as st
import pickle
import numpy as np

# 1. Load the pre-trained model
@st.cache_resource
def load_model():
    with open('crop_model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# 2. App Styling & Header
st.set_page_config(page_title="AgroPredict AI", page_icon="🌾", layout="centered")
st.title("🌾 AgroPredict: AI Crop Recommendation System")
st.write("Enter the soil and environmental characteristics below to find the most optimal crop to cultivate.")

st.divider()

# 3. Input Fields organized into Columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 🧪 Soil Nutrients")
    N = st.number_input("Nitrogen (N) ratio in soil", min_value=0, max_value=200, value=90)
    P = st.number_input("Phosphorus (P) ratio in soil", min_value=0, max_value=200, value=42)
    K = st.number_input("Potassium (K) ratio in soil", min_value=0, max_value=200, value=43)
    ph = st.slider("Soil pH level", min_value=0.0, max_value=14.0, value=6.5, step=0.1)

with col2:
    st.markdown("#### 🌤️ Climate Parameters")
    temp = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=25.0)
    humidity = st.slider("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=80.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=500.0, value=200.0)

st.divider()

# 4. Prediction Logic
if st.button("✨ Recommend Optimal Crop", type="primary", use_container_width=True):
    # Format inputs into an array matching model requirements
    features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
    
    # Make prediction
    prediction = model.predict(features)
    recommended_crop = prediction[0].upper()
    
    # Display Result
    st.balloons()
    st.success(f"### 🎉 Recommended Crop: **{recommended_crop}**")
    st.info("💡 *Tip: Ensure proper irrigation according to local weather forecasts for optimal output.*")