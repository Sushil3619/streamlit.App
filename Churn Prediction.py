import streamlit as st
import numpy as np
import pandas as pd
import pickle
#import sklearn


from sklearn.preprocessing import StandardScaler,LabelEncoder
label_encoder= LabelEncoder ()

scaler= StandardScaler ()

st.title("Customer Churn Prediction")

gender=st.selectbox('select Gender:',option= ['Male', 'Female'])
sen=st.selectbox('select Senior Citizen:', option= ['Yes', 'No'])
Partner =st.selectbox('Do you have partener?', option=['Yes','No'] )
Dependents = st.selectbox('Do you have dependents?', option=['Yes','No'] )
tenure = st.text_input('Enter tenure (in months):', value=1)
Phoneservice=st.selectbox('Do you have phone service?', option=['Yes','No'])
multiline = st.selectbox('Select Multiple Lines:', option=['Yes','No'])
contact=st.selectbox('Select Contract Type:', option=['Month-to-month', 'One year', 'Two year'])
totalcharge = st.text_input('Enter Total Charge:', value=29.85)



model=pickle.load(open('churn_model.pkl','rb'))

result = model.predict([[gender,sen,Partner,Dependents,tenure,Phoneservice,multiline,contact,totalcharge]])

if st.button('Predict'):
    st.success('The churn prediction is {}'.format(result))


    if result[0]==1:
        st.warning('The customer is likely to churn')
        st.balloons()
    else:
        st.write('The customer is not to churn')

