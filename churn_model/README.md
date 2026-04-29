# Customer Churn Prediction App

A machine learning project that predicts whether a customer will churn based on behavioral and subscription data.  
The model is deployed using a Streamlit web application for real-time predictions.

---

## 🚀 Project Overview

Customer churn prediction helps businesses identify customers who are likely to stop using a service.  
This project builds a supervised learning pipeline to classify customers into:

- **0 → Not Churn**
- **1 → Churn**

The final model is deployed as an interactive web app using Streamlit.

---

## 🧠 Machine Learning Pipeline

The project uses a full preprocessing + classification pipeline:

### Preprocessing:
- Numerical features → StandardScaler
- Categorical features → OneHotEncoder

### Models tested:
- Logistic Regression
- Random Forest
- XGBoost
- SVM

### Final model:
- XGBoost Classifier

---

## 📊 Features Used

### Numerical:
- Age  
- Tenure  
- Usage Frequency  
- Support Calls  
- Payment Delay  
- Total Spend  
- Last Interaction  

### Categorical:
- Gender  
- Subscription Type  
- Contract Length  

---

## ⚙️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- XGBoost  
- Streamlit  
- Joblib  

---

## 🖥️ Streamlit App Features

- Manual customer input form  
- Real-time churn prediction  
- Probability score output  
- Pre-trained model loading (`churn_model.pkl`)  
- Fast inference (no retraining in app)