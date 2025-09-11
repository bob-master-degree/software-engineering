import streamlit as st
from modules.audio_processor import AudioProcessor
from modules.text_translator import TextTranslator

st.set_page_config(page_title="Audio-to-Russian Translation App", page_icon="🎵", layout="wide")

st.title("🎵 Audio-to-Russian Translation App")
st.markdown("Convert audio to English text, then translate to Russian using Hugging Face models")

with st.sidebar:
    st.header("⚙️ Configuration")
    api_token = st.text_input("Hugging Face API Token", type="password", help="Enter your Hugging Face API token")
    if not api_token:
        st.warning("⚠️ Please enter your Hugging Face API token to use the app")
        st.stop()
    st.markdown("---")
    st.markdown("### 📋 Available Models")
    st.markdown("- **Audio-to-Text**: openai/whisper-large-v2")
    st.markdown("- **Translation**: Helsinki-NLP/opus-mt-en-ru")

audio_processor = AudioProcessor(api_token)
text_translator = TextTranslator(api_token)

st.header("🔄 Audio-to-Russian Workflow")
uploaded_audio_workflow = st.file_uploader("Upload Audio for Full Workflow", type=['wav', 'mp3', 'm4a', 'flac', 'ogg'], key="workflow_audio")
if uploaded_audio_workflow and st.button("🚀 Process Workflow"):
    with st.spinner("Processing..."):
        transcription = audio_processor.process_audio(uploaded_audio_workflow)
        translation = text_translator.translate(transcription)
        st.success(f"English Transcription: {transcription}")
        st.success(f"Russian Translation: {translation}")
