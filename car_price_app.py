import streamlit as st
import pandas as pd
import pickle

# Load the trained pipeline (Random Forest with preprocessing inside)
with open('CarProject.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit App Title
st.title("🚗 Car Price Prediction App")

st.write(
    """
    This app predicts the **estimated price** of a used car.
    
    Fill out the details below:
    """
)

# Input fields for user
company = st.text_input("Enter Company Name")
name = st.text_input("Enter Car Model Name")
year = st.number_input("Enter Year of Purchase", min_value=1990, max_value=2025, step=1)
kms_driven = st.number_input("Enter Kilometers Driven", min_value=0, step=500)
fuel_type = st.selectbox("Select Fuel Type", ["Petrol", "Diesel", "LPG"])

# Prediction Button
if st.button("Predict Price"):
    # Create input DataFrame with correct column order
    input_data = pd.DataFrame(
        [[company, name, year, kms_driven, fuel_type]],
        columns=["company", "name", "year", "kms_driven", "fuel_type"]
    )

    # Predict using the loaded model
    predicted_price = model.predict(input_data)[0]

    # Show result
    st.success(f"Estimated Car Price: ₹ {int(predicted_price):,}")