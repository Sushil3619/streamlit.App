import streamlit as st
import numpy as np
import pickle

# Load pretrained loan approval model (save your model as loan_model.pkl in working directory)
with open('loan_model.pkl', 'rb') as file:
    model = pickle.load(file)

def preprocess_input(gender, married, dependents, education, self_employed, 
                     applicant_income, coapplicant_income, loan_amount, 
                     loan_amount_term, credit_history, property_area):
    gender_encoded = 1 if gender == 'Male' else 0
    married_encoded = 1 if married == 'Yes' else 0
    dependents_encoded = 0 if dependents == 'None' else (3 if dependents == '3+' else int(dependents))
    education_encoded = 1 if education == 'Graduate' else 0
    self_employed_encoded = 1 if self_employed == 'Yes' else 0
    property_area_encoded = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}[property_area]
    loan_amount_scaled = loan_amount / 1000 if loan_amount else 0
    loan_amount_term_scaled = loan_amount_term / 12 if loan_amount_term else 0

    features = np.array([[gender_encoded, married_encoded, dependents_encoded, education_encoded,
                          self_employed_encoded, applicant_income, coapplicant_income,
                          loan_amount_scaled, loan_amount_term_scaled, credit_history,
                          property_area_encoded]])
    return features

def main():
    st.title("Loan Approval Prediction")

    st.subheader("Enter Applicant Details")

    gender = st.selectbox("Gender", options=["Male", "Female"])
    married = st.selectbox("Married", options=["Yes", "No"])
    dependents = st.selectbox("Dependents", options=["None", "1", "2", "3+"])
    education = st.selectbox("Education", options=["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", options=["Yes", "No"])
    applicant_income = st.number_input("Applicant Income (₹)", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income (₹)", min_value=0)
    loan_amount = st.number_input("Loan Amount (₹)", min_value=0)
    loan_amount_term = st.number_input("Loan Amount Term (Months)", min_value=0)
    credit_history = st.selectbox("Credit History", options=[1, 0])
    property_area = st.selectbox("Property Area", options=["Urban", "Semiurban", "Rural"])

    if st.button("Predict Loan Approval"):
        inputs = preprocess_input(gender, married, dependents, education, self_employed,
                                  applicant_income, coapplicant_income, loan_amount,
                                  loan_amount_term, credit_history, property_area)
        prediction = model.predict(inputs)
        prediction_prob = model.predict_proba(inputs)[0][1]

        if prediction[0] == 1:
            st.success(f"Loan Approved with confidence {prediction_prob:.2f}")
        else:
            st.error(f"Loan Rejected with confidence {1 - prediction_prob:.2f}")

if __name__ == "__main__":
    main()
