import unittest
from translate_microsoft import words_translator
from translate_microsoft import exceptions
api_key = '9dcd4058b8ee4bd88b9838bda9a6f890'
words_list = ['mr', 'white', 'hello', 'mr', 'white', 'the', "car's"]


class TestTranslateMicrosoft(unittest.TestCase):
    def test_init_when_src_lang_does_not_exists(self):
        self.assertRaises(exceptions.LangDoesNotExists,
                          words_translator.TranslateWordsMicrosoft,
                          words_list=words_list,
                          api_key=api_key,
                          src_lang='abc',
                          dest_lang='en'
                          )

    def test_init_when_dest_lang_does_not_exists(self):
        self.assertRaises(exceptions.LangDoesNotExists,
                          words_translator.TranslateWordsMicrosoft,
                          words_list=words_list,
                          api_key=api_key,
                          src_lang='en',
                          dest_lang='pla'
                          )

    def test_init_when_src_lang_is_readable_and_both_lang_exists(self):
        tr = words_translator.TranslateWordsMicrosoft(words_list=words_list,
                                                      api_key=api_key,
                                                      src_lang='Polish',
                                                      dest_lang='en')

        self.assertEqual(tr.src_lang, 'pl')

    def test_init_when_dest_lang_is_readable_and_both_lang_exists(self):
        tr = words_translator.TranslateWordsMicrosoft(words_list=words_list,
                                                      api_key=api_key,
                                                      src_lang='en',
                                                      dest_lang='Polish')

        self.assertEqual(tr.dest_lang, 'pl')

    def test_init_if_src_lang_is_english_and_dest_lang_exist(self):
        tr = words_translator.TranslateWordsMicrosoft(words_list=words_list,
                                                      api_key=api_key,
                                                      src_lang='en',
                                                      dest_lang='de')
        self.assertEqual(tr.dest_lang, 'de')

    def test_translate_words(self):
        tr = words_translator.TranslateWordsMicrosoft(words_list=words_list,
                                                      api_key=api_key,
                                                      src_lang='en',
                                                      dest_lang='pl')
        self.assertGreater(len(tr.translate_words().values()), 0)

    def test_translate_words_with_frequency(self):
        tr = words_translator.TranslateWordsMicrosoft(words_list=words_list,
                                                      api_key=api_key,
                                                      src_lang='en',
                                                      dest_lang='pl')
        tr.translate_words_with_frequency()

        self.assertGreater(len(tr._translated_words), 0)


if __name__ == '__main__':
    unittest.main()
