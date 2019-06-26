import uuid

import requests
import json


# uses microsoft translator api
class TranslateMicrosoft:
    def __init__(self, words_list, api_key):
        self._words_list = words_list
        self.subscriptionKey = api_key

        self.translated_words = {}
        self.headers = {}

    # codes for all languages
    # useful if you want translate subtitles from specific language to another
    @staticmethod
    def show_all_languages():
        languages = {}
        url = r'https://api.cognitive.microsofttranslator.com/languages?api-version=3.0'
        r = requests.get(url).json()
        for key, val in r['translation'].items():
            languages[val['name']] = key
        return languages

    # constructing url request
    # 'overloaded' method (one method - two jobs)
    # user has to pass src language if it's different than english
    # and dest language if it's different than polish
    def construct_request(self, src_lang='en', dest_lang='pl', with_frequency=False):
        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/dictionary/lookup?api-version=3.0&'
        params = 'from={0}&to={1}'.format(src_lang, dest_lang)
        constructed_url = base_url + path + params

        # headers
        headers = {
            'Ocp-Apim-Subscription-Key': self.subscriptionKey,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())}

        if with_frequency:
            for word in self._words_list:
                pass

        else:
            for word in self._words_list:
                # body contains text to translate
                body = [{'text': "{}".format(word)}]

                # request to endpoint
                req = requests.post(constructed_url,
                                    headers=headers,
                                    json=body)
                yield req.json()

    def translate_words(self):
        print('Translation in progress...\nPlease wait, process can take up to 5min')
        for i in self.construct_request():

            # some words or numbers can't be translated
            # that's why script checks if list with translations has length greater than 0
            if len(i[0]['translations']) > 0:
                self.translated_words[i[0]['displaySource'].lower()] = i[0]['translations'][0]['displayTarget'].lower()
        print('\n---Translated---')

    def translate_words_with_frequency(self):
        for i, j in zip(self._words_list, self.construct_request(with_frequency=True)):
            pass
