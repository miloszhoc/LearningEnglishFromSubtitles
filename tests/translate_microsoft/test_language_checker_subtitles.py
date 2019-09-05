import unittest

from translate_microsoft import language_checker_subtitles
from utils import exceptions


class TestLanguageCheckerSubtitles(unittest.TestCase):

    def setUp(self):
        self.lc = language_checker_subtitles.CheckLanguageSubtitles()

    def test_show_all_languages_translation(self):
        self.assertGreater(len(self.lc.show_all_languages_translation()), 0)

    def test_check_lang_translation_when_lang_exists_and_is_in_readable_form(self):
        self.assertEqual(self.lc.check_lang_translation('tongan'), 'to')

    def test_check_lang_translation_when_lang_exists_as_code(self):
        self.assertEqual(self.lc.check_lang_translation('to'), 'to')

    def test_check_lang_translation_when_lang_does_not_exists(self):
        self.assertRaises(exceptions.LangDoesNotExists, self.lc.check_lang_translation, 'qwerty')
