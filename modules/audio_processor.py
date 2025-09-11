import tempfile
import os
import requests
import mimetypes

class AudioProcessor:
    def __init__(self, api_token, model_id="openai/whisper-large-v3"):
        self.api_token = api_token
        self.model_id = model_id
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_id}"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
    
    def process_audio(self, uploaded_file):
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=self._get_file_extension(uploaded_file.name)) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name

            try:
                with open(tmp_file_path, "rb") as f:
                    data = f.read()

                content_type, _ = mimetypes.guess_type(tmp_file_path)
                if not content_type:
                    content_type = "audio/wav"

                headers = self.headers.copy()
                headers["Content-Type"] = content_type

                response = requests.post(
                    self.api_url,
                    headers=headers,
                    data=data
                )

                if response.status_code != 200:
                    raise Exception(f"API error {response.status_code}: {response.text}")

                result = response.json()
                transcription = result.get("text")
                return transcription or ""

            finally:
                if os.path.exists(tmp_file_path):
                    os.unlink(tmp_file_path)

        except Exception as e:
            raise Exception(f"Error processing audio file: {str(e)}")
    
    def _get_file_extension(self, filename):
        if '.' in filename:
            return '.' + filename.split('.')[-1]
        return '.wav'
