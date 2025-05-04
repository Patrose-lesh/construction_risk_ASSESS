
import streamlit as st
import joblib
import numpy as np

# Load model, vectorizer, and label encoder
model = joblib.load("risk_level_model.pkl")
vectorizer = joblib.load("hazard_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Construction Risk Level Predictor", layout="centered")
st.title("🏗️ Construction Risk Level Predictor")

st.markdown("Predict whether a construction task is **Low**, **Medium**, or **High** risk based on hazard details.")

# Input fields
hazard = st.text_area("📝 Hazard Description", "Struck-by moving equipment")
probability = st.slider("📊 Probability (1–5)", 1, 5, 3)
impact = st.slider("💥 Impact (1–5)", 1, 5, 3)

if st.button("🔍 Predict Risk Level"):
    # Prepare input features
    text_features = vectorizer.transform([hazard]).toarray()
    input_features = np.hstack((text_features, [[probability, impact]]))
    
    # Predict and decode result
    prediction = model.predict(input_features)
    risk_level = label_encoder.inverse_transform(prediction)[0]
    
    # Display result
    st.success(f"✅ Predicted Risk Level: **{risk_level}**")
