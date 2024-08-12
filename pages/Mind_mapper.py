import streamlit as st
import requests
import google.generativeai as genai
import os
from keys import api_key 
from PyPDF2 import PdfReader
import graphviz

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
    return response.text

# Function to generate a mind map using Graphviz
def generate_mind_map(keywords):
    dot = graphviz.Digraph(comment='Mind Map')
    dot.node('Root', 'Main Keywords')
    for keyword in keywords:
        dot.node(keyword, keyword)
        dot.edge('Root', keyword)
    return dot

def main():
    st.title("PDF Text Extraction and Mind Map Generation")
    
    # File uploader for PDF
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file is not None:
        # Extract text from PDF
        text = extract_text_from_pdf(uploaded_file)
        st.write("### Extracted Text from PDF:")
        st.write(text)

        # Text input for prompt
        prompt = "Generate a keywords for this document text"

        if st.button("Generate Mind Map"):
            if prompt:
                # Combine text with user prompt
                combined_prompt = f"{text}\n{prompt}"

                # Perform keyword extraction using Gemini API
                keywords = generate_content(combined_prompt)
                if keywords:
                    st.write("### Extracted Keywords:")
                    st.write(keywords)
                    
                    # Generate mind map using extracted keywords
                    keyword_list = keywords.split()
                    mind_map = generate_mind_map(keyword_list)
                    
                    st.graphviz_chart(mind_map.source)
            else:
                st.write("Please enter a prompt for keyword extraction.")

if __name__ == "__main__":
    main()
    