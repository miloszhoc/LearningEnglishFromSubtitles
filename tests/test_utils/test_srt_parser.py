import unittest
from utils import srt_parser


class TestSrtParser(unittest.TestCase):

    def test_read_srt_file_when_file_exists(self):
        parser = srt_parser.SrtParser(file='part_to_test.srt')
        self.assertTrue(parser.read_srt_file())

    def test_read_srt_file_when_file_doesnt_exists(self):
        parser = srt_parser.SrtParser(file='part.srt')
        self.assertFalse(parser.get_words_from_file())


if __name__ == '__main__':
    unittest.main()
