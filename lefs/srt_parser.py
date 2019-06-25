import re


class SrtToWords:
    def __init__(self, arg):
        self._file = arg
        self.all_words = []
        self.words_frequency = []

    # generator which reads srt file line by line
    def read_srt_file(self):
        with open(self._file, 'r') as f:
            for line in f:
                yield line

    def get_words_from_file(self):
        pattern_without_num = r"[^0-9]"  # getting rid of numbers at the beginning (eg. time)
        # pattern_text = r"\w+'?\w+"  # takes only text
        pattern_text = r"[a-zA-Z]+'?[a-zA-Z]+"  # takes only text

        # iterates through lines of file and extends
        # words list by only words from subtitles
        for i in self.read_srt_file():
            if re.match(pattern_without_num, i):
                self.all_words.extend(re.findall(pattern_text, i.lower()))
        return self.all_words

    def words_without_repetitions(self):
        return list(set(self.all_words))

    def words_with_frequency(self, descending=True, min_len=1):

        all_words = self.get_words_from_file()
        temp = set()

        # counts repetitions
        for i in all_words:
            temp.add((all_words.count(i), i))

        # list contains tuple - (word, how many times it occurs)
        for i in sorted(temp, reverse=descending):
            if len(i[1]) >= min_len:
                self.words_frequency.append((i[1], str(i[0])))

        return self.words_frequency
