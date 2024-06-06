import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

# Streamlit app
st.title("Resume Maker")

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

# Generate and Download Resume as PDF
if st.button("Generate PDF Resume"):
    # Create a PDF document
    pdf_buffer = BytesIO()
    doc = SimpleDocTemplate(pdf_buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    # Add content to the PDF
    elements.append(Paragraph(f"<b>Name:</b> {name}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Email:</b> {email}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Phone:</b> {phone}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Education:</b>", styles["Normal"]))
    elements.append(Paragraph(f"{degree} in {school}, Graduation Year: {graduation_year}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Work Experience:</b>", styles["Normal"]))
    elements.append(Paragraph(f"{job_title} at {company}, Duration: {work_duration}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Skills:</b> {skills}", styles["Normal"]))

    # Build the PDF
    doc.build(elements)

    # Provide a download link for the PDF
    st.success("PDF Resume generated successfully.")
    st.download_button("Download PDF Resume", pdf_buffer.getvalue(), file_name="resume.pdf", key="download-pdf")

