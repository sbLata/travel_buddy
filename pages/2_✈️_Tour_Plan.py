import streamlit as st

from utils import TravelPurpose, cached_ai_response, get_countries


def tour_plan_page():
    st.title("Create Your Tour Plan ✈️")

    countries = get_countries()

    # Collect inputs outside the form for real-time updates
    origin = st.selectbox("I am from:*", options=countries, index=None)
    destination = st.selectbox("I want to go to:*", options=countries, index=None)

    col1, col2 = st.columns(2)
    with col1:
        num_days = st.number_input(
            "Number of days I want to stay:*", min_value=1, max_value=30, value=1
        )
        num_adults = st.number_input("Number of adults:*", min_value=1, value=1)
    with col2:
        num_children = st.number_input("Number of children:", min_value=0, value=0)
        budget = st.number_input("Budget (USD):*", min_value=0, value=0)

    purpose = st.selectbox(
        "I want to travel for:*", options=[p.value for p in TravelPurpose]
    )
    special_instructions = st.text_area("Special instructions:")

    # Validation checks
    errors = []
    # print(
    #     origin,
    #     destination,
    #     num_days,
    #     num_adults,
    #     num_children,
    #     budget,
    #     purpose,
    #     special_instructions,
    # )
    if not origin:
        errors.append("Please select your origin.")
    if not destination:
        errors.append("Please select your destination.")
    if origin == destination:
        errors.append("Origin and destination cannot be the same.")
    if budget <= 0:
        errors.append("Please specify a valid budget.")

    # Display warnings dynamically
    if errors:
        for error in errors:
            st.warning(error)

    disabled = bool(errors)

    # Submit button reacts dynamically
    if st.button("Generate Tour Plan", disabled=disabled):
        if not disabled:
            prompt = f"""Please create a detailed {num_days}-day tour plan for {destination} with the following specifications:
            - Number of adults: {num_adults}
            - Number of children: {num_children}
            - Budget: ${budget}
            - Purpose: {purpose}
            - Special instructions: {special_instructions}

            Please include:
            1. Day-by-day itinerary
            2. Estimated costs for activities
            3. Recommended accommodations
            4. Transportation suggestions
            5. Meal recommendations
            """

            with st.spinner("Generating your personalized tour plan..."):
                plan = cached_ai_response(prompt)
                if plan:
                    st.success("Tour plan generated successfully!")
                    st.write(plan)

    st.markdown(
        "<small style='color: grey; position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;'>Note: This app generates AI-based content. Please use responsibly and verify the information as needed. The developer is not liable for inaccuracies.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    tour_plan_page()
