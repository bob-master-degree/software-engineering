import requests
import re

class TextTranslator:
    def __init__(self, api_token, model_id="Helsinki-NLP/opus-mt-en-ru"):
        self.api_token = api_token
        self.model_id = model_id
        self.api_url = f"https://api-inference.huggingface.co/models/{self.model_id}"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}
    
    def translate(self, text):
        if not text or not text.strip():
            return ""
        
        text = self._preprocess_text(text)
        
        response = requests.post(self.api_url, headers=self.headers, json={"inputs": text})
        if response.status_code != 200:
            raise Exception(f"API error {response.status_code}: {response.text}")
        
        result = response.json()
        translation = result[0].get("translation_text", "")
        return self._postprocess_translation(translation)
    
    def _preprocess_text(self, text):
        text = re.sub(r'\s+', ' ', text.strip())
        text = text.replace('\n', ' ').replace('\t', ' ')
        return text
    
    def _postprocess_translation(self, translation):
        translation = translation.strip()
        if translation:
            translation = translation[0].upper() + translation[1:]
        return translation
