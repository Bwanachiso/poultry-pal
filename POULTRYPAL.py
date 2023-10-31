import streamlit as st
import requests

st.title("PoultryPal Chatbot")

session_id = "unique_session_id"  # Use a unique session ID for each user

user_message = st.text_input("You:", "")

if st.button("Send"):
    if user_message:
        response = requests.post(f"http://your-flask-api-url/api/chat/{session_id}", json={"message": user_message})
        bot_reply = response.json()["message"]
        st.write(f"Bot: {bot_reply}")

