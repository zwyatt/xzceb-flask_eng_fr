'''
Methods to translate EN-FR and FR-EN using the IBM Cloud Language Translator
for the Python Project for AI & Application Development course
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    ''' Translate English to French using the language_translator instance '''
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    ''' Translate French to English using the language_translator instance '''
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    return english_text['translations'][0]['translation']
