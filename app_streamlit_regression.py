import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model

# Loading trained model, scalar pickle, encoders pickle
model = load_model("regression_model.h5")

with open("label_encoder_geography.pkl", "rb") as file:
    label_encoder_geography = pickle.load(file)

with open("label_encoder_gender.pkl", "rb") as file:
    label_encoder_gender = pickle.load(file)

with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

# Streamlit application
st.title("Estimated Salary Prediction")

# User input
geography = st.selectbox("Geography", label_encoder_geography.categories_[0])
gender = st.selectbox("Gender", label_encoder_gender.classes_)
age = st.slider("Age", 18, 90)
balance = st.number_input("Balance")
credit_score = st.number_input("Credit Score")
exited = st.selectbox("Exited", [0, 1])
tenure = st.slider("Tenure", 0, 10)
num_of_products = st.slider("Number of Products", 1, 4)
has_cr_card = st.selectbox("Has Credit Card", [0, 1])
is_active_member = st.selectbox("Is Active Member", [0, 1])

# Preparing the input
input_data = pd.DataFrame(
    {
        "CreditScore": [credit_score],
        "Gender": [label_encoder_gender.transform([gender])[0]],
        "Age": [age],
        "Tenure": [tenure],
        "Balance": [balance],
        "NumOfProducts": [num_of_products],
        "HasCrCard": [has_cr_card],
        "IsActiveMember": [is_active_member],
        "Exited": [exited],
    }
)

# Separately prepared Geography input
geography_encoded = label_encoder_geography.transform([[geography]]).toarray()

df_geography_encoded = pd.DataFrame(
    geography_encoded,
    columns=label_encoder_geography.get_feature_names_out(["Geography"]),
)

# Addig the Grography input to the input data
input_data = pd.concat(
    [input_data.reset_index(drop=True), df_geography_encoded], axis=1
)

# Scaling the input
scaled_input = scaler.transform(input_data)

# Predicting the salary
prediction = model.predict(scaled_input)
predicted_salary = prediction[0][0]

# Printing the result
st.write(f"Predicted Estimated Salary: ${predicted_salary:.2f}")
