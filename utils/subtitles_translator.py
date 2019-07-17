import re
import requests
import uuid


# translate subtitles using Microsoft Translator
class SubtitlesTranslatorMicrosoft:
    def __init__(self, api_key):
        self._subscriptionKey = api_key

    # def detect_language(self, line):
    #     text = r"""{}""".format(line)
    #     url = r'https://api.cognitive.microsofttranslator.com/detect?api-version=3.0'
    #
    #     headers = {'Ocp-Apim-Subscription-Key': self._subscriptionKey,
    #                'Content-Type': 'application/json',
    #                'Content-Length': str(len(text)),
    #                'X-ClientTraceId': str(uuid.uuid4())}
    #
    #     body = [{"Text": text}]
    #     r = requests.post(url, headers=headers,
    #                       json=body)
    #     return r.json()[0]['language']

    # todo: allow other languages as destination language
    # todo: make function more flexible
    def _construct_request(self, content):
        text = r""""{}""".format(content)

        url = r'https://api.cognitive.microsofttranslator.com/translate?'
        query_params = 'api-version=3.0&' + 'to={}&'.format('pl') + 'textType=plain'
        full_url = url + query_params

        headers = {'Ocp-Apim-Subscription-Key': self._subscriptionKey,
                   'Content-Type': 'application/json',
                   'Content-Length': '1',
                   'X-ClientTraceId': str(uuid.uuid4())}

        body = [{"Text": text}]

        r = requests.post(full_url, headers=headers,
                          json=body)
        if r.status_code == 200:
            return r.json()[0]['translations'][0]['text']
        else:
            return False

    # Saves translated lines to .srt file
    # and decides which line should be translated or omitted.
    def translate_lines(self):
        pass

    # returns translated part of subtitles
    def translate_part(self, content):
        return self._construct_request(' '.join(content))
