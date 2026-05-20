import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit app
st.title("AI Python Tutor")

st.sidebar.title("Tutor Modules")
st.sidebar.write("""
- Concept Explainer
- Code Example Generator
- Error Debugger
- Exercise Creator
- Feedback Provider
""")

st.write("Welcome to your beginner-friendly AI tutor!")

# Tutoring modes
mode = st.selectbox(
    "Choose a tutoring mode:",
    [
        "Concept Explainer",
        "Code Example Generator",
        "Error Debugger",
        "Exercise Creator",
        "Feedback Provider"
    ]
)

# User input
user_input = st.text_area("Enter your question or code:")

# Generate response
if st.button("Get Tutor Response"):

    if user_input.strip() == "":
        st.warning("Please enter a question or code before submitting.")

    else:
        prompt = f"""
        You are a beginner-friendly Python tutor.

        Tutoring Mode:
        {mode}

        User Request:
        {user_input}

        Respond in this format:

        1. Concept Explanation
        2. Code Example
        3. Practice Exercise
        4. Feedback
        """

        try:
            with st.spinner("Generating tutor response..."):
                response = model.generate_content(prompt)

                st.subheader("Tutor Response")
                st.write(response.text)

                st.success("Response generated successfully!")

        except Exception as e:
            st.error(f"An error occurred: {e}")