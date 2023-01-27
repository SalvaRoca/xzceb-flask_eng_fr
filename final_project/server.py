'''
Flask application for routing each endpoint to the desired function
'''

from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator")

@app.route("/englishToFrench")
def translate_to_french():
    '''
    Endpoint function to translate English text to French
    '''
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(text_to_translate)
    return translated_text

@app.route("/frenchToEnglish")
def translate_to_english():
    '''
    Endpoint function to translate French text to English
    '''
    text_to_translate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(text_to_translate)
    return translated_text

@app.route("/")
def render_index_page():
    '''
    Homepage endpoint
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host="0.0.0.0", port=8080)
