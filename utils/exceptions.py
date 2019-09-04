class ParserExceptions(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class PartDoesNotExists(ParserExceptions):
    def __init__(self):
        super().__init__('Requested part of subtitles does not exists')


class WrongFileFormat(ParserExceptions):
    def __init__(self):
        super().__init__('Wrong format of the file')


class LenLessEqualZero(ParserExceptions):
    def __init__(self):
        super().__init__('Word length should be positive integer')


class OccursLessEqualZero(ParserExceptions):
    def __init__(self):
        super().__init__('Number of word occurrences should be positive integer')


class TranslatorExceptions(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class LangDoesNotExists(TranslatorExceptions):
    def __init__(self):
        super().__init__(
            'Requested language does not exists\nTry to run \'lang\' command to be familiar with supported languages')


class EnglishNotFound(TranslatorExceptions):
    def __init__(self):
        super().__init__('Either source language or destination language has to be English')
