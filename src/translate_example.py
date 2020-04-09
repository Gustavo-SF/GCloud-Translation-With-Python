# -*- coding: utf-8 -*-

from google.cloud import translate_v2 as translate


def translate_text(text, target='en'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language = target)
    print('Text: ', result['input'])
    print('Translation: ', result['translatedText'])
    print('Detected source lang: ', result['detectedSourceLanguage'])

example_text = 'Olá, tudo bem? Acho que podiamos fazer uma festa hoje'

translate_text(example_text)