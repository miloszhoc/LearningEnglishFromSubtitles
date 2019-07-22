import unittest

from translate_microsoft import language_checker


class TestLanguageChecker(unittest.TestCase):
    def test_show_all_languages_dictionary(self):
        lc = language_checker.CheckLanguage()
        self.assertGreater(len(lc.show_all_languages_dictionary()), 0)

    def test_show_all_languages_transaltion(self):
        lc = language_checker.CheckLanguage()
        self.assertGreater(len(lc.show_all_languages_translation()), 0)

    # todo: finish tests
