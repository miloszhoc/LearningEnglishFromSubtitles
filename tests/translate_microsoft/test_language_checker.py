import unittest

from translate_microsoft import language_checker
from utils import exceptions


class TestLanguageChecker(unittest.TestCase):

    def setUp(self):
        self.lc = language_checker.CheckLanguage()

    def test_show_all_languages_dictionary(self):
        self.assertGreater(len(self.lc.show_all_languages_dictionary()), 0)

    def test_check_lang_dictionary_when_src_lang_does_not_exists(self):
        self.assertRaises(exceptions.LangDoesNotExists,
                          self.lc.check_lang_dictionary,
                          src_lang='abc',
                          dest_lang='en')

    def test_check_lang_dictionary_when_dest_lang_does_not_exists(self):
        self.assertRaises(exceptions.LangDoesNotExists,
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
        self.assertRaises(exceptions.EnglishNotFound,
                          self.lc.check_lang_dictionary,
                          src_lang='greek',
                          dest_lang='de')

    def test_show_all_languages_translation(self):
        self.assertGreater(len(self.lc.show_all_languages_translation()), 0)

    def test_check_lang_translation_when_lang_exists_and_is_in_readable_form(self):
        self.assertEqual(self.lc.check_lang_translation('tongan'), 'to')

    def test_check_lang_translation_when_lang_exists_as_code(self):
        self.assertEqual(self.lc.check_lang_translation('to'), 'to')

    def test_check_lang_translation_when_lang_does_not_exists(self):
        self.assertRaises(exceptions.LangDoesNotExists, self.lc.check_lang_translation, 'qwerty')
