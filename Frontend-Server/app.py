import streamlit as st
import requests

# Backend server URL 
BACKEND_URL = "http://127.0.0.1:3000/analyze-sentiment"


def get_chat_response(user_input):
    """Send user input to the backend and get the chatbot's response."""
    response = requests.post(BACKEND_URL, json={'text': user_input})
    if response.status_code == 200:
        return response.json().get('sentiment', "Sorry, I couldn't process that.")
    else:
        return "Error: Failed to get a response from the server."


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.title("Seintiment Analysis")


for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_input = st.chat_input("Type your message here...")


if user_input:
    
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    
    with st.chat_message("user"):
        st.write(user_input)

    
    chatbot_response = get_chat_response(user_input)

    st.session_state.chat_history.append({"role": "assistant", "content": "The sentiment of the text is: "+chatbot_response})

    
    with st.chat_message("assistant"):
        st.write("The sentiment of the text is: "+chatbot_response)