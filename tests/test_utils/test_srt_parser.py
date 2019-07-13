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

    def test_words_with_frequency_when_min_len_is_0_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency(min_len=0)
        self.assertFalse(words)

    def test_words_with_frequency_when_min_len_is_default_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency()
        self.assertEqual(len(words), len([('no', '5'), ('we', '3'), ('mr', '2'),
                                          ('white', '2'), ('oh', '2'), ('hello', '1'),
                                          ('the', '1'), ("car's", '1'), ('been', '1'),
                                          ('dealt', '1'), ('with', '1'), ('sir', '1'), ("who's", '1'),
                                          ('and', '1'), ("i'll", '1'), ('handle', '1'), ('it', '1'),
                                          ('god', '1'), ('than', '1'), ('could', '1'),
                                          ('spend', '1'), ('in', '1'), ('lifetimes', '1')]))

    def test_words_with_frequency_when_min_len_is_3_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency(min_len=3)
        self.assertEqual(len(words), len([('white', '2'), ('hello', '1'),
                                          ('the', '1'), ("car's", '1'), ('been', '1'),
                                          ('dealt', '1'), ('with', '1'), ('sir', '1'),
                                          ("who's", '1'), ('and', '1'), ("i'll", '1'),
                                          ('handle', '1'), ('god', '1'), ('than', '1'),
                                          ('could', '1'), ('spend', '1'), ('lifetimes', '1')]))

    def test_words_with_frequency_when_min_occurs_is_0_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency(min_occurs=0)
        self.assertFalse(words)

    def test_words_with_frequency_when_min_occurs_is_default_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency()
        self.assertEqual(len(words), len([('no', '5'), ('we', '3'), ('mr', '2'),
                                          ('white', '2'), ('oh', '2'), ('hello', '1'),
                                          ('the', '1'), ("car's", '1'), ('been', '1'),
                                          ('dealt', '1'), ('with', '1'), ('sir', '1'), ("who's", '1'),
                                          ('and', '1'), ("i'll", '1'), ('handle', '1'), ('it', '1'),
                                          ('god', '1'), ('than', '1'), ('could', '1'),
                                          ('spend', '1'), ('in', '1'), ('lifetimes', '1')]))

    def test_words_with_frequency_when_min_occurs_is_3_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency(min_occurs=3)
        self.assertEqual(len(words), len([('no', '5'), ('we', '3')]))

    def test_words_with_frequency_when_min_occurs_is_2_asc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency(min_occurs=2, descending=False)
        self.assertListEqual(words, [('mr', '2'), ('oh', '2'), ('white', '2'), ('we', '3'), ('no', '5')])

    def test_words_with_frequency_when_min_occurs_is_2_and_min_len_is_3_asc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency(min_len=3, min_occurs=2, descending=False)
        self.assertListEqual(words, [('white', '2')])


if __name__ == '__main__':
    unittest.main()
