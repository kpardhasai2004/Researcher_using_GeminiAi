import streamlit as st
import requests
from PyPDF2 import PdfReader
import google.generativeai as genai
from keys import api_key

# Configure Gemini API and model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Function to extract text from PDF using PyPDF2
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to generate content using Gemini API
def generate_content(prompt):
    response = model.generate_content(prompt)
    return response

# Streamlit UI for PDF text extraction and Gemini API usage
def main():
    st.title("Go beyond the Pages of your Doc")
    st.header("Upload a PDF File and Enter Prompt")

    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    # Text input for prompt
    prompt = st.text_area("Enter your prompt for content generation:", "")

    if uploaded_file is not None:
        # Display uploaded PDF filename and size
        st.write(f"Uploaded PDF: {uploaded_file.name} ({uploaded_file.size} bytes)")

        # Button to extract text and enter prompt
        if st.button("Extract Text & Generate Content"):
            # Extract text from PDF
            pdf_text = extract_text_from_pdf(uploaded_file)

            # Display extracted text (for debugging purposes)
            # st.write("### Extracted Text from PDF:")
            # st.write(pdf_text)

            if prompt:
                # Generate content using Gemini API
                st.write("### Generated Content:")
                generated_content = generate_content(f" '{pdf_text}' \n{prompt}")
                st.write(generated_content.text)
            else:
                st.write("Please enter a prompt for content generation.")

if __name__ == "__main__":
    main()
