import unittest
from translate_microsoft import subtitles_translator
from utils import exceptions

api_key = '9dcd4058b8ee4bd88b9838bda9a6f890'


class TestSubtitlesTranslator(unittest.TestCase):
    def test_init_when_dest_lang_exist(self):
        st = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, 'de')
        self.assertEqual(st.dest_lang, 'de')

    def test_init_when_dest_lang_exists_and_is_in_readable_form(self):
        st = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, 'russian')
        self.assertEqual(st.dest_lang, 'ru')

    def test_init_when_dest_lang_does_not_exist(self):
        st = subtitles_translator.SubtitlesTranslatorMicrosoft
        self.assertRaises(exceptions.LangDoesNotExists, st, api_key, 'zxcv')

    def test_translate_when_string_as_parameter(self):
        st = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, 'french')
        trans = st.translate
        self.assertRaises(SystemExit, trans, "the car's been dealt with, sir.")

    def test_translate_when_list_as_parameter(self):
        st = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, 'french')
        trans = st.translate(["the car's been dealt with, sir."])
        self.assertEqual(trans, "la voiture a été traitée, monsieur.")


if __name__ == '__main__':
    unittest.main()
