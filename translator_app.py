from translation_service import TranslationService
from googletrans import LANGUAGES

def display_available_languages():
    """Display all available languages and their codes."""
    print("\nAvailable languages:")
    for code, language in LANGUAGES.items():
        print(f"{code}: {language.capitalize()}")

def get_user_input():
    """Get text and language choices from user."""
    text = input("\nEnter the text to translate: ")
    
    print("\nSource language (press Enter for auto-detection):")
    source_lang = input("Enter language code (e.g. 'en' for English): ").lower().strip()
    
    print("\nTarget language:")
    target_lang = input("Enter language code (e.g. 'es' for Spanish): ").lower().strip()
    
    return text, source_lang, target_lang

def main():
    translator = TranslationService()
    
    while True:
        print("\n=== Language Translator ===")
        print("1. Show available languages")
        print("2. Translate text")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            display_available_languages()
        
        elif choice == '2':
            text, source_lang, target_lang = get_user_input()
            
            try:
                result = translator.translate_text(text, source_lang, target_lang)
                print("\nTranslation Results:")
                print(f"Original text ({result['source_lang']}): {text}")
                print(f"Translated text ({target_lang}): {result['translated_text']}")
            
            except Exception as e:
                print(f"\nError: {str(e)}")
        
        elif choice == '3':
            print("\nThank you for using the translator!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main() 