class ParserExceptions(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class PartDoesNotExists(ParserExceptions):
    def __init__(self):
        super().__init__('Requested part of subtitles does not exists')


class WrongFormat(ParserExceptions):
    def __init__(self):
        super().__init__('Wrong format of the file')


class TranslatorExceptions(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message


class LangDoesNotExists(TranslatorExceptions):
    def __init__(self):
        super().__init__('Requested language does not exists')
