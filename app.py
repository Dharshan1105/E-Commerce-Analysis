import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("profit_prediction_model.pkl")

# Page configuration
st.set_page_config(page_title="Profit Predictor", layout="centered")

# Title
st.title(" E-Commerce Profit Prediction")
st.write("Predict order profit using a Random Forest model")

st.divider()

# Sidebar Inputs
st.sidebar.header("Order Details")

sales = st.sidebar.slider("Sales", 0.0, 10000.0, 500.0)

quantity = st.sidebar.slider("Quantity", 1, 20, 2)

discount = st.sidebar.slider("Discount", 0.0, 1.0, 0.1)

shipping_cost = st.sidebar.slider("Shipping Cost", 0.0, 500.0, 50.0)

aging = st.sidebar.slider("Aging (days)", 0, 30, 5)

st.divider()

# Show selected values
st.subheader("Selected Inputs")

st.write(f"Sales: {sales}")
st.write(f"Quantity: {quantity}")
st.write(f"Discount: {discount}")
st.write(f"Shipping Cost: {shipping_cost}")
st.write(f"Aging: {aging}")

# Prediction button
if st.button("Predict Profit"):

    features = np.array([[sales, quantity, discount, shipping_cost, aging]])

    prediction = model.predict(features)

    st.success(f" Predicted Profit: ${prediction[0]:.2f}")