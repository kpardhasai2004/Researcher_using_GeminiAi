import streamlit as st
import pandas as pd
import google.generativeai as genai
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from keys import api_key

# Configure Gemini API
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Function to generate insights using Gemini API
def generate_insights(data, prompt):
    combined_prompt = f"{prompt}\n\nData: {data.head(5).to_string()}\n\nGenerate insights based on the above data."
    response = model.generate_content(combined_prompt)
    if response:
        return response
    else:
        return "Failed to generate insights. Please try again."

# Streamlit UI for data visualization
def main():
    st.title("Visualize data from your Dataset")
    
    # Upload CSV or Excel file
    uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        # Check the file extension and read the file accordingly
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            df = pd.read_excel(uploaded_file)

        # Display uploaded data and visualization side by side
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.write("### Uploaded Data:")
            st.write(df)

        # Data visualization options
        with col2:
            st.write("### Visualization Options")
            vis_option = st.selectbox("Choose a visualization type:", ["Histogram", "Scatter Plot", "Line Plot", "Bar Chart"])

            # Based on selected visualization type, display corresponding column selection
            if vis_option == "Histogram":
                column = st.selectbox("Select column for histogram:", df.columns)
                if st.button("Generate Histogram"):
                    plt.figure(figsize=(10, 6))
                    sns.histplot(df[column], kde=True)
                    st.pyplot(plt)

            elif vis_option == "Scatter Plot":
                x_column = st.selectbox("Select X column for scatter plot:", df.columns)
                y_column = st.selectbox("Select Y column for scatter plot:", df.columns)
                if st.button("Generate Scatter Plot"):
                    fig = px.scatter(df, x=x_column, y=y_column)
                    st.plotly_chart(fig)

            elif vis_option == "Line Plot":
                x_column = st.selectbox("Select X column for line plot:", df.columns)
                y_column = st.selectbox("Select Y column for line plot:", df.columns)
                if st.button("Generate Line Plot"):
                    fig = px.line(df, x=x_column, y=y_column)
                    st.plotly_chart(fig)

            elif vis_option == "Bar Chart":
                column = st.selectbox("Select column for bar chart:", df.columns)
                if st.button("Generate Bar Chart"):
                    fig = px.bar(df, x=df.index, y=column)
                    st.plotly_chart(fig)

if __name__ == "__main__":
    main()
