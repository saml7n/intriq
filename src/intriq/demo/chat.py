import random
import time
import streamlit as st

# Dummy function to simulate chatbot responses


def get_chatbot_response(query):
    dummy_responses = {
        "current sales status": "Sales are currently 15% above the forecast for this quarter.",
        "operational efficiency": "Operational efficiency has improved by 10% since the last assessment.",
        "marketing campaign performance": "The latest marketing campaign has seen a 20% increase in engagement.",
        "default": "I'm sorry, I don't have information on that topic."
    }
    return random.choice(list(dummy_responses.values()))


def display_chatbot():
    with st.form("my_form"):
        query = st.text_area(
            "Enter text:", "How is this initiative performing?")
        submitted = st.form_submit_button("Submit")
        if submitted:
            with st.spinner('Processing...'):
                time.sleep(3)
            st.info(get_chatbot_response(query))
