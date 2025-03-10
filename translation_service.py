from deep_translator import GoogleTranslator
from googletrans import LANGUAGES

class TranslationService:
    def __init__(self):
        """Initialize the translator service."""
        pass
    
    def validate_language(self, lang_code):
        """Validate if the language code is supported."""
        if not lang_code:  # Empty string for auto-detection is OK
            return True
        
        if lang_code not in LANGUAGES:
            raise ValueError(f"Language code '{lang_code}' is not supported")
        return True
    
    def translate_text(self, text, source_lang="", target_lang="en"):
        """
        Translate text from source language to target language.
        
        Args:
            text (str): Text to translate
            source_lang (str): Source language code (empty for auto-detection)
            target_lang (str): Target language code
            
        Returns:
            dict: Dictionary containing translated text and detected source language
        """
        if not text.strip():
            raise ValueError("Please enter some text to translate")
        
        self.validate_language(source_lang)
        self.validate_language(target_lang)
        
        try:
            # If source_lang is empty, use 'auto'
            translator = GoogleTranslator(
                source=source_lang if source_lang else 'auto',
                target=target_lang
            )
            
            translated_text = translator.translate(text)
            detected_source = source_lang if source_lang else translator.source
            
            return {
                'translated_text': translated_text,
                'source_lang': detected_source
            }
            
        except Exception as e:
            raise Exception(f"Translation failed: {str(e)}") from e 