# -*- coding: utf-8 -*-
import datetime
import re

import chardet
from exceptions import parser_exceptions


class SrtParser:
    # To learn more about .srt files visit: https://en.wikipedia.org/wiki/SubRip

    def __init__(self, file):
        self._file = file

    def detect_encoding(self):
        with open(self._file, 'rb') as f:
            return chardet.detect(f.read())['encoding']

    # generator which reads srt file line by line
    def read_srt_file(self):
        try:
            encoding = self.detect_encoding()
            with open(self._file, 'r', encoding=encoding) as f:
                for line in f:
                    yield line
        except FileNotFoundError:
            print('File does not exist.\nCheck your path or file name.')
            exit()

    # returns all words form file (with repetitions)
    def get_words_from_file(self):
        all_words = []
        pattern_text = r"[^\W\d_]+'?[^\W\d_]+"  # search only for text
        # iterates through lines of file and extends
        # words list by only words from subtitles
        for i in self.read_srt_file():
            all_words.extend(re.findall(pattern_text, i.lower(), re.U))
        if all_words:
            return all_words
        else:
            raise parser_exceptions.EmptyFile

    # returns words without repetitions
    def words_without_repetitions(self):
        return list(set(self.get_words_from_file()))

    # returns words with repetitions counter
    def words_with_frequency(self, descending=True, min_len=1, min_occurs=1):
        if min_len <= 0:
            raise parser_exceptions.LenLessEqualZero
        if min_occurs <= 0:
            raise parser_exceptions.OccursLessEqualZero

        all_words = self.get_words_from_file()
        temp = set()
        words_frequency = []

        for i in all_words:
            temp.add((all_words.count(i), i))

            # list contains tuples - (word, how many times it occurs)
        for word in sorted(temp, reverse=descending):
            if len(word[1]) >= min_len and word[0] >= min_occurs:
                words_frequency.append((word[1], str(word[0])))
        return words_frequency

    # returns only text from specific part of subtitles
    def part_subtitles(self, group_num=None, time=None):
        lines = self.read_srt_file()
        text = []
        # if time is nt passed to function checks by group number
        if not time:
            group_num = str(group_num)
            for line in lines:
                if re.match('{}$'.format(group_num), line):  # if line contains only subtitles number
                    try:
                        while line != '\n':  # reads next line until empty line
                            if re.search(r'[^\W\d_]', line, re.U):
                                text.append(line.rstrip('\n'))
                            line = next(lines)  # updating line
                    except StopIteration:
                        pass
                    finally:
                        return text
            else:
                raise parser_exceptions.PartDoesNotExists
        else:
            time = datetime.datetime.strptime(time, '%H:%M:%S').time()
            for line in lines:
                times = re.findall('\d{2}:\d{2}:\d{2}', line)
                if times:  # checks if times is not empty list
                    time_begin = datetime.datetime.strptime(times[0], '%H:%M:%S').time()
                    time_end = datetime.datetime.strptime(times[1], '%H:%M:%S').time()
                    if time_begin <= time <= time_end:
                        try:
                            while line != '\n':
                                line = next(lines)
                                if line != '\n':
                                    text.append(line.rstrip('\n'))
                        except StopIteration:
                            pass
                        finally:
                            return text
            else:
                raise parser_exceptions.PartDoesNotExists

    # Method reads file line by line until EOF is reached.
    # Checks each line, if line contains any text it will be translated to
    # given language and saved to file.
    # If it doesn't contains any text line will be saved to file.
    # todo: split translated line again into multiple lines

    # todo: entire_subtitles and double_subtitles are the same
    def entire_subtitles(self, func):
        file_line = self.read_srt_file()
        text = []
        try:
            line = next(file_line)  # reads first line in file
            while True:  # runs until EOF
                while line != '\n':  # reads one group in file (until \n occurs)
                    if re.search('[^\W\d_]', line, flags=re.U):
                        text.append(line.rstrip('\n'))
                    else:
                        yield line
                    line = next(file_line)  # updating lines
                if len(text) > 0:
                    translated_line = func(text)
                    yield translated_line + '\n'  # write translated line to file
                yield '\n'  # empty line between groups
                text = []
                line = next(file_line)  # reads line in next group
        except StopIteration:
            translated_line = func(text)
            yield translated_line

    def double_subtitles(self, func):
        file_line = self.read_srt_file()
        text = []
        try:
            line = next(file_line)  # reads first line in file
            while True:  # runs until EOF
                while line != '\n':  # reads one group in file (until \n occurs)
                    if re.search('[^\W\d_]', line, flags=re.U):
                        text.append(line.rstrip('\n'))
                    else:
                        yield line
                    line = next(file_line)  # updating lines
                if len(text) > 0:
                    translated_line = func(text)
                    yield ''.join(text) + '\n' + '\t-' + '\n' + translated_line + '\n'  # write translated line to file
                yield '\n'  # empty line between groups
                text = []
                line = next(file_line)  # reads line in next group
        except StopIteration:
            translated_line = func(text)
            yield ''.join(text) + '\n' + '\t-' + '\n' + translated_line
