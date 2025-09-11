import streamlit as st
import pandas as pd

st.title("Medical Cost Price Prediction Model")

# Input person details
age = st.number_input("Age", min_value=0, max_value=120, value=30, help="Age of the person in years")
sex = st.selectbox("Sex", ["Male", "Female"], help="Biological sex of the person")
bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=60.0, value=25.0, format="%.1f",
                      help="Body Mass Index, a measure of body fat")
children = st.number_input("Number of Children", min_value=0, max_value=20, value=0,
                           help="Number of dependents/children")
smoker = st.selectbox("Smoker", ["Yes", "No"], help="Smoking status")
region = st.selectbox("Residential Region", ["Southwest", "Southeast", "Northwest", "Northeast"],
                      help="Region of residence")

# Additional factors
pre_existing_conditions = st.multiselect(
    "Pre-existing Conditions / Chronic Diseases",
    options=["Diabetes", "Hypertension", "Heart Disease", "Asthma", "Cancer", "None"],
    default=["None"],
    help="Select any known chronic medical conditions"
)

lifestyle = st.multiselect(
    "Lifestyle and Habits",
    options=["Regular Exercise", "Balanced Diet", "Alcohol Consumption", "Sedentary Lifestyle", "None"],
    default=["None"],
    help="Select lifestyle factors relevant to the person"
)

previous_medical_costs = st.number_input("Previous Medical Costs (Rupees)", min_value=0, max_value=1000000, value=0,
                                         help="Total past recorded medical expenses")
insurance_coverage = st.selectbox(
    "Insurance Coverage Factor",
    options=["Basic Plan", "Standard Plan", "Premium Plan", "None"],
    help="Type of insurance coverage the person has"
)

def predict_medical_cost(age, sex, bmi, children, smoker, region,
                         pre_existing_conditions, lifestyle,
                         previous_medical_costs, insurance_coverage):

    cost = 2000
    cost += age * 50
    cost += bmi * 40
    cost += children * 600
    if smoker == "Yes":
        cost += 12000
    if sex == "Male":
        cost += 800

    region_factors = {
        "Southwest": 150,
        "Southeast": 250,
        "Northwest": 350,
        "Northeast": 450
    }
    cost += region_factors.get(region, 0)

    condition_factors = {
        "Diabetes": 5000,
        "Hypertension": 4000,
        "Heart Disease": 8000,
        "Asthma": 3500,
        "Cancer": 12000,
        "None": 0
    }
    for condition in pre_existing_conditions:
        cost += condition_factors.get(condition, 0)

    lifestyle_adjustments = {
        "Regular Exercise": -1000,
        "Balanced Diet": -800,
        "Alcohol Consumption": 1500,
        "Sedentary Lifestyle": 2000,
        "None": 0
    }
    for habit in lifestyle:
        cost += lifestyle_adjustments.get(habit, 0)

    cost += previous_medical_costs * 0.1

    coverage_factors = {
        "Basic Plan": 1000,
        "Standard Plan": 2500,
        "Premium Plan": 4000,
        "None": 0,
    }
    cost -= coverage_factors.get(insurance_coverage, 0)

    return round(cost, 2)

if st.button("Predict Medical Cost"):
    pred_cost = predict_medical_cost(age, sex, bmi, children, smoker, region,
                                     pre_existing_conditions, lifestyle,
                                     previous_medical_costs, insurance_coverage)
    st.subheader(f"Predicted Medical Cost:in One Years *Rs{pred_cost}")

    # Visualization data for cost contributors
    factors = {
        "Base Cost": 2000,
        "Age Factor": age * 50,
        "BMI Factor": bmi * 40,
        "Children Factor": children * 600,
        "Smoking Factor": 12000 if smoker == "Yes" else 0,
        "Sex Factor": 800 if sex == "Male" else 0,
        "Region Factor": {
            "Southwest": 150,
            "Southeast": 250,
            "Northwest": 350,
            "Northeast": 450
        }.get(region, 0),
        "Pre-existing Conditions":
            sum({
                "Diabetes": 5000,
                "Hypertension": 4000,
                "Heart Disease": 8000,
                "Asthma": 3500,
                "Cancer": 12000,
                "None": 0
            }.get(cond, 0) for cond in pre_existing_conditions),
        "Lifestyle Impact":
            sum({
                "Regular Exercise": -1000,
                "Balanced Diet": -800,
                "Alcohol Consumption": 1500,
                "Sedentary Lifestyle": 2000,
                "None": 0
            }.get(habit, 0) for habit in lifestyle),
        "Previous Medical Costs Adjustment": previous_medical_costs * 0.1,
        "Insurance Coverage Adjustment": -{
            "Basic Plan": 1000,
            "Standard Plan": 2500,
            "Premium Plan": 4000,
            "None": 0,
        }.get(insurance_coverage, 0)
    }

    df = pd.DataFrame(list(factors.items()), columns=["Factor", "Cost Impact"])
    st.bar_chart(df.set_index("Factor"))

else:
    st.info("Fill all the details above and click 'Predict Medical Cost'")

