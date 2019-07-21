import uuid

import requests


# uses microsoft translator api
class TranslateWordsMicrosoft:
    def __init__(self, words_list, api_key, src_lang='en', dest_lang='pl'):
        # dictionary contains Language: code
        # keys contains languages in readable form eg. 'English', 'Polish', 'German'
        # values contains languages codes eg. 'en', 'fr', 'pl'
        languages = TranslateWordsMicrosoft.show_all_languages()

        # code checks if language given by user is in list with supported languages
        # if it is src_lang is set to value given by user
        # else it checks if user typed for example 'English'
        # if both cases are false variable is set to ''
        if src_lang in languages.values():
            self.src_lang = src_lang
        else:
            for readable, code in languages.items():
                if src_lang.capitalize() in readable:
                    self.src_lang = code
                    break
            else:
                self.src_lang = ''

        # The only possibility according to Translator API documentation
        # is to translate words from or to English.
        # If source language is set to English program should ask about
        # destination language.
        # If source is set to different language than English program should
        # automatically set destination language to English
        if self.src_lang == 'en':
            if dest_lang in languages.values():
                self.dest_lang = dest_lang
            else:
                for readable, code in languages.items():
                    if dest_lang.capitalize() in readable:
                        self.dest_lang = code
                        break
                else:
                    self.dest_lang = ''
        else:
            print("Setting destination language to English...")
            self.dest_lang = 'en'

        # 'final check' checks if language is supported by Translator
        if (self.src_lang in languages.values() and self.dest_lang in languages.values()) \
                and (self.src_lang == 'en' or self.dest_lang == 'en'):
            print('Translation from: ' + self.src_lang + ' to: ' + self.dest_lang)
        else:
            raise ValueError

        self._words_list = words_list
        self._subscriptionKey = api_key
        self._translated_words = {}

    # codes of all languages
    # useful if you want translate words from specific language to another
    # dictionary contains - Language: code
    @staticmethod
    def show_all_languages():
        languages = {}
        url = r'https://api.cognitive.microsofttranslator.com/languages?api-version=3.0&scope=dictionary'
        r = requests.get(url).json()
        for key, val in r['dictionary'].items():
            languages[val['name']] = key
        return languages

    # constructing url request
    # 'overloaded' method (one method - two jobs)
    def _construct_request(self, with_frequency=False):
        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/dictionary/lookup?api-version=3.0&'
        params = 'from={0}&to={1}'.format(self.src_lang, self.dest_lang)
        constructed_url = base_url + path + params

        # headers
        headers = {
            'Ocp-Apim-Subscription-Key': self._subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())}

        if with_frequency:
            for word in self._words_list:
                # body contains text to translate
                body = [{'text': "{}".format(word[0])}]
                # request to endpoint
                req = requests.post(constructed_url,
                                    headers=headers,
                                    json=body)
                if req.status_code == 200:
                    yield req.json()
                else:
                    return False
        else:
            for word in self._words_list:
                # body contains text to translate
                body = [{'text': "{}".format(word)}]

                # request to endpoint
                req = requests.post(constructed_url,
                                    headers=headers,
                                    json=body)
                if req.status_code == 200:
                    yield req.json()
                else:
                    return False

    def translate_words(self):
        print('Translation in progress...\nPlease wait, process can take up to 5min')
        for i in self._construct_request():

            # some words or numbers can't be translated
            # that's why script checks if list with translations has length greater than 0
            if len(i[0]['translations']) > 0:
                self._translated_words[i[0]['displaySource'].lower()] = i[0]['translations'][0]['displayTarget'].lower()
        print('\nAll words translated!')
        return self._translated_words

    def translate_words_with_frequency(self):
        print('Translation in progress...\nPlease wait, process can take up to 5min')
        for original, translated in zip(self._words_list, self._construct_request(with_frequency=True)):
            # some words or numbers can't be translated
            # that's why script checks if list with translations has length greater than 0
            if len(translated[0]['translations']) > 0:
                self._translated_words[original[0]] = (translated[0]['translations'][0]['displayTarget'].lower(),
                                                       original[1])
        print('\nAll words translated!')
        return self._translated_words
