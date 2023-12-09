import random
import time
import streamlit as st

# Dummy function to simulate chatbot responses


def get_chatbot_response(query):
    dummy_responses = {
        "current inventory accuracy": "Inventory accuracy currently stands at 98%, showing an improvement following the digital transformation initiative.",
        "stock turnover rate": "The stock turnover rate has increased by 12% since the implementation of the new inventory management system.",
        "progress on digital transformation": "The Digital Transformation for Inventory Management initiative is approximately 30% complete, on track with the projected timeline."
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
