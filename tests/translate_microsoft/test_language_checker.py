import unittest

from translate_microsoft import language_checker
from utils import exceptions


class TestLanguageChecker(unittest.TestCase):

    def test_show_all_languages_dictionary(self):
        lc = language_checker.CheckLanguage()
        self.assertGreater(len(lc.show_all_languages_dictionary()), 0)

    def test_check_lang_dictionary_when_lang_exists_lower_case(self):
        lc = language_checker.CheckLanguage()
        self.assertEqual(lc.check_lang_dictionary('greek'), 'el')

    def test_check_lang_dictionary_when_lang_exists_capitalize(self):
        lc = language_checker.CheckLanguage()
        self.assertEqual(lc.check_lang_dictionary('German'), 'de')

    def test_check_lang_dictionary_when_lang_exists_upper_case(self):
        lc = language_checker.CheckLanguage()
        self.assertEqual(lc.check_lang_dictionary('FRENCH'), 'fr')

    def test_check_lang_dictionary_when_lang_does_not_exists(self):
        lc = language_checker.CheckLanguage()
        self.assertRaises(exceptions.LangDoesNotExists, lc.check_lang_dictionary, 'xda')

    def test_show_all_languages_translation(self):
        lc = language_checker.CheckLanguage()
        self.assertGreater(len(lc.show_all_languages_translation()), 0)

    def test_check_lang_translation_when_lang_exists(self):
        lc = language_checker.CheckLanguage()
        self.assertEqual(lc.check_lang_translation('Tongan'), 'to')

    def test_check_lang_translation_when_lang_does_not_exists(self):
        lc = language_checker.CheckLanguage()
        self.assertRaises(exceptions.LangDoesNotExists, lc.check_lang_translation, 'qwerty')
