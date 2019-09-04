import unittest
from translate_microsoft import words_translator
from . import api_key

words_list = ['mr', 'white', 'hello', 'mr', 'white', 'the', "car's"]


# todo: add more tests
class TestTranslateWordsMicrosoft(unittest.TestCase):

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
