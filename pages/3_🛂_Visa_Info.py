# pages/3_🛂_Visa_Info.py
import streamlit as st

from utils import cached_ai_response, get_countries


def visa_info_page():
    st.title("Visa Information 🛂")

    countries = get_countries()

    with st.form("visa_info"):
        citizenship = st.selectbox("I am a citizen of:", options=countries, index=None)
        destination = st.selectbox("I want to visit:", options=countries, index=None)

        submitted = st.form_submit_button("Get Visa Information")

        if submitted and citizenship and destination:
            prompt = f"""Please provide detailed visa information for a {citizenship} citizen traveling to {destination}, including:
            1. Visa requirements and types
            2. Application process
            3. Required documents
            4. Processing time
            5. Fees
            6. Important notes or special conditions
            """

            with st.spinner("Fetching visa information..."):
                info = cached_ai_response(prompt)
                if info:
                    st.success("Visa information retrieved!")
                    st.write(info)
    st.markdown(
        "<small style='color: grey; position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;'>Note: This app generates AI-based content. Please use responsibly and verify the information as needed. The developer is not liable for inaccuracies.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    visa_info_page()
