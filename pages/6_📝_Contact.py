# pages/6_📝_Contact.py

import streamlit as st


def contact_page():
    st.title("Contact Me 📝")

    st.write(
        """
    ### Let's Connect!
    
    Feel free to reach out to me through any of these platforms:

    - 💼 LinkedIn: [Suraiya Banu Lata](https://linkedin.com/in/suraiyabanulata)
    
    """
    )

    # with st.form("contact_form"):
    #     name = st.text_input("Name")
    #     email = st.text_input("Email")
    #     message = st.text_area("Message")
    #     submitted = st.form_submit_button("Send Message")

    #     if submitted:
    #         msg = MIMEMultipart()
    #         msg["From"] = "abc@gmail.com"
    #         msg["To"] = "abc@gmail.com"
    #         msg["Subject"] = "Contact Form Submission"
    #         body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    #         msg.attach(MIMEText(body, "plain"))

    #         server = smtplib.SMTP("smtp.gmail.com", 587)
    #         server.starttls()
    #         server.login(msg["From"], "xyt")
    #         text = msg.as_string()
    #         server.sendmail(msg["From"], msg["To"], text)
    #         server.quit()

    #     st.success("Thanks for reaching out! I'll get back to you soon.")

    st.markdown(
        "<small style='color: grey; position: fixed; bottom: 0; left: 0; width: 100%; text-align: center;'>Note: This app generates AI-based content. Please use responsibly and verify the information as needed. The developer is not liable for inaccuracies.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    contact_page()
