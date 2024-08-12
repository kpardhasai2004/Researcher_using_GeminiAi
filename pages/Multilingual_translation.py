import streamlit as st
import requests
import google.generativeai as genai
from keys import api_key

# Configure Gemini API and model
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# Function to perform translation using Gemini API
def translate_text(text, target_language):
    # Prepare the prompt for translation
    prompt = f"Translate the following text to {target_language}: {text}"
    
    # Generate translation using the Gemini API
    response = model.generate_content(prompt)
    
    # Extract translated text from the response
    if response:
        translated_text = response.text
        return translated_text
    else:
        return "Translation failed. Please try again."

# Streamlit UI for multilingual translation
def main():
    st.title("Bridging Languages, Unveiling Translations")
    
    # Text input for the text to be translated
    text_to_translate = st.text_area("Enter text to translate:", "")
    
    # Selectbox for target language selection
    target_language = st.selectbox(
        "Select target language:",
        ["","Arabic", "Bengali", "Bulgarian", "Chinese", "Croatian", "Czech", "Danish", "Dutch", "English",
         "Estonian", "Finnish", "French", "German", "Greek", "Hebrew", "Hindi", "Hungarian", "Indonesian", 
         "Italian", "Japanese", "Korean", "Latvian", "Lithuanian", "Norwegian", "Polish", "Portuguese", 
         "Romanian", "Russian", "Serbian", "Slovak", "Slovenian", "Spanish", "Swahili", "Swedish", 
         "Thai", "Turkish", "Ukrainian", "Vietnamese"]
    )
    
    # Button to perform translation
    if st.button("Translate"):
        if text_to_translate:
            # Perform translation
            translated_text = translate_text(text_to_translate, target_language)
            
            # Display translated text
            st.write("### Translated Text:")
            st.write(translated_text)
        else:
            st.error("Please enter text to translate.")

if __name__ == "__main__":
    main()
