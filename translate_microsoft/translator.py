from translate_microsoft.modules import language_checker_subtitles, language_checker_words, \
    subtitles_translator, words_translator as words_translator
from subtitles_parser import srt_parser
from exceptions import parser_exceptions
from exceptions import translator_exceptions


class Translator:
    def __init__(self, api_key, srt_file):
        self.api_key = api_key
        self.subtitles_parser = srt_parser.SrtParser(srt_file)

    def _create_file(self, filename, content):
        with open(filename + '.txt', 'a+', encoding='utf-8')as f:
            f.write(content + '\n')

    def translate_words(self, src_lang, dest_lang, out_file):
        print('This command supports translation only from or to English!')
        try:
            words = self.subtitles_parser.words_without_repetitions()

            check_lang = language_checker_words.CheckLanguageWords()
            lang_dict = check_lang.check_lang_dictionary(src_lang, dest_lang)

            trans = words_translator.TranslateWordsMicrosoft(words_list=words,
                                                             api_key=self.api_key,
                                                             src_lang=lang_dict['src'],
                                                             dest_lang=lang_dict['dest'])
        except (translator_exceptions.LangDoesNotExists, translator_exceptions.EnglishNotFound) as e:
            print(e.message)
        else:
            print('Translation in progress...')
            for word, translation in trans.translate_words().items():
                content = word + '-' + translation
                self._create_file(out_file, content)
            print('All translated!')

    def translate_wordsfreq(self, src_lang, dest_lang, sort, min_len, min_occurs, out_file):
        print('This command supports translation only from or to English!')
        try:
            check_lang = language_checker_words.CheckLanguageWords()
            lang_dict = check_lang.check_lang_dictionary(src_lang, dest_lang)

            words = self.subtitles_parser.words_with_frequency(descending=True if sort == 'desc' else False,
                                                               min_len=min_len,
                                                               min_occurs=min_occurs)
            trans = words_translator.TranslateWordsMicrosoft(words_list=words,
                                                             api_key=self.api_key,
                                                             src_lang=lang_dict['src'],
                                                             dest_lang=lang_dict['dest'])
        except (translator_exceptions.LangDoesNotExists, parser_exceptions.LenLessEqualZero,
                parser_exceptions.OccursLessEqualZero, translator_exceptions.EnglishNotFound) as e:
            print(e.message)
        else:
            print('Translation in progress...')
            for word, translation in trans.translate_words_with_frequency().items():
                content = word + '-' + translation[0] + ' (' + translation[1] + ')'
                self._create_file(out_file, content)
            print('All translated!')

    def translate_all(self, dest_lang, out_file):
        try:
            check_lang = language_checker_subtitles.CheckLanguageSubtitles()
            dest_lang = check_lang.check_lang_translation(dest_lang)

            s_t = subtitles_translator.SubtitlesTranslatorMicrosoft(self.api_key, dest_lang=dest_lang)
        except translator_exceptions.LangDoesNotExists as e:
            print(e.message)
        else:
            print('\nTranslation in progress...')
            for line in self.subtitles_parser.entire_subtitles(s_t.translate):
                with open(out_file + '.srt', 'a+', encoding='utf-8') as f:
                    f.write(line)
            print('All translated')

    def translate_part(self, time, group, dest_lang):
        part = None
        if (time is None and group is None) or (time is not None and group is not None):
            print('You have to specify either time or group')
            exit()
        elif time is not None:
            time = ':'.join(time)
            try:
                part = self.subtitles_parser.part_subtitles(time=time)
            except ValueError:
                print('Wrong time format')
            except parser_exceptions.PartDoesNotExists as e:
                print(e.message)
        elif group is not None:
            try:
                part = self.subtitles_parser.part_subtitles(group_num=group)
            except parser_exceptions.PartDoesNotExists as e:
                print(e.message)
        try:
            check_lang = language_checker_subtitles.CheckLanguageSubtitles()
            dest_lang = check_lang.check_lang_translation(dest_lang)

            trans = subtitles_translator.SubtitlesTranslatorMicrosoft(self.api_key, dest_lang=dest_lang)
        except translator_exceptions.LangDoesNotExists as e:
            print(e.message)
        else:
            translated = trans.translate(part)
            print(translated)

    def translate_double(self, dest_lang, out_file):
        try:
            check_lang = language_checker_subtitles.CheckLanguageSubtitles()
            dest_lang = check_lang.check_lang_translation(dest_lang)

            s_t = subtitles_translator.SubtitlesTranslatorMicrosoft(self.api_key, dest_lang=dest_lang)
        except translator_exceptions.LangDoesNotExists as e:
            print(e.message)
        else:
            print('\nTranslation in progress...')
            for line in self.subtitles_parser.double_subtitles(s_t.translate):
                with open(out_file + '.srt', 'a+', encoding='utf-8') as f:
                    f.write(line)
            print('All translated')
