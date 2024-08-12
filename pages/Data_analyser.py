import streamlit as st
import pandas as pd
import requests
import google.generativeai as genai
from keys import api_key  # Assuming you have a separate file for API keys

# Configure Gemini API and model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Function to generate content using Gemini API
def generate_content(prompt):
    response = model.generate_content(prompt)
    if response and 'text' in response:
        return response['text']
    return "Failed to generate content."

# Function to perform data analysis using Gemini API
def perform_data_analysis(data, query):
    # Combine data with user query
    prompt = f"{data}\n{query}"
    response = generate_content(prompt)
    return response

# Streamlit UI for data analytics
def main():
    st.title("Let's unveil the hidden story of Data")
    st.header("Upload File and Perform Analysis")
    
    # File uploader
    uploaded_file = st.file_uploader("Upload a dataset file (CSV, XLSX)", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read file contents using pandas
        if uploaded_file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or uploaded_file.type == 'application/vnd.ms-excel':
            df = pd.read_excel(uploaded_file)
        else:
            df = pd.read_csv(uploaded_file)
        
        st.write("### Sample Data from Uploaded File:")
        st.write(df)

        # Text input for query
        query = st.text_area("Enter your query for analysis:", "")

        if st.button("Run Analysis"):
            if query:
                # Selecting a sample row for demonstration (you can modify as per your requirement)
                sample_data = df.head(5).to_dict()  # Converting top 5 rows to a dictionary for simplicity
                data = f"Sample Data: {sample_data}"

                # Perform analysis using Gemini API
                analysis_result = perform_data_analysis(data, query)
                if analysis_result:
                    st.write("### Analysis Result:")
                    st.write(analysis_result)
            else:
                st.write("Please enter a query for analysis.")

if __name__ == "__main__":
    main()
