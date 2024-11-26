# pages/4_💡_My_Tips.py
import streamlit as st

from utils import cached_ai_response, get_countries


def my_tips_page():
    st.title("Travel Tips 💡")

    countries = get_countries()
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    years = [2024, 2025, 2026, 2027, 2028, 2029, 2030]

    with st.form("travel_tips"):
        destination = st.selectbox("I am going to:", options=countries, index=None)

        col1, col2 = st.columns(2)
        with col1:
            month = st.selectbox("Month:", options=months, index=None)
        with col2:
            year = st.selectbox("Year:", options=years, index=None)

        submitted = st.form_submit_button("Get Travel Tips")

        if submitted and destination:
            prompt = f"""Please provide comprehensive travel tips for visiting {destination} in {month} {year}, including:
            1. Weather and what to expect
            2. Best time to visit
            3. Local customs and etiquette
            4. Safety precautions
            5. Transportation tips
            6. Packing essentials
            7. Seasonal events and festivals
            8. Local cuisine recommendations
            """

            with st.spinner(f"Finding best travel tips for {destination}..."):
                tips = cached_ai_response(prompt)
                if tips:
                    st.success("Travel tips generated!")
                    st.write(tips)
    st.markdown(
        "<small style='color: grey; position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;'>Note: This app generates AI-based content. Please use responsibly and verify the information as needed. The developer is not liable for inaccuracies.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    my_tips_page()
