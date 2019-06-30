import unittest
from utils import words_translator

api_key = ''
words_list = ['mr', 'white', 'hello', 'mr', 'white', 'the', "car's",
              'been', 'dealt', 'with', 'sir', 'we', "who's", 'we',
              'and', "i'll", 'handle', 'it', 'oh', 'no', 'no', 'no',
              'oh', 'god', 'no', 'no', 'than', 'we', 'could', 'spend',
              'in', 'lifetimes']


class TestTranslateMicrosoft(unittest.TestCase):
    def test_init_when_src_lang_does_not_exists(self):
        self.assertRaises(ValueError,
                          words_translator.TranslateMicrosoft,
                          words_list=words_list,
                          api_key=api_key,
                          src_lang='abc',
                          dest_lang='pl'
                          )

    def test_init_when_dest_lang_does_not_exists(self):
        self.assertRaises(ValueError,
                          words_translator.TranslateMicrosoft,
                          words_list=words_list,
                          api_key=api_key,
                          src_lang='en',
                          dest_lang='pla'
                          )

    def test_init_when_src_lang_and_dest_lang_does_not_exists(self):
        self.assertRaises(ValueError,
                          words_translator.TranslateMicrosoft,
                          words_list=words_list,
                          api_key=api_key,
                          src_lang='abc',
                          dest_lang='pla'
                          )

    def test_init_when_src_lang_is_readable_and_both_lang_exists(self):
        tr = words_translator.TranslateMicrosoft(words_list=words_list,
                                                 api_key=api_key,
                                                 src_lang='English',
                                                 dest_lang='pl')

        self.assertEqual(tr.src_lang, 'en')

    def test_init_when_dest_lang_is_readable_and_both_lang_exists(self):
        tr = words_translator.TranslateMicrosoft(words_list=words_list,
                                                 api_key=api_key,
                                                 src_lang='en',
                                                 dest_lang='Polish')

        self.assertEqual(tr.dest_lang, 'pl')

    def test_init_when_both_are_readable_and_both_lang_exists(self):
        tr = words_translator.TranslateMicrosoft(words_list=words_list,
                                                 api_key=api_key,
                                                 src_lang='en',
                                                 dest_lang='polish'.capitalize())

        self.assertEqual(tr.dest_lang, 'pl')
