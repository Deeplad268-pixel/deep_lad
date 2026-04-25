import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")

age = st.number_input("Age")
balance = st.number_input("Balance")
frequent = st.number_input("frequent flyer")
services = st.number_input("services opted")
acc = st.number_input("account linked to social media")
book = st.number_input("Booked hotel")
target = st.number_input("target")

if st.button("Predict"):
    input_data = np.array([[age, balance,frequent,acc,book,target]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.write("Customer will churn")
    else:
        st.write("Customer will stay")