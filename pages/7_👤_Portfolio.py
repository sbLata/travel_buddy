# pages/7_👤_Portfolio.py
import streamlit as st


def portfolio_page():
    st.title("My Portfolio 👤")

    st.write(
        """
    ### About Me
    
    As a Product Manager with over 4 years of experience in SaaS product management, Agile methodologies, and cross-functional collaboration, I am passionate about driving innovative solutions. Recently, I have been exploring the world of Generative AI through certifications like Duke University's AI Product Management course and hands-on projects, such as building AI-powered applications using OpenAI API and Streamlit. This journey reflects my commitment to leveraging cutting-edge technologies to create impactful, user-centric products. 
    
    ### Skills
    - Critical Thinking
    - Requirement Analysis
    - Agile Leadership
    - Proactive
    - Solution oriented
    
    ## Hire Me
    - [LinkedIn](https://linkedin.com/in/suraiyabanulata)
    
    """
    )
    ### Projects
    # col1, col2 = st.columns(2)

    # with col1:
    #     st.subheader("Travel Buddy")
    #     st.image("paris.jpg")
    #     st.write(
    #         "An AI-powered travel companion app built with Streamlit and Google's Gemini API."
    #     )

    # with col2:
    #     st.subheader("Project 2")
    #     st.image("paris.jpg")
    #     st.write("Description of another impressive project.")

    # st.write(
    #     """
    # ### Education
    # - Bachelor's in Computer Science
    # - Relevant certifications

    # ### Work Experience
    # - Current role and company
    # - Previous experiences
    # """
    # )

    st.markdown(
        "<small style='color: grey; position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;'>Note: This app generates AI-based content. Please use responsibly and verify the information as needed. The developer is not liable for inaccuracies.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    portfolio_page()
