🔥 Calories Burnt Prediction Web App
This project is a machine learning-based web application that predicts the number of calories a person burns during an exercise session based on their physiological and activity-related data. It uses a trained model integrated into a user-friendly Streamlit interface for real-time predictions.

📌 Key Features:
Accepts user inputs: Gender, Age, Height, Weight, Duration, Heart Rate, and Body Temperature.

Predicts calories burnt using a trained machine learning model.

Built with Python, Streamlit, and scikit-learn.

Simple, interactive UI for health-conscious individuals and fitness applications.

🧠 How It Works:
A model is trained using data on physical parameters and calories burned.

The trained model (calories_model.pkl) is loaded in a Streamlit app.

Users enter their data, and the model predicts calories burnt in real time.

📂 Files Included:
calorie_burnt.ipynb – Notebook for data preprocessing, EDA, and model training.

calories_model.pkl – Saved trained model using joblib.

streamlit_app.py – Streamlit script for the interactive prediction app.

📈 Model Performance:
The machine learning model was trained and evaluated using the Random Forest Regressor.

Metric	                                Value
R² Score	                            0.91 (91%)
MAE (Mean Absolute Error)	            ~3.5 kcal
Model Used	                            RandomForestRegressor

