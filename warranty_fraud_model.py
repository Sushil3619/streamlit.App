import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained model (assumes model saved as 'warranty_fraud_model.pkl')
with open('warranty_fraud_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def preprocess_input(claim_amount, claim_reason, product_age, customer_history, 
                     claim_time, product_category, previous_claims):

    # Convert categorical features to numeric encoding as required by model
    claim_reason_encoded = {'Accidental': 0, 'Mechanical Failure': 1, 'Electrical Failure': 2, 'Other': 3}.get(claim_reason, 3)
    product_category_encoded = {'Electronics': 0, 'Furniture': 1, 'Appliance': 2, 'Other': 3}.get(product_category, 3)
    customer_history_encoded = 1 if customer_history == 'Good' else 0
    claim_time_encoded = 1 if claim_time == 'Working Hours' else 0

    features = np.array([[claim_amount, claim_reason_encoded, product_age, customer_history_encoded,
                          claim_time_encoded, product_category_encoded, previous_claims]])
    return features

def main():
    st.title("Warranty Claims Fraud Prediction")

    st.write("Please input the claim details for fraud prediction:")

    claim_amount = st.number_input("Claim Amount (INR)", min_value=0.0)
    claim_reason = st.selectbox("Claim Reason", ["Accidental", "Mechanical Failure", "Electrical Failure", "Other"])
    product_age = st.number_input("Product Age (in years)", min_value=0)
    customer_history = st.selectbox("Customer History", ["Good", "Bad"])
    claim_time = st.selectbox("Time of Claim", ["Working Hours", "Non-working Hours"])
    product_category = st.selectbox("Product Category", ["Electronics", "Furniture", "Appliance", "Other"])
    previous_claims = st.number_input("Number of Previous Claims", min_value=0)

    if st.button("Predict Fraud"):
        input_features = preprocess_input(claim_amount, claim_reason, product_age, customer_history,
                                          claim_time, product_category, previous_claims)
        prediction = model.predict(input_features)
        prediction_prob = model.predict_proba(input_features)[0][1]

        if prediction[0] == 1:
            st.error(f"Warning: This claim is likely fraudulent! (Probability: {prediction_prob:.2f})")
        else:
            st.success(f"This claim appears genuine. (Probability of fraud: {prediction_prob:.2f})")

if __name__ == '__main__':
    main()
