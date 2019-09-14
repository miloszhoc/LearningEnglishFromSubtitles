import argparse

import requests

from translate_microsoft.modules import language_checker_subtitles, language_checker_words
from translate_microsoft.translator import Translator


def create_file(self, filename, content):
    with open(filename + '.txt', 'a+', encoding='utf-8')as f:
        f.write(content + '\n')


# todo: add progress bar
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

        translate = None
        if 'srt_file' in args:
            translate = Translator(api_key, args.srt_file)
        if args.subparser_name == 'words' or args.subparser_name == 'w':
            translate.translate_words(args.src_lang,
                                      args.dest_lang,
                                      args.out_file)
        if args.subparser_name == 'wordsfreq' or args.subparser_name == 'f':
            translate.translate_wordsfreq(args.src_lang,
                                          args.dest_lang,
                                          args.sort,
                                          args.min_len,
                                          args.min_occurs,
                                          args.out_file)
        if args.subparser_name == 'all' or args.subparser_name == 'a':
            translate.translate_all(args.dest_lang,
                                    args.out_file)
        if args.subparser_name == 'part' or args.subparser_name == 'p':
            translate.translate_part(args.time,
                                     args.group,
                                     args.dest_lang)
        if args.subparser_name == 'double' or args.subparser_name == 'd':
            translate.translate_double(args.dest_lang,
                                       args.out_file)
    except requests.exceptions.ConnectionError:
        print('Check your Internet connection!')


if __name__ == '__main__':
    main()
