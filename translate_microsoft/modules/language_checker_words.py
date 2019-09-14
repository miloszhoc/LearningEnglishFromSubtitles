import requests
from exceptions import translator_exceptions


# codes for all languages in dictionary scope
# dictionary contains - Language: code
class CheckLanguageWords:
    def show_all_languages_dictionary(self):
        languages = {}
        url = r'https://api.cognitive.microsofttranslator.com/languages?api-version=3.0&scope=dictionary'
        r = requests.get(url).json()
        for key, val in r['dictionary'].items():
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
                    raise translator_exceptions.LangDoesNotExists

        elif dest_lang == 'en' or dest_lang.capitalize() == 'English':
            lang_codes['dest'] = 'en'
            if src_lang in languages.values():
                lang_codes['src'] = src_lang
            else:
                if src_lang.capitalize() in languages:
                    lang_codes['src'] = languages[src_lang.capitalize()]
                else:
                    raise translator_exceptions.LangDoesNotExists

        else:
            raise translator_exceptions.EnglishNotFound
        return lang_codes
