"""
Library for French to English translation and vice-versa
"""
#import json
import os
from os.path import join, dirname

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)
apikey = os.environ["APIKEY"]
url = os.environ["URL"]

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version = "2018-05-01", authenticator = authenticator)
language_translator.set_service_url(url)

def get_languages():
    """Returns the available languages for translation from the IBM Watson API"""
    return language_translator.list_identifiable_languages().get_result()

def english_to_french(english_text=None):
    """Function that translates English text into French"""
    if english_text is not None:
        fr_text_response = language_translator.translate(english_text, model_id="en-fr")
        fr_text_result = fr_text_response.get_result()
        fr_text = fr_text_result["translations"][0]["translation"]
    else:
        fr_text = "Missing text input! Rerun the code with a text next time."

    return fr_text

def french_to_english(french_text=None):
    """Function that translates French text into English"""
    if french_text is not None:
        en_text_response = language_translator.translate(french_text, model_id="fr-en")
        en_text_result = en_text_response.get_result()
        en_text = en_text_result["translations"][0]["translation"]
    else:
        en_text = "Missing text input! Rerun the code with a text next time."

    return en_text
