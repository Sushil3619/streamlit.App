import streamlit as st
import pickle
import numpy as np

# Load the trained model (assumes you have a model saved as 'loan_model.pkl')
with open('loan_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def preprocess_input(gender, married, dependents, education, self_employed, 
                     applicant_income, coapplicant_income, loan_amount, 
                     loan_amount_term, credit_history, property_area):
    # Encoding the categorical inputs as numbers expected by the model
    gender_encoded = 1 if gender == 'Male' else 0
    married_encoded = 1 if married == 'Yes' else 0
    dependents_encoded = 0 if dependents == 'None' else int(dependents[0])  # '1', '2', '3+'
    education_encoded = 1 if education == 'Graduate' else 0
    self_employed_encoded = 1 if self_employed == 'Yes' else 0
    property_area_encoded = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}[property_area]

    # Some features scaled/normalized like loan amount in thousands
    loan_amount_scaled = loan_amount / 1000 if loan_amount > 0 else 0
    loan_amount_term_scaled = loan_amount_term / 12 if loan_amount_term > 0 else 0  # in years

    features = np.array([[gender_encoded, married_encoded, dependents_encoded, education_encoded,
                          self_employed_encoded, applicant_income, coapplicant_income,
                          loan_amount_scaled, loan_amount_term_scaled, credit_history,
                          property_area_encoded]])
    return features

def main():
    st.title("Loan Approval Prediction")

    st.subheader("Fill in the details below to predict loan approval status:")

    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["None", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    applicant_income = st.number_input("Applicant Income (in INR)", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income (in INR)", min_value=0)
    loan_amount = st.number_input("Loan Amount (in INR)", min_value=0)
    loan_amount_term = st.number_input("Loan Amount Term (in months)", min_value=0)
    credit_history = st.selectbox("Credit History (1 = meets guidelines, 0 = does not)", [1, 0])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    if st.button("Predict Loan Approval"):
        input_data = preprocess_input(gender, married, dependents, education, self_employed,
                                      applicant_income, coapplicant_income, loan_amount,
                                      loan_amount_term, credit_history, property_area)
        prediction = model.predict(input_data)
        prediction_prob = model.predict_proba(input_data)[0][1]

        if prediction[0] == 1:
            st.success(f"Loan Approved with probability {prediction_prob:.2f}")
        else:
            st.error(f"Loan Rejected with probability {1-prediction_prob:.2f}")

if __name__ == '__main__':
    main()
