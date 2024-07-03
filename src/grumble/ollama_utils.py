import requests
import streamlit as st
from langchain_community.llms import Ollama

OLLAMA_API_URL = "http://localhost:11434/api"
DEFAULT_PROMPT = "You are a helpful assistant. Please respond in plain text. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."

def list_ollama_models():
    try:
        response = requests.get(f"{OLLAMA_API_URL}/tags")
        response.raise_for_status()
        data = response.json()
        models = [model["name"] for model in data["models"]]
        return models
    except requests.ConnectionError:
        st.error("Failed to connect to the Ollama service. Please ensure it is running and try again.")
        return []
    except requests.RequestException as e:
        st.error(f"Failed to list models: {str(e)}")
        return []

def generate_ollama_response(model_name, prompt_input, temperature, top_p, max_length, pdf_text=None):
    string_dialogue = build_dialogue()
    input_text = f"{string_dialogue}User: {prompt_input}\n\nAssistant: "
    if pdf_text:
        input_text = f"PDF Content: {pdf_text}\n\n" + input_text

    try:
        llm = Ollama(model=model_name)
        response = llm.invoke(input_text, temperature=temperature, top_p=top_p, max_length=max_length)
        return response
    except Exception as e:
        st.error(f"Failed to generate response: {str(e)}")
        return "Sorry, I couldn't generate a response."

def build_dialogue():
    dialogue = DEFAULT_PROMPT + "\n\n"
    for message in st.session_state.messages:
        if message["role"] == "user":
            dialogue += f"User: {message['content']}\n\n"
        else:
            dialogue += f"Assistant: {message['content']}\n\n"
    return dialogue

