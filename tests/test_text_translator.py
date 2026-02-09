import pytest
from unittest.mock import patch, MagicMock
from modules.text_translator import TextTranslator

@patch("modules.text_translator.requests.post")
def test_translate_success(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"translation_text": "Привет мир"}
    ]
    mock_post.return_value = mock_response

    translator = TextTranslator(api_token="fake-token")
    result = translator.translate("hello world")

    assert result == "Привет мир"
    mock_post.assert_called_once()

def test_translate_empty_text():
    translator = TextTranslator(api_token="fake-token")
    result = translator.translate("   ")
    assert result == ""

@patch("modules.text_translator.requests.post")
def test_translate_api_error(mock_post):
    mock_response = MagicMock()
    mock_response.status_code = 403
    mock_response.text = "Forbidden"
    mock_post.return_value = mock_response

    translator = TextTranslator(api_token="fake-token")

    with pytest.raises(Exception) as exc_info:
        translator.translate("hello")

    assert "API error 403" in str(exc_info.value)
