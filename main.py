import textblob
from deep_translator import GoogleTranslator


def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated
