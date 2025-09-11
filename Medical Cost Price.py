import streamlit as st
import pandas as pd
import numpy as np

st.title("Medical Cost Price Prediction Model")

# Input fields for person details
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["Southwest", "Southeast", "Northwest", "Northeast"])

# Mock prediction function simulating a trained ML model
def predict_medical_cost(age, sex, bmi, children, smoker, region):
    base_cost = 2000
    cost = base_cost
    cost += (age * 50)
    cost += (bmi * 30)
    cost += (children * 500)
    if smoker == "Yes":
        cost += 10000
    if sex == "Male":
        cost += 500
    region_factor = {
        "Southwest": 100,
        "Southeast": 200,
        "Northwest": 300,
        "Northeast": 400
    }
    cost += region_factor.get(region, 0)
    return round(cost, 2)

if st.button("Predict Medical Cost"):
    predicted_cost = predict_medical_cost(age, sex, bmi, children, smoker, region)
    st.subheader(f"Predicted Medical Cost: ${predicted_cost}")

    # Visualization of input factors vs cost contribution
    factors = {
        "Age": age * 50,
        "BMI": bmi * 30,
        "Children": children * 500,
        "Smoker Cost": 10000 if smoker == "Yes" else 0,
        "Sex Cost": 500 if sex == "Male" else 0,
        "Region Cost": {
            "Southwest": 100,
            "Southeast": 200,
            "Northwest": 300,
            "Northeast": 400
        }.get(region, 0)
    }
    df = pd.DataFrame(list(factors.items()), columns=["Factor", "Cost Contribution"])
    st.bar_chart(df.set_index("Factor"))
else:
    st.info("Fill all fields and click 'Predict Medical Cost'")

