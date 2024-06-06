from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import streamlit as st

# Streamlit app
st.title("Text to PDF Converter")

# User input
text_input = st.text_area("Enter your text:")

# Convert text to PDF
if st.button("Convert to PDF"):
    if text_input:
        pdf_filename = "output.pdf"
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        c.setFont("Helvetica", 12)
        
        # Split text into lines and add to PDF
        lines = text_input.split("\n")
        for line in lines:
            c.drawString(50, 750, line)
            c.showPage()
        
        c.save()
        
        st.success(f"PDF created: [{pdf_filename}]")
        with open(pdf_filename, "rb") as pdf_file:
            st.download_button(
                label="Download PDF",
                data=pdf_file.read(),
                key="download-pdf",
                file_name=pdf_filename,
            )
    else:
        st.warning("Please enter some text to convert to PDF.")
