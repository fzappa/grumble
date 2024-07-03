import streamlit as st

from .chat import display_chat_messages, initialize_chat
from .ollama_utils import generate_ollama_response, list_ollama_models
from .pdf_utils import extract_text_from_pdf


def configure_page():
    st.set_page_config(page_title="🦙 GrumbleChat 💬", layout="wide")


def display_sidebar():
    st.sidebar.title("🦙 Grumble 💬")
    st.sidebar.subheader("Models and parameters")

    model_names = list_ollama_models()
    if model_names:
        if "selected_model" not in st.session_state:
            st.session_state.selected_model = model_names[0]

        st.sidebar.selectbox(
            "Choose an Ollama model", model_names, key="selected_model"
        )
        st.sidebar.slider("Temperature", 0.01, 1.0, 0.7, 0.01, key="temperature")
        st.sidebar.slider("Top_p", 0.01, 1.0, 0.9, 0.01, key="top_p")
        st.sidebar.slider("Max_length", 32, 128, 64, 8, key="max_length")
        st.sidebar.markdown("⚡ Alan Franco ⚡")
    else:
        st.sidebar.error("No models available in Ollama.")

    st.sidebar.button("Clear Chat History", on_click=clear_chat_history)
    uploaded_file = st.sidebar.file_uploader(
        "Upload your PDF", type=["pdf"], label_visibility="collapsed"
    )
    return uploaded_file


def display_model_name():
    st.sidebar.write(f"**Current Model:** {st.session_state.selected_model}")


def handle_pdf_upload():
    uploaded_file = display_sidebar()
    if uploaded_file and not st.session_state.pdf_processed:
        pdf_text = extract_text_from_pdf(uploaded_file)
        if pdf_text:
            st.session_state.pdf_text = pdf_text
            st.session_state.pdf_processed = True
            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": f"File {uploaded_file.name} uploaded successfully.",
                }
            )
            st.chat_message("user").markdown(
                f"File {uploaded_file.name} uploaded successfully."
            )

            with st.spinner("Thinking..."):
                response = generate_ollama_response(
                    st.session_state.selected_model,
                    "Please summarize the uploaded PDF.",
                    st.session_state.temperature,
                    st.session_state.top_p,
                    st.session_state.max_length,
                    pdf_text=pdf_text,
                )
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response,
                        "model": st.session_state.selected_model,
                    }
                )
                st.chat_message("assistant").markdown(
                    f"**{st.session_state.selected_model}**: {response}"
                )
            st.rerun()


def display_chat_input():
    prompt = st.chat_input("Enter your message here")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_ollama_response(
                    st.session_state.selected_model,
                    prompt,
                    st.session_state.temperature,
                    st.session_state.top_p,
                    st.session_state.max_length,
                )
            st.markdown(f"**{st.session_state.selected_model}**: {response}")
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
                "model": st.session_state.selected_model,
            }
        )


def clear_chat_history():
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "How may I assist you today?",
            "model": st.session_state.selected_model,
        }
    ]
    st.session_state.pdf_text = ""
    st.session_state.pdf_processed = False
