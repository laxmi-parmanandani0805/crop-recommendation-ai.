# 🌾 AgroPredict: AI Crop Recommendation System

A simple web application built for the **ANNAM.AI Course at IIT Ropar**. It uses Machine Learning to recommend the best crop to plant based on soil nutrients and weather conditions.

👉 **[Click Here to View the Live App]([[[YOUR_LIVE_STREAMLIT_APP_URL_HERE](https://crop-recommendation-ai-glcpjqcyierfnt8ecvfcjr.streamlit.app/)]**

---

## 📂 Project Files

* `app.py` - The code for the web user interface (Streamlit).
* `crop_model.pkl` - The trained AI model file.
* `requirements.txt` - List of libraries needed to run the app.
* `Crop_recommendation.csv` - The dataset containing soil data.
* `train.py` - Script used to train the machine learning model.

---

## 🚀 How to Run Locally

If you want to run this project on your own computer inside VS Code, follow these quick steps:

1. **Install the required libraries:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Train the Machine Learning Model:**
   Run the training script to process the dataset and generate your saved serialized model file (crop_model.pkl):
   ```bash
   python train.py
   ```
3. **Launch the Web Application:**
   Start up the interactive Streamlit local web server:
   ```bash
   streamlit run app.py
   ```

---

## 📊 How It Works

The application utilizes an advanced Decision Tree Classifier to analyze environmental indicators. You simply enter 7 core parameters into the app interface:
* `🧪Soil Metrics`: Nitrogen (N), Phosphorus (P), Potassium (K), and pH levels.
* `🌤️ Climate Parameters`: Temperature, Humidity, and regional Rainfall.

Once submitted, the AI model instantly processes these inputs against optimized agricultural datasets to predict and display the perfect, high-yielding crop for the farmer to cultivate.
   
