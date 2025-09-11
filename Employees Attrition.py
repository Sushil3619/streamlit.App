import streamlit as st

st.title("Employees Attrition Prediction Model")

st.write("Enter employee details to predict if they are likely to leave:")

# Input fields for employee features (example)
age = st.number_input("Age", min_value=18, max_value=65, value=30)
job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000)
years_at_company = st.number_input("Years at Company", min_value=0, max_value=40, value=5)
distance_from_home = st.number_input("Distance From Home (km)", min_value=0, max_value=100, value=10)

if st.button("Predict Attrition"):
    # Placeholder model logic (replace with actual model prediction)
    score = (age * 0.02) + (job_satisfaction * -0.3) + (monthly_income * -0.0001) + (years_at_company * -0.1) + (distance_from_home * 0.05)
    attrition_risk = "High" if score > 0.5 else "Low"
    
    st.write(f"Predicted Attrition Risk: **{attrition_risk}**")
