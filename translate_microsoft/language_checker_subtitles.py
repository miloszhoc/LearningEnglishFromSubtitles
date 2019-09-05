import requests
from utils import exceptions


class CheckLanguageSubtitles:

    # codes for all languages in translation scope
    # dictionary contains - Language: code
    def show_all_languages_translation(self):
        languages = {}
        url = r'https://api.cognitive.microsofttranslator.com/languages?api-version=3.0&scope=translation'
        r = requests.get(url).json()
        for key, val in r['translation'].items():
            languages[val['name']] = key
        return languages

    def check_lang_translation(self, dest_lang):
        languages = self.show_all_languages_translation()
        if dest_lang in languages.values():
            pass
        elif dest_lang.capitalize() in languages:
            dest_lang = languages[dest_lang.capitalize()]
        else:
            raise exceptions.LangDoesNotExists
        return dest_lang

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
