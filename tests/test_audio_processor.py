import pytest
from unittest.mock import patch, MagicMock
from modules.audio_processor import AudioProcessor

class DummyUploadedFile:
    def __init__(self, name="test.wav", content=b"fake audio"):
        self.name = name
        self._content = content

    def getvalue(self):
        return self._content

@patch("modules.audio_processor.requests.post")
def test_process_audio_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"text": "Hello world"}
    mock_post.return_value = mock_response

    processor = AudioProcessor(api_token="fake-token")
    uploaded_file = DummyUploadedFile()

    result = processor.process_audio(uploaded_file)

    assert result == "Hello world"
    mock_post.assert_called_once()

@patch("modules.audio_processor.requests.post")
def test_process_audio_api_error(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_post.return_value = mock_response

    processor = AudioProcessor(api_token="fake-token")
    uploaded_file = DummyUploadedFile()

    with pytest.raises(Exception) as exc_info:
        processor.process_audio(uploaded_file)

    assert "API error 500" in str(exc_info.value)
