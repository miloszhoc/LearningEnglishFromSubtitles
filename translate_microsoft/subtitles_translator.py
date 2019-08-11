import requests
import uuid
from translate_microsoft import language_checker


# translate subtitles using Microsoft Translator
class SubtitlesTranslatorMicrosoft:
    def __init__(self, api_key, dest_lang):
        self._subscriptionKey = api_key
        check_lang = language_checker.CheckLanguage()
        languages = check_lang.show_all_languages_translation()
        # todo: move language checking to external class
        if dest_lang in languages.values():
            self.dest_lang = dest_lang
        else:
            self.dest_lang = check_lang.check_lang_translation(dest_lang)

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

    def _construct_request(self, content):
        text = r"""{}""".format(content)

        url = r'https://api.cognitive.microsofttranslator.com/translate?'
        query_params = 'api-version=3.0&' + 'to={}&'.format(self.dest_lang) + 'textType=plain'
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

    # returns translated part of subtitles
    def translate(self, content):
        try:
            assert isinstance(content, list)
        except AssertionError:
            print("Error while translation")
            exit()
        else:
            return self._construct_request(' '.join(content))
