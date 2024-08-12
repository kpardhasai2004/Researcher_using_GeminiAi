import streamlit as st
import google.generativeai as genai
from keys import api_key

# Configure the Generative AI model
genai.configure(api_key=api_key)

# Function to generate brainstorming ideas
def generate_brainstorming_ideas(keywords, prompt):
    # Prepare the prompt for generating brainstorming ideas
    full_prompt = f"{prompt} based on the following keywords: {keywords}"
    
    # Generate content using the Gemini model
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(full_prompt)
    
    return response

# Streamlit UI for the brainstorming page
def main():
    st.title("Start Your Brainstorming Here")
    
    # Define multiple text inputs
    keywords = st.text_input("Enter your research keywords:", "")
    prompt = st.text_input("Enter your prompt (optional):", "Generate creative research ideas")
    
    if st.button("Generate Ideas"):
        if keywords:
            ideas = generate_brainstorming_ideas(keywords, prompt)
            st.write("### Generated Research Ideas:")
            st.write(ideas.text)
        else:
            st.write("Please enter some keywords to generate ideas.")

if __name__ == "__main__":
    main()
