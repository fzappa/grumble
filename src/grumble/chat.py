import streamlit as st


def initialize_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "How may I assist you today?",
                "model": st.session_state.selected_model,
            }
        ]
    if "pdf_text" not in st.session_state:
        st.session_state.pdf_text = ""
    if "pdf_processed" not in st.session_state:
        st.session_state.pdf_processed = False


def display_chat_messages():
    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        model = message.get("model", "Unknown Model")
        if role == "assistant":
            st.chat_message(role).markdown(f"**{model}**: {content}")
        else:
            st.chat_message(role).markdown(content)
