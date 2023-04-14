from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

def extract_text(translated):
    ''' Extracts text from the dictionary that is returned by language_translator '''
    text = translated['translations']
    text = text[0]
    text = text['translation']
    return text

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated = translator.english_to_french(textToTranslate)
    text = extract_text(translated)
    return text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated = translator.french_to_english(textToTranslate)
    text = extract_text(translated)
    return text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
