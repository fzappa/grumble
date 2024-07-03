import streamlit as st

from src.grumble.chat import display_chat_messages, initialize_chat
from src.grumble.ollama_utils import (
    list_ollama_models,
)  # Adicione esta linha para importar a função
from src.grumble.ui_utils import (
    configure_page,
    display_chat_input,
    display_model_name,
    display_sidebar,
    handle_pdf_upload,
)

# Configure page settings
configure_page()

# Ensure session state initialization
if "selected_model" not in st.session_state:
    model_names = list_ollama_models()
    if model_names:
        st.session_state.selected_model = model_names[0]

# Initialize chat
initialize_chat()

# Display sidebar and handle PDF upload
handle_pdf_upload()

# Display model name
display_model_name()

# Display chat messages and input
display_chat_messages()
display_chat_input()
