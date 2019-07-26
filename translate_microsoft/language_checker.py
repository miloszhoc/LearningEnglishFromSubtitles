# -*- coding: utf-8 -*-
import requests
from translate_microsoft import exceptions


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

    def check_lang_dictionary(self, full_lang):
        for readable, code in self.show_all_languages_dictionary().items():
            if full_lang.capitalize() in readable:
                out_code = code
                break
        else:
            raise exceptions.LangDoesNotExists
        return out_code

    def check_lang_translation(self, full_lang):
        for readable, code in self.show_all_languages_translation().items():
            if full_lang.capitalize() in readable:
                out_code = code
                break
        else:
            raise exceptions.LangDoesNotExists
        return out_code
