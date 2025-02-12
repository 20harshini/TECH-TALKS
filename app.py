import streamlit as st
import google.generativeai as genai
import pandas as pd

# Set up API key
API_KEY = "AIzaSyB69jPo_cUCWCiDj4FWa8kanZQyj6m-yP8"
genai.configure(api_key=API_KEY)

# Function to generate blog content
def generate_blog(topic):
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Write a blog post about {topic} and its impact on social media."
    
    response = model.generate_content(prompt)
    return response.text if response else "No response from AI."

# Streamlit UI
st.title("📄 Blog Generator using Gemini AI")
st.write("Enter a topic to generate a blog post.")

# User input
topic = st.text_input("Enter a topic:", placeholder="e.g., Social Media Marketing Trends")

if st.button("Generate Blog"):
    if topic:
        blog_content = generate_blog(topic)
        
        # Display blog content in a table format
        df = pd.DataFrame([[topic, blog_content]], columns=["Topic", "Generated Blog"])
        st.table(df)
    else:
        st.warning("Please enter a topic.")