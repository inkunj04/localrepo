# 🔥 Calories Burnt Prediction Web App

This is a machine learning-based web application that predicts the number of calories burned during exercise using physiological and activity-related input data.  
It’s powered by a trained model and a Streamlit interface for real-time predictions with a sleek, interactive user experience.

---

## 🎯 Key Features

- Accepts user inputs:
  - Gender
  - Age
  - Height (cm)
  - Weight (kg)
  - Exercise Duration (minutes)
  - Heart Rate
  - Body Temperature
- Predicts calories burned in real-time
- Powered by a machine learning model (`RandomForestRegressor`)
- Interactive and beginner-friendly UI using **Streamlit**
- Lightweight and deployable for personal or demo use

---

## 🧠 How It Works

1. A machine learning model is trained on a labeled dataset of physical parameters and calories burned.
2. The model is saved using `joblib` as `calories_model.pkl`.
3. A **Streamlit** app (`streamlit_app.py`) loads the model and allows users to input data.
4. On submission, the app predicts and displays the number of calories burned based on the input.

---

## 📁 Files Included

- `📓 calorie_burnt.ipynb` – Model training, preprocessing, and EDA
- `📦 calories_model.pkl` – Saved trained model (Joblib format)
- `💻 streamlit_app.py` – Streamlit web application code
- `📝 README.md` – Project documentation

---

## 📊 Model Performance

The model was trained and tested using **Random Forest Regressor** and achieved:

### 📊 Model Performance Summary

| Metric                  | Value               |
|-------------------------|---------------------|
| R² Score                | 0.91 (91%)          |
| Mean Absolute Error     | ~3.5 kcal           |
| Model Used              | Random Forest Regressor |

---

## 📚 Dataset Information

- **Source**: [Calories Burnt Dataset - Kaggle](https://www.kaggle.com/datasets/fmohajeri/calories-burnt)
- **Features Used**:
  - Gender
  - Age
  - Height
  - Weight
  - Duration
  - Heart Rate
  - Body Temperature
- **Target**:
  - Calories Burned

