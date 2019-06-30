import re


class SrtParser:
    def __init__(self, file):
        self._file = file
        self.words_frequency = []

    # generator which reads srt file line by line
    def read_srt_file(self):
        try:
            with open(self._file, 'r') as f:
                for line in f:
                    yield line
        except FileNotFoundError:
            print('File does not exist.\nCheck your path or file name.')
            return False

    # returns all words form file (with repetitions)
    def get_words_from_file(self):
        all_words = []
        pattern_without_num = r"\D"  # get rid of all numbers
        pattern_text = r"[a-zA-Z]+'?[a-zA-Z]+"  # search only for text

        # iterates through lines of file and extends
        # words list by only words from subtitles
        for i in self.read_srt_file():
            if re.match(pattern_without_num, i):
                all_words.extend(re.findall(pattern_text, i.lower()))
        return all_words

    # returns words without repetitions
    def words_without_repetitions(self):
        return list(set(self.get_words_from_file()))

    # returns words with repetitions counter
    def words_with_frequency(self, descending=True, min_len=1, min_occurs=1):
        all_words = self.get_words_from_file()
        temp = set()

        # counts repetitions for every word
        # deletes repetitions
        for i in all_words:
            temp.add((all_words.count(i), i))

        if min_len > 0 and min_occurs > 0:
            # list contains tuples - (word, how many times it occurs)
            for word in sorted(temp, reverse=descending):
                if len(word[1]) >= min_len and word[0] >= min_occurs:
                    self.words_frequency.append((word[1], str(word[0])))
            return self.words_frequency
        else:
            print('Minimal word length can\'t be less or equal 0')
            print('Minimal word frequency can\'t  be less or equal 0')
            return False
