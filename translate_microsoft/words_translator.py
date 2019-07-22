import uuid

import requests
from translate_microsoft import language_checker


# uses microsoft translator api
class TranslateWordsMicrosoft:
    def __init__(self, words_list, api_key, src_lang, dest_lang):
        # dictionary contains Language: code
        # keys contains languages in readable form eg. 'English', 'Polish', 'German'
        # values contains languages codes eg. 'en', 'fr', 'pl'
        check_lang = language_checker.CheckLanguage()
        languages = check_lang.show_all_languages_dictionary()

        # Code checks if language given by user is in list with supported languages
        # if it is, src_lang will be set to value given by user
        # else it checks if user typed for example 'English',
        # if both cases are false exception will be raised.

        # The only possibility according to Translator API documentation
        # is to translate words from or to English.
        # If source language is set to English program should ask about
        # destination language.
        # If source is set to different language than English program will
        # automatically set destination language to English
        if src_lang == 'en':
            self.src_lang = src_lang
            if dest_lang in languages.values():
                self.dest_lang = dest_lang
            else:
                self.dest_lang = check_lang.check_lang_dictionary(dest_lang)
        else:
            self.dest_lang = 'en'
            if src_lang in languages.values():
                self.src_lang = src_lang
            else:
                self.src_lang = check_lang.check_lang_dictionary(src_lang)

        self._words_list = words_list
        self._subscriptionKey = api_key
        self._translated_words = {}

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
        for i in self._construct_request():

            # some words or numbers can't be translated
            # that's why script checks if list with translations has length greater than 0
            if len(i[0]['translations']) > 0:
                self._translated_words[i[0]['displaySource'].lower()] = i[0]['translations'][0]['displayTarget'].lower()
        return self._translated_words

    def translate_words_with_frequency(self):
        for original, translated in zip(self._words_list, self._construct_request(with_frequency=True)):
            # some words or numbers can't be translated
            # that's why script checks if list with translations has length greater than 0
            if len(translated[0]['translations']) > 0:
                self._translated_words[original[0]] = (translated[0]['translations'][0]['displayTarget'].lower(),
                                                       original[1])
        return self._translated_words
