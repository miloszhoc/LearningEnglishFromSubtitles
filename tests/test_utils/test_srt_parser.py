import unittest
from utils import srt_parser

# file contains some possible scenarios
path_to_file = r'tests\test_utils\part_to_test.srt'


class TestSrtParser(unittest.TestCase):

    def test_read_srt_file_when_file_exists(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        self.assertTrue(parser.read_srt_file())

    def test_read_srt_file_when_file_doesnt_exists(self):
        parser = srt_parser.SrtParser(file='part.srt')
        self.assertFalse(parser.get_words_from_file())

    def test_get_words_from_file(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.get_words_from_file()
        self.assertListEqual(words, ['mr', 'white', 'hello', 'mr', 'white', 'the', "car's",
                                     'been', 'dealt', 'with', 'sir', 'we', "who's", 'we',
                                     'and', "i'll", 'handle', 'it', 'oh', 'no', 'no', 'no',
                                     'oh', 'god', 'no', 'no', 'than', 'we', 'could', 'spend',
                                     'in', 'lifetimes'])

    def test_words_without_repetitions(self):
        parser = srt_parser.SrtParser(file=path_to_file)

        # method words_without_repetitions returns set casted to list.
        # In order to compare something unordered with another unordered structure
        # method has to be casted again to set.
        words = set(parser.words_without_repetitions())
        self.assertSetEqual(words, {'mr', 'white', 'hello', 'mr', 'white', 'the', "car's",
                                    'been', 'dealt', 'with', 'sir', 'we', "who's", 'we',
                                    'and', "i'll", 'handle', 'it', 'oh', 'no', 'no', 'no',
                                    'oh', 'god', 'no', 'no', 'than', 'we', 'could', 'spend',
                                    'in', 'lifetimes'})

    def test_words_with_frequency(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        self.assertFalse(True)


if __name__ == '__main__':
    unittest.main()
