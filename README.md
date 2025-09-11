# Audio-to-Text App

A web application built with Streamlit that uses Hugging Face models to convert audio to English text, then translate the results to Russian.

## Models Used

| Model | Purpose | Provider |
|-------|---------|----------|
| `openai/whisper-large-v2` | Audio to Text (Speech Recognition) | OpenAI |
| `Helsinki-NLP/opus-mt-en-ru` | English to Russian Translation | Helsinki-NLP |

## Installation

### Prerequisites

- Python 3.8 or higher
- Hugging Face account with API token

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/bob-master-degree/software-engineering.git
   cd software-engineering
   ```

2. **Create virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get Hugging Face API Token**
   - Go to [Hugging Face Settings](https://huggingface.co/settings/tokens)
   - Create a new token with read access
   - Copy the token for use in the app

## Usage

### Running the Streamlit App

1. **Start the application**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Open your browser**
   - Navigate to the URL shown in the terminal
   - Enter your Hugging Face API token in the sidebar

## Project Structure

```
├── app.py                        # Streamlit app entrypoint
├── requirements.txt              # Dependencies
├── README.md
└── modules/
    ├── __init__.py
    ├── audio_processor.py        # Audio processing and transcription
    └── text_translator.py        # Text translation
```

---
