import streamlit as st
import google.genai as genai
import os

# Load API Key (replace with your actual key or set it in env variables)
api_key = "GEMINI_API_KEY"  

# Initialize Gemini Client
client = genai.Client(api_key=api_key)

st.title("🤖 Gemini Chatbot ")

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate response
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=user_input
    )

    bot_reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])
