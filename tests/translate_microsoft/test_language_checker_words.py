import unittest

from translate_microsoft.modules import language_checker_words
from exceptions import translator_exceptions


class TestLanguageCheckerSubtitles(unittest.TestCase):

    def setUp(self):
        self.lc = language_checker_words.CheckLanguageWords()

    def test_show_all_languages_dictionary(self):
        self.assertGreater(len(self.lc.show_all_languages_dictionary()), 0)

    def test_check_lang_dictionary_when_src_lang_does_not_exists(self):
        self.assertRaises(translator_exceptions.LangDoesNotExists,
                          self.lc.check_lang_dictionary,
                          src_lang='abc',
                          dest_lang='en')

    def test_check_lang_dictionary_when_dest_lang_does_not_exists(self):
        self.assertRaises(translator_exceptions.LangDoesNotExists,
                          self.lc.check_lang_dictionary,
                          src_lang='en',
                          dest_lang='pla')

    def test_check_lang_dictionary_when_src_lang_is_readable_and_both_lang_exists(self):
        langs = self.lc.check_lang_dictionary(src_lang='Polish',
                                              dest_lang='en')
        self.assertDictEqual(langs, {'src': 'pl',
                                     'dest': 'en'})

    def test_check_lang_dictionary_when_dest_lang_is_readable_and_both_lang_exists(self):
        langs = self.lc.check_lang_dictionary(src_lang='en',
                                              dest_lang='German')
        self.assertDictEqual(langs, {'src': 'en',
                                     'dest': 'de'})

    def test_check_lang_dictionary_when_both_are_readable_and_both_lang_exists_english_as_dest(self):
        langs = self.lc.check_lang_dictionary(src_lang='greek',
                                              dest_lang='English')
        self.assertDictEqual(langs, {'src': 'el',
                                     'dest': 'en'})

    def test_check_lang_dictionary_when_both_are_readable_and_both_lang_exists_english_as_src(self):
        langs = self.lc.check_lang_dictionary(src_lang='greek',
                                              dest_lang='English')
        self.assertDictEqual(langs, {'src': 'el',
                                     'dest': 'en'})

    def test_check_lang_dictionary_when_none_of_languages_is_english(self):
        self.assertRaises(translator_exceptions.EnglishNotFound,
                          self.lc.check_lang_dictionary,
                          src_lang='greek',
                          dest_lang='de')
