# pages/5_💭_Chat.py
import streamlit as st

from utils import model


def chat_page():
    st.title("Travel Assistant Chat 💭")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask me anything about your travel plans..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                if "chat" not in st.session_state:
                    st.session_state.chat = model.start_chat(history=[])

                response = st.session_state.chat.send_message(prompt)
                st.write(response.text)
                st.session_state.messages.append(
                    {"role": "assistant", "content": response.text}
                )

    st.markdown(
        "<small style='color: grey;'>Note: This app generates AI-based content. Please use responsibly and verify the information as needed. The developer is not liable for inaccuracies.</small>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    chat_page()
