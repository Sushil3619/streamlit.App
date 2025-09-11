import streamlit as st
import pandas as pd
import numpy as np

st.title("Employee Skills Gap Prediction Model")

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

