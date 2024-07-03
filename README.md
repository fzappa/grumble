# 🦙 Grumble 💬

Grumble is a Streamlit-based chatbot application that leverages models available in Ollama to provide responses to user inputs. This application allows users to upload PDF files, extract text from them, and use the extracted text to generate responses from selected language models.

## Features

- List and select available models from Ollama.
- Upload PDF files and extract text using `pdfplumber`.
- Generate responses using selected models from Ollama.
- Display chat messages with a user-friendly interface.
- Clear chat history with a single click.

## Installation

1. Clone the repository:

```sh
git clone https://github.com/fzappa/grumble.git
cd grumble
```

2. **Create the Hatch environment**:

If you are already using a python environment (Anaconda, mamba, miniconda...)

```bash
pip install hatch
hatch env create
```

## Running the Application

1. Ensure the Ollama service is running and accessible at `http://localhost:11434`.

2. Start the Streamlit application:

```sh
hatch run streamlit run grumble.py
```

3. Open your web browser and navigate to `http://localhost:8501` to use the chatbot.

## Usage

1. **Select a Model:**

   - Choose an available model from the dropdown list in the sidebar.

2. **Upload a PDF:**

   - Use the file uploader in the main interface to upload a PDF file.
   - Once uploaded, the text from the PDF will be extracted.

3. **Chat:**

   - The extracted text will be used to generate responses from the selected model.
   - Chat messages will be displayed in the main interface.

4. **Clear Chat History:**
   - Click the "Clear Chat History" button in the sidebar to reset the chat.

## Code Overview

### Constants

**src/grumble/ollama_utils.py**

- `OLLAMA_API_URL`: The base URL for the Ollama API.
- `DEFAULT_PROMPT`: The default prompt used to initialize the chat.
