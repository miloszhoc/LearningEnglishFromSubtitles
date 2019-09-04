import requests
from utils import exceptions


# todo: split into 2 classes (for words and text)
class CheckLanguage:

    # codes for all languages in dictionary scope
    # dictionary contains - Language: code
    def show_all_languages_dictionary(self):
        languages = {}
        url = r'https://api.cognitive.microsofttranslator.com/languages?api-version=3.0&scope=dictionary'
        r = requests.get(url).json()
        for key, val in r['dictionary'].items():
            languages[val['name']] = key
        return languages

    # codes for all languages in translation scope
    # dictionary contains - Language: code
    def show_all_languages_translation(self):
        languages = {}
        url = r'https://api.cognitive.microsofttranslator.com/languages?api-version=3.0&scope=translation'
        r = requests.get(url).json()
        for key, val in r['translation'].items():
            languages[val['name']] = key
        return languages

    def check_lang_dictionary(self, src_lang, dest_lang):
        # The only possibility according to Translator API documentation
        # is to translate words from or to English.

        # Code checks if language given by user is in list with supported languages
        # if it is, src_lang will be set to value given by user
        # else it checks if user typed for example 'English',
        # if both cases are false exception will be raised.

        lang_codes = {}
        languages = self.show_all_languages_dictionary()

        if src_lang == 'en' or src_lang.capitalize() == 'English':
            lang_codes['src'] = 'en'
            if dest_lang in languages.values():
                lang_codes['dest'] = dest_lang
            else:
                if dest_lang.capitalize() in languages:
                    lang_codes['dest'] = languages[dest_lang.capitalize()]
                else:
                    raise exceptions.LangDoesNotExists

        elif dest_lang == 'en' or dest_lang.capitalize() == 'English':
            lang_codes['dest'] = 'en'
            if src_lang in languages.values():
                lang_codes['src'] = src_lang
            else:
                if src_lang.capitalize() in languages:
                    lang_codes['src'] = languages[src_lang.capitalize()]
                else:
                    raise exceptions.LangDoesNotExists

        else:
            raise exceptions.EnglishNotFound
        return lang_codes

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
