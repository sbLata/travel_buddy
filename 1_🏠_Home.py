# Home.py (main page)
import streamlit as st

from utils import initialize_session_state


def main():
    st.set_page_config(
        page_title="Travel Buddy",
        page_icon="🌎",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    initialize_session_state()

    st.title("Welcome to Travel Buddy! 🌎")
    st.write("Your AI-powered travel companion")

    # Introduction section
    st.markdown(
        """
    ### What can I help you with?
    
    - ✈️ **Plan Your Tour**: Create customized travel itineraries
    - 🛂 **Visa Information**: Get detailed visa requirements
    - 💡 **Travel Tips**: Discover essential tips for your destination
    - 💭 **Chat Assistance**: Get personalized travel advice
    - 📝 **Contact**: Get in touch with me
    - 👤 **Portfolio**: Check out my work
    
    ### How to get started?
    
    1. Navigate through the pages using the sidebar
    2. Fill in your travel details
    3. Get personalized recommendations and assistance
    """
    )

    # Featured destinations (optional)

    st.markdown(
        "<small style='color: grey; position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;'>Note: This app generates AI-based content. Please use responsibly and verify the information as needed. The developer is not liable for inaccuracies.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
