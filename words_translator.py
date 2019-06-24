import uuid

import requests


class TranslateMicrosoft:
    def __init__(self, words_list, api_key, dest_lang='pl'):
        self._words_list = words_list
        self.subscriptionKey = api_key
        self.dest_lang = dest_lang
        self.translated_words = {}
        self.headers = {}

    # constructing url request
    # 'overloaded' method (one method - two jobs)
    def construct_request(self, with_frequency=False):
        base_url = 'https://api.cognitive.microsofttranslator.com'
        path = '/dictionary/lookup?api-version=3.0&'
        params = 'from=en&to={}'.format(self.dest_lang)
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
        print('Translation in progress...\n')
        for i in self.construct_request():

            # some words can't be translated
            # that's why script checks if list with translations has length greater than 0
            if len(i[0]['translations']) > 0:
                self.translated_words[i[0]['displaySource'].lower()] = i[0]['translations'][0]['displayTarget'].lower()
        print('\n---Translated---')

    def translate_words_with_frequency(self):
        for i, j in zip(self._words_list, self.construct_request(True)):
            pass
