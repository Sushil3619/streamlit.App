import streamlit as st
import pandas as pd
import numpy as np

st.title("Employee Skills Gap Prediction Model")


st.title("Employee Information Form")

# Form for multiple questions about an employee
with st.form("employee_form"):
    name = st.text_input("Employee Name")
    age = st.number_input("Age", min_value=18, max_value=70, value=30)
    department = st.selectbox("Department", ["HR", "Sales", "IT", "Finance", "Marketing"])
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)
    performance_rating = st.slider("Performance Rating (1-5)", 1, 5, 3)
    skills = st.text_area("Key Skills (comma separated)")

    submitted = st.form_submit_button("Submit")

if submitted:
    st.write("### Employee Details Entered:")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Department: {department}")
    st.write(f"Experience: {experience} years")
    st.write(f"Performance Rating: {performance_rating}")
    st.write(f"Skills: {skills}")
else:
    st.write("Please fill out the form and submit.")


# Collect inputs
st.header("Employee Details Input")

resume_skill = st.slider("Resume Skill Level (0=none to 10=expert)", 0, 10, 5)
work_performance = st.slider("Work Performance (1=low to 5=high)", 1, 5, 3)
experience_years = st.number_input("Years of Experience", 0, 50, 5)

# Skill gap calculation (mock logic)
skill_gap = max(0, 10 - resume_skill - (experience_years * 0.15) + (5 - work_performance))

st.subheader(f"Predicted Skills Gap Score: {skill_gap:.2f} (0=no gap, 10=max gap)")

# Prepare data for visualization table
data = {
    "Metric": ["Resume Skill", "Work Performance", "Experience (years)", "Skills Gap"],
    "Value": [resume_skill, work_performance, experience_years, skill_gap]
}
df = pd.DataFrame(data)

st.write("### Skill Metrics Table")
st.dataframe(df.style.highlight_max(axis=0))

# Simple bar chart for visualization using Streamlit's built-in chart support
st.write("### Skill Gap Visualization")
st.bar_chart(data=df.set_index("Metric"))

import streamlit as st
import pandas as pd

st.title("CSV फाइल अपलोड करा आणि डाटा पहा")

# CSV फाइल अपलोड करण्यासाठी फाइल अपलोडर विजेट
uploaded_file = st.file_uploader("CSV फाइल निवडा", type=["csv"])

if uploaded_file is not None:
    # अपलोड केलेल्या फाइलचे पांडस DataFrame मध्ये वाचन करा
    df = pd.read_csv(uploaded_file)
    
    # डेटा डिस्प्ले करा
    st.write("अपलोड केलेला डेटा खाली दिसणार आहे:")
    st.dataframe(df)
else:
    st.write("कृपया CSV फाइल अपलोड करा.")
