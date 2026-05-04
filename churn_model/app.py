import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Churn Prediction App", layout="centered")

st.title("Customer Churn Prediction")

model = joblib.load("churn_model/model.pkl")

st.markdown("### Customer Information:")

age = st.number_input("Age", 18, 100, 30)
tenure = st.number_input("Tenure", 0, 100, 5)
usage = st.number_input("Usage Frequency", 0, 100, 10)
support_calls = st.number_input("Support Calls", 0, 100, 2)
payment_delay = st.number_input("Payment Delay", 0, 100, 1)
total_spend = st.number_input("Total Spend", 0.0, 100000.0, 1000.0)
last_interaction = st.number_input("Last Interaction", 0, 365, 10)

gender = st.selectbox("Gender", ["Male", "Female"])
subscription = st.selectbox("Subscription Type", ["Basic", "Standard", "Premium"])
contract = st.selectbox("Contract Length", ["Monthly", "Quarterly", "Yearly"])


input_df = pd.DataFrame([{
    "Age": age,
    "Tenure": tenure,
    "Usage Frequency": usage,
    "Support Calls": support_calls,
    "Payment Delay": payment_delay,
    "Total Spend": total_spend,
    "Last Interaction": last_interaction,
    "Gender": gender,
    "Subscription Type": subscription,
    "Contract Length": contract
}])

if st.button("Predict"):
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.subheader("Result")
    st.write("Churn Prediction:", "Yes" if pred == 1 else "No")
    st.write("Probability:", float(prob))
