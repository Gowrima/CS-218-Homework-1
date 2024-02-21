from bottle import *
from fruits_unicode import *

languages = ['Kannada', 'Tamil', 'Malayalam']
fruits = [fruit for fruit in fruit_names_unicode]

@route('/')
def welcome():
    response.content_type = 'text/html; charset=utf-8'
    return '<h1>Homework 1: Translate fruit name into Kannada, Tamil or Malayalam!</h1>'

@route('/<lang>/<word>')
def translate_(lang, word):
    response.content_type = 'text/html; charset=utf-8'

    if lang not in languages or word not in fruits:
        return "Invalid fruit/language"

    try:
        translation = fruit_names_unicode[word][lang]
        translation_message = f"Translation of {word} in {lang} is {translation}"
        return translation_message.encode('utf-8')
    except KeyError:
        return "Fruit not found"

if __name__ == '__main__':
    run(host='0.0.0.0', port='8080')
