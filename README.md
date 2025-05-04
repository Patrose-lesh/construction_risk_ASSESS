
# 🏗️ Construction Risk Level Predictor

This Streamlit web app predicts the **risk level (Low, Medium, High)** of construction tasks based on:
- The **hazard description**
- The **probability** of occurrence (1–5)
- The **impact** severity (1–5)

## 🚀 How to Use

### Online (Streamlit Cloud)
1. Upload all files to a new GitHub repo:
   - `streamlit_app.py`
   - `risk_level_model.pkl`
   - `hazard_vectorizer.pkl`
   - `label_encoder.pkl`
   - `requirements.txt`
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your GitHub and select the repo
4. Set **main file path** to: `streamlit_app.py`
5. Click **Deploy**

### Local Setup
```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 🧠 Model Info
- **Model**: Random Forest Classifier
- **Text Feature**: TF-IDF Vectorizer on hazard descriptions
- **Target**: Risk Level (High, Medium, Low)

## 📄 License
This app is for educational and demonstration purposes.
