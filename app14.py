import streamlit as st

# Streamlit app
st.title("Simple Resume Maker")

# Basic Information
st.header("Basic Information")

# Input fields for basic information
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

# Education
st.header("Education")

# Input fields for education
school = st.text_input("School/University")
degree = st.text_input("Degree")
graduation_year = st.text_input("Graduation Year")

# Work Experience
st.header("Work Experience")

# Input fields for work experience
job_title = st.text_input("Job Title")
company = st.text_input("Company")
work_duration = st.text_input("Work Duration")

# Skills
st.header("Skills")

# Input field for skills
skills = st.text_area("Skills (comma-separated)")

# Generate Resume
if st.button("Generate Resume"):
    # Create a simple resume
    resume = f"**Name:** {name}\n\n" \
             f"**Email:** {email}\n\n" \
             f"**Phone:** {phone}\n\n" \
             f"**Education:**\n{degree} in {school}, Graduation Year: {graduation_year}\n\n" \
             f"**Work Experience:**\n{job_title} at {company}, Duration: {work_duration}\n\n" \
             f"**Skills:** {skills}"
    
    # Display the resume
    st.markdown(resume)

