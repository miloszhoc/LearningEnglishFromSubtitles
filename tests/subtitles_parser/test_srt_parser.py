import unittest
from parser import srt_parser
from exceptions import parser_exceptions

# file contains some possible scenarios
path_to_file = r'tests/subtitles/part_to_test.srt'


class TestSrtParser(unittest.TestCase):

    def test_read_srt_file_when_file_doesnt_exists(self):
        parser = srt_parser.SrtParser(file='part.srt')
        self.assertRaises(SystemExit, parser.get_words_from_file)

    def test_get_words_from_file(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.get_words_from_file()
        self.assertListEqual(words, ['mr', 'white', 'hello', 'mr', 'white', 'the', "car's",
                                     'been', 'dealt', 'with', 'sir', 'we', "who's", 'we',
                                     'and', "i'll", 'handle', 'it', 'oh', 'no', 'no', 'no',
                                     'oh', 'god', 'no', 'no', 'than', 'we', 'could', 'spend',
                                     'in', 'lifetimes', 'know', 'you', 'think', "i'm", 'sociopath',
                                     'יש', 'לך', 'את', 'זה', 'הנה', 'היא', 'באה', 'ich', 'weiß',
                                     'noch', 'nicht', 'genau', 'астральна', 'площина', 'нагадувала',
                                     'магніт'])

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
                                    'in', 'lifetimes', 'know', 'you', 'think', "i'm", 'sociopath',
                                    'יש', 'לך', 'את', 'זה', 'הנה', 'היא', 'באה', 'ich', 'weiß',
                                    'noch', 'nicht', 'genau', 'астральна', 'площина', 'нагадувала',
                                    'магніт'})

    def test_words_with_frequency_when_min_len_is_0(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency
        self.assertRaises(parser_exceptions.LenLessEqualZero, words, min_len=0)

    def test_words_with_frequency_when_min_len_is_negative(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency
        self.assertRaises(parser_exceptions.LenLessEqualZero, words, min_len=-1)

    def test_words_with_frequency_when_min_len_is_default_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency()
        self.assertEqual(len(words), len([('no', '5'), ('we', '3'), ('mr', '2'),
                                          ('white', '2'), ('oh', '2'), ('hello', '1'),
                                          ('the', '1'), ("car's", '1'), ('been', '1'),
                                          ('dealt', '1'), ('with', '1'), ('sir', '1'), ("who's", '1'),
                                          ('and', '1'), ("i'll", '1'), ('handle', '1'), ('it', '1'),
                                          ('god', '1'), ('than', '1'), ('could', '1'),
                                          ('spend', '1'), ('in', '1'), ('lifetimes', '1'),
                                          ('know', '1'), ('you', '1'), ('think', '1'), ("i'm", '1'),
                                          ('sociopath', '1'), ('ich', '1'), ('weiß', '1'), ('באה', '1'),
                                          ('היא', '1'), ('הנה', '1'), ('זה', '1'), ('את', '1'), ('לך', '1'),
                                          ('יש', '1'), ('noch', '1'), ('nicht', '1'), ('genau', '1'),
                                          ('астральна', '1'), ('площина', '1'), ('нагадувала', '1'),
                                          ('магніт', '1')]))

    def test_words_with_frequency_when_min_len_is_3_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency(min_len=3)
        self.assertEqual(len(words), len([('white', '2'), ('hello', '1'),
                                          ('the', '1'), ("car's", '1'), ('been', '1'),
                                          ('dealt', '1'), ('with', '1'), ('sir', '1'),
                                          ("who's", '1'), ('and', '1'), ("i'll", '1'),
                                          ('handle', '1'), ('god', '1'), ('than', '1'),
                                          ('could', '1'), ('spend', '1'), ('lifetimes', '1'),
                                          ('know', '1'), ('you', '1'), ('think', '1'), ("i'm", '1'),
                                          ('sociopath', '1'), ('ich', '1'), ('weiß', '1'), ('באה', '1'),
                                          ('היא', '1'), ('הנה', '1'), ('noch', '1'), ('nicht', '1'),
                                          ('genau', '1'), ('астральна', '1'), ('площина', '1'),
                                          ('нагадувала', '1'), ('магніт', '1')]))

    def test_words_with_frequency_when_min_occurs_is_0(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency
        self.assertRaises(parser_exceptions.OccursLessEqualZero, words, min_occurs=0)

    def test_words_with_frequency_when_min_occurs_is_negative(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency
        self.assertRaises(parser_exceptions.OccursLessEqualZero, words, min_occurs=-2)

    def test_words_with_frequency_when_min_occurs_is_default_desc(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        words = parser.words_with_frequency()
        self.assertEqual(len(words), len([('no', '5'), ('we', '3'), ('mr', '2'),
                                          ('white', '2'), ('oh', '2'), ('hello', '1'),
                                          ('the', '1'), ("car's", '1'), ('been', '1'),
                                          ('dealt', '1'), ('with', '1'), ('sir', '1'), ("who's", '1'),
                                          ('and', '1'), ("i'll", '1'), ('handle', '1'), ('it', '1'),
                                          ('god', '1'), ('than', '1'), ('could', '1'),
                                          ('spend', '1'), ('in', '1'), ('lifetimes', '1'),
                                          ('know', '1'), ('you', '1'), ('think', '1'), ("i'm", '1'),
                                          ('sociopath', '1'), ('ich', '1'), ('weiß', '1'), ('באה', '1'),
                                          ('היא', '1'), ('הנה', '1'), ('זה', '1'), ('את', '1'), ('לך', '1'),
                                          ('יש', '1'), ('noch', '1'), ('nicht', '1'), ('genau', '1'),
                                          ('астральна', '1'), ('площина', '1'), ('нагадувала', '1'),
                                          ('магніт', '1')]))

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

    def test_part_subtitles_when_num_is_passed(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        part = parser.part_subtitles(group_num='296')
        self.assertListEqual(part, ['...than we could spend', 'in 10 lifetimes.'])

    def test_part_subtitles_when_num_not_in_srt_file(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        part = parser.part_subtitles
        self.assertRaises(parser_exceptions.PartDoesNotExists, part, group_num='58')

    def test_part_subtitles_when_num_is_not_number(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        part = parser.part_subtitles
        self.assertRaises(parser_exceptions.PartDoesNotExists, part, group_num='x')

    def test_part_subtitles_when_time_is_passed(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        part = parser.part_subtitles(time='00:01:17')
        self.assertListEqual(part, ["Mr. White,", "the car's been dealt with, sir."])

    def test_part_subtitles_when_not_existing_time_is_passed(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        part = parser.part_subtitles
        self.assertRaises(parser_exceptions.PartDoesNotExists, part, time='00:11:17')

    def test_part_subtitles_when_wrong_time_format_is_passed(self):
        parser = srt_parser.SrtParser(file=path_to_file)
        part = parser.part_subtitles
        self.assertRaises(ValueError, part, time='00:1211:17')


if __name__ == '__main__':
    unittest.main()
