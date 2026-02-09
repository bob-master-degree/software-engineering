from unittest.mock import MagicMock

from modules.audio_processor import AudioProcessor
from modules.text_translator import TextTranslator

class DummyUploadedFile:
    def __init__(self, name="test.wav", content=b"fake audio"):
        self.name = name
        self._content = content

    def getvalue(self):
        return self._content

def test_audio_to_translation_flow(monkeypatch):
    fake_transcription = "Hello world"
    fake_translation = "Привет мир"

    audio_processor = AudioProcessor(api_token="fake-token")
    text_translator = TextTranslator(api_token="fake-token")

    monkeypatch.setattr(
        audio_processor,
        "process_audio",
        MagicMock(return_value=fake_transcription),
    )

    monkeypatch.setattr(
        text_translator,
        "translate",
        MagicMock(return_value=fake_translation),
    )

    uploaded_file = DummyUploadedFile()

    transcription = audio_processor.process_audio(uploaded_file)
    translation = text_translator.translate(transcription)

    assert transcription == fake_transcription
    assert translation == fake_translation

    audio_processor.process_audio.assert_called_once_with(uploaded_file)
    text_translator.translate.assert_called_once_with(fake_transcription)
