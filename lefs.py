import argparse

import requests

from translate_microsoft import words_translator as words_translator
from translate_microsoft import language_checker_subtitles
from translate_microsoft import language_checker_words
from translate_microsoft import subtitles_translator
from utils import exceptions, srt_parser


def create_file(filename, content):
    with open(filename + '.txt', 'a+', encoding='utf-8')as f:
        f.write(content + '\n')


def main():
    api_key = '9dcd4058b8ee4bd88b9838bda9a6f890'
    parser = argparse.ArgumentParser(prog='lefs',
                                     description="Program translates words from subtitles or whole .srt file.")
    subparsers = parser.add_subparsers(help='sub-command help', dest='subparser_name')

    # languages
    parser_lang = subparsers.add_parser('lang',
                                        aliases=['l'],
                                        help='shows all supported languages and codes')
    parser_lang.add_argument('-w',
                             action='store_true',
                             help='shows all supported languages and codes for subtitles translation '
                                  '(for \'words\', and \'wordsfreq\' command)')
    parser_lang.add_argument('-t',
                             action='store_true',
                             help='shows all supported languages and codes for subtitles translation '
                                  '(for \'all\', \'part\' and \'double\' command)')

    # words command
    parser_words = subparsers.add_parser('words',
                                         aliases=['w'],
                                         help='Creates file which contains words with translations.\n'
                                              'Function supports translations only from or to English!')
    parser_words.add_argument('srt_file',
                              type=str,
                              help='file in .srt format',
                              action='store')
    parser_words.add_argument('src_lang',
                              type=str,
                              help='source language',
                              action='store')
    parser_words.add_argument('dest_lang',
                              type=str,
                              help='destination language',
                              action='store')
    parser_words.add_argument('out_file',
                              type=str,
                              help='output file name (without extension)',
                              action='store')

    # words with frequency command
    parser_freq = subparsers.add_parser('wordsfreq',
                                        aliases=['f'],
                                        help='creates file which contains words with translations and how many times each word occurs', )
    parser_freq.add_argument('srt_file',
                             type=str,
                             help='File in .srt format',
                             action='store')
    parser_freq.add_argument('src_lang',
                             type=str,
                             help='source language',
                             action='store')
    parser_freq.add_argument('dest_lang',
                             type=str,
                             help='destination language',
                             action='store')
    parser_freq.add_argument('min_len',
                             type=int,
                             help='minimal word length',
                             action='store')
    parser_freq.add_argument('min_occurs',
                             type=int,
                             help='minimal word occurs',
                             action='store')
    parser_freq.add_argument('sort',
                             type=str,
                             help='sorting (by frequency) [asc/desc]',
                             action='store',
                             choices=('asc', 'desc'))
    parser_freq.add_argument('out_file',
                             type=str,
                             help='output file name (without extension)',
                             action='store')

    # all command
    parser_all = subparsers.add_parser('all',
                                       aliases=['a'],
                                       help='translates whole subtitles')
    parser_all.add_argument('srt_file',
                            type=str,
                            help='file in .srt format')
    parser_all.add_argument('dest_lang',
                            type=str,
                            help='destination language')
    parser_all.add_argument('out_file',
                            type=str,
                            help='output file name (without extension)')

    # part command
    parser_part = subparsers.add_parser('part',
                                        aliases=['p'],
                                        help='translate specific part of subtitles')
    parser_part.add_argument('srt_file',
                             type=str,
                             help='file in .srt format')
    parser_part.add_argument('dest_lang',
                             type=str,
                             help='destination language')
    parser_part.add_argument('-t', '--time',
                             type=str,
                             nargs=3,
                             help='show by time')
    parser_part.add_argument('-g', '--group',
                             type=int,
                             help='show by group number')
    parser_part.add_argument('out_file',
                             type=str,
                             help='output file name (without extension)')

    # double command
    parser_double = subparsers.add_parser('double',
                                          aliases=['d'],
                                          help='generates a .srt file which contains subtitles in both languages')
    parser_double.add_argument('srt_file',
                               type=str,
                               help='file in .srt format')
    parser_double.add_argument('dest_lang',
                               type=str,
                               help='destination language')
    parser_double.add_argument('out_file',
                               type=str,
                               help='output file name (without extension)')

    args = parser.parse_args()

    try:
        if 'w' in args and args.w is True:
            langs = language_checker_words.CheckLanguageWords()
            for k, v in langs.show_all_languages_dictionary().items():
                print(k, '-', v)
        if 't' in args and args.t is True:
            langs = language_checker_subtitles.CheckLanguageSubtitles()
            for k, v in langs.show_all_languages_translation().items():
                print(k, '-', v)
        if args.subparser_name == 'words' or args.subparser_name == 'w':
            print('This command supports translation only from or to English!')
            try:
                subtitles_parser = srt_parser.SrtParser(args.srt_file)
                words = subtitles_parser.words_without_repetitions()

                check_lang = language_checker_words.CheckLanguageWords()
                lang_dict = check_lang.check_lang_dictionary(args.src_lang, args.dest_lang)

                trans = words_translator.TranslateWordsMicrosoft(words_list=words,
                                                                 api_key=api_key,
                                                                 src_lang=lang_dict['src'],
                                                                 dest_lang=lang_dict['dest'])
            except (exceptions.LangDoesNotExists, exceptions.EnglishNotFound) as e:
                print(e.message)
            else:
                print('Translation in progress...')
                for word, translation in trans.translate_words().items():
                    content = word + '-' + translation
                    create_file(args.out_file, content)
                print('All translated!')
        if args.subparser_name == 'wordsfreq' or args.subparser_name == 'f':
            print('This command supports translation only from or to English!')

            try:
                subtitles_parser = srt_parser.SrtParser(args.srt_file)

                check_lang = language_checker_words.CheckLanguageWords()
                lang_dict = check_lang.check_lang_dictionary(args.src_lang, args.dest_lang)

                words = subtitles_parser.words_with_frequency(descending=True if args.sort == 'desc' else False,
                                                              min_len=args.min_len,
                                                              min_occurs=args.min_occurs)
                trans = words_translator.TranslateWordsMicrosoft(words_list=words,
                                                                 api_key=api_key,
                                                                 src_lang=lang_dict['src'],
                                                                 dest_lang=lang_dict['dest'])
            except (exceptions.LangDoesNotExists, exceptions.LenLessEqualZero,
                    exceptions.OccursLessEqualZero, exceptions.EnglishNotFound) as e:
                print(e.message)
            else:
                print('Translation in progress...')
                for word, translation in trans.translate_words_with_frequency().items():
                    content = word + '-' + translation[0] + ' (' + translation[1] + ')'
                    create_file(args.out_file, content)
                print('All translated!')
        if args.subparser_name == 'all' or args.subparser_name == 'a':
            subtitles_parser = srt_parser.SrtParser(args.srt_file)
            try:
                check_lang = language_checker_subtitles.CheckLanguageSubtitles()
                dest_lang = check_lang.check_lang_translation(args.dest_lang)

                s_t = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, dest_lang=dest_lang)
            except exceptions.LangDoesNotExists as e:
                print(e.message)
            else:
                print('\nTranslation in progress...')
                for line in subtitles_parser.entire_subtitles(s_t.translate):
                    with open(args.out_file + '.srt', 'a+', encoding='utf-8') as f:
                        f.write(line)
                print('All translated')
        if args.subparser_name == 'part' or args.subparser_name == 'p':
            subtitles_parser = srt_parser.SrtParser(args.srt_file)
            part = None
            if args.time is not None:
                time = ':'.join(args.time)
                try:
                    part = subtitles_parser.part_subtitles(time=time)
                except ValueError:
                    print('Wrong time format')
                except exceptions.PartDoesNotExists as e:
                    print(e.message)
            elif args.group is not None:
                try:
                    part = subtitles_parser.part_subtitles(group_num=args.group)
                except exceptions.PartDoesNotExists as e:
                    print(e.message)
            try:
                check_lang = language_checker_subtitles.CheckLanguageSubtitles()
                dest_lang = check_lang.check_lang_translation(args.dest_lang)

                trans = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, dest_lang=dest_lang)
            except exceptions.LangDoesNotExists as e:
                print(e.message)
            else:
                translated = trans.translate(part)
                print(translated)
        if args.subparser_name == 'double' or args.subparser_name == 'd':
            subtitles_parser = srt_parser.SrtParser(args.srt_file)
            try:
                check_lang = language_checker_subtitles.CheckLanguageSubtitles()
                dest_lang = check_lang.check_lang_translation(args.dest_lang)

                s_t = subtitles_translator.SubtitlesTranslatorMicrosoft(api_key, dest_lang=dest_lang)
            except exceptions.LangDoesNotExists as e:
                print(e.message)
            else:
                print('\nTranslation in progress...')
                for line in subtitles_parser.double_subtitles(s_t.translate):
                    with open(args.out_file + '.srt', 'a+', encoding='utf-8') as f:
                        f.write(line)
                print('All translated')

    except requests.exceptions.ConnectionError:
        print('Check your Internet connection!')


if __name__ == '__main__':
    main()
