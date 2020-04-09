# -*- coding: utf-8 -*-

from google.cloud import translate_v2 as translate
"""
Translate to:

3) en already there
2) fr
3) de
4) es
5) sv
6) it
7) pt
"""
def translate_text(text, target='en'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language = target)
    print('Text: ', result['input'])
    print('Translation: ', result['translatedText'])
    print('Detected source lang: ', result['detectedSourceLanguage'])

example_text = 'Olá, tudo bem? Acho que podiamos fazer uma festa hoje'

translate_text(example_text)