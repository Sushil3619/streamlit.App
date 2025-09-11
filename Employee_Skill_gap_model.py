import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Employee Skills Gap Prediction Model")

# Input employee info
st.header("Employee Information")
resume_skill_level = st.slider(
    "Resume Skill Level (0=none to 10=expert)", 0, 10, 5)
work_performance = st.slider(
    "Work Performance (Rating 1=low to 5=high)", 1, 5, 3)
experience_years = st.number_input(
    "Years of Experience", min_value=0, max_value=50, value=5)

# Define predicted skill gap based on inputs (mock logic)
# Skill gap higher if resume skill low and less experience but work performance high
skill_gap_score = max(0, 10 - resume_skill_level - (experience_years * 0.2) + (5 - work_performance))

st.subheader(f"Predicted Skill Gap Score: {skill_gap_score:.2f} (0 = no gap, 10 = max gap)")

# Visualize skill gap and features
data = {
    "Resume Skill Level": resume_skill_level,
    "Work Performance": work_performance,
    "Experience (years)": experience_years,
    "Skill Gap": skill_gap_score
}
df = pd.DataFrame(list(data.items()), columns=["Metric", "Value"])

sns.barplot(df["Metric"], df["Value"], color=['skyblue'])
plt.show()



fig, ax = plt.subplots()
bars = ax.bar(df["Metric"], df["Value"], color=['skyblue', 'lightgreen', 'orange', 'red'])
ax.set_ylim(0, 12)
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.3, round(yval, 2), ha='center', va='bottom')
st.pyplot(fig)
