import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")

# Example inputs (change based on your dataset)
age = st.number_input("Age")
balance = st.number_input("Balance")

if st.button("Predict"):
    prediction = model.predict([[age, balance]])
    
    if prediction == 1:
        st.write("Customer will churn")
    else:
        st.write("Customer will stay")