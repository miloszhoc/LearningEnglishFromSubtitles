import unittest
from translate_microsoft.modules import subtitles_translator
from . import api_key


class TestSubtitlesTranslator(unittest.TestCase):

    def test_translate_when_string_as_parameter(self):
        st = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, 'fr')
        trans = st.translate
        self.assertRaises(SystemExit, trans, "the car's been dealt with, sir.")

    def test_translate_when_list_as_parameter(self):
        st = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, 'fr')
        trans = st.translate(["the car's been dealt with, sir."])
        self.assertEqual(trans, "la voiture a été traitée, monsieur.")
