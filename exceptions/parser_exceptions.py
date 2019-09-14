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


class EmptyFile(ParserExceptions):
    def __init__(self):
        super().__init__('File is empty')
