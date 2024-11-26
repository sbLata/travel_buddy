# utils.py
import os
import time
import random
import pycountry
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from enum import Enum

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Set up the model
model = genai.GenerativeModel("gemini-pro")

class TravelPurpose(str, Enum):
    HONEYMOON = "Honeymoon"
    FAMILY = "Family Vacation"
    ADVENTURE = "Adventure"
    BUSINESS = "Business"
    CULTURAL = "Cultural Experience"
    RELAXATION = "Relaxation"
    OTHER = "Other"

# Caching functions
@st.cache_data(ttl=3600, show_spinner=False)
def cached_ai_response(prompt, chat_history=None):
    try:
        model = genai.GenerativeModel("gemini-pro")
        if chat_history:
            chat = model.start_chat(history=chat_history)
            response = chat.send_message(prompt)
        else:
            chat = model.start_chat(history=[])
            response = chat.send_message(prompt)
        return response.text
    except Exception as e:
        st.error(f"Error getting response from AI: {str(e)}")
        return None

@st.cache_data
def get_countries():
    return [c.name for c in pycountry.countries]

def initialize_session_state():
    default_states = {
        "name": None,
        "origin_country": None,
        "destination": None,
        "messages": [],
        "chat": None,
        "travel_tips": None,
        "visa_info": None,
    }

    for key, default_value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = default_value