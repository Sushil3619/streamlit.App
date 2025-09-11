import streamlit as st
import PyPDF2
import pandas as pd
import numpy as np

st.title("Employee Skills Gap Prediction from Resume and Info")

# Resume upload
uploaded_file = st.file_uploader("Upload your Resume (PDF or TXT)", type=["pdf", "txt"])

def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text

def analyze_resume_text(text):
    # Example skill keywords to look for
    skills = ["python", "machine learning", "data analysis", "excel", "communication", "leadership"]
    skill_count = sum(text.lower().count(skill) for skill in skills)
    # Skill gap score inversely related to number of skills found (mock logic)
    skill_gap_score = max(0, 10 - skill_count)
    return skill_gap_score

# Additional employee info form
st.header("Additional Employee Information")
with st.form("employee_info_form"):
    performance = st.slider("Work Performance (1 to 5)", min_value=1, max_value=5, value=3)
    experience = st.number_input("Years of Experience", min_value=0, max_value=50, value=5)
    submit_info = st.form_submit_button("Submit Employee Info")

if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        resume_text = extract_text_from_pdf(uploaded_file)
    else:
        resume_text = uploaded_file.read().decode("utf-8")
    
    st.subheader("Resume Text Snippet:")
    st.write(resume_text[:1000] + "...")
    
    skill_gap = analyze_resume_text(resume_text)
    
    if submit_info:
        # Modify skill gap based on additional info (example logic)
        skill_gap = max(0, skill_gap - (performance * 0.5) - (experience * 0.1))
        skill_gap = round(skill_gap, 2)
        
        st.subheader(f"Predicted Skills Gap Score: {skill_gap} (0 = no gap, 10 = max gap)")
        
        # Visualize metrics
        data = {
            "Metric": ["Resume Skill Gap", "Performance Adjustment", "Experience Adjustment", "Final Skill Gap"],
            "Value": [skill_gap + (performance * 0.5) + (experience * 0.1), performance * 0.5, experience * 0.1, skill_gap]
        }
        df = pd.DataFrame(data)
        st.bar_chart(df.set_index("Metric"))
    else:
        st.info("Please fill employee info and submit to compute final skill gap.")
else:
    st.info("Please upload a resume (PDF or TXT) to analyze.")


