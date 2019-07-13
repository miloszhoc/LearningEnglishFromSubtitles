import sys

from utils import words_translator as words_translator

from utils import srt_parser


def create_file(filename, content):
    with open(filename + '.txt', 'a+', encoding='utf-8')as f:
        f.write(content + '\n')


def main(args):
    api_key = '9dcd4058b8ee4bd88b9838bda9a6f890'
    if len(args) == 3:
        if args[1] == '-words':
            parser = srt_parser.SrtParser(args[2])
            words = parser.words_without_repetitions()
            try:
                print('This command supports translation only from or to English!')
                print('Either source language or destination language has to be English')
                print('If source language is different, '
                      'destination language will be automatically set to English\n')
                src = input('what is the subtitles language? ')
                dest = input('what is the destination language? ')
                f_name = input('file name: ')

                trans = words_translator.TranslateWordsMicrosoft(words_list=words,
                                                                 api_key=api_key,
                                                                 src_lang=src,
                                                                 dest_lang=dest)
            except ValueError:
                print('Language Error\nTry to run -lang command to be familiar with supported languages')
                exit()
            else:
                for word, translation in trans.translate_words().items():
                    content = word + '-' + translation
                    create_file(f_name, content)

        elif args[1] == '-wordsFreq':
            parser = srt_parser.SrtParser(args[2])
            src = input('What is the subtitles language? ')
            dest = input('what is the destination language? ')
            while True:
                try:
                    min_len = int(input('Minimal length of each word to translation: '))
                    assert min_len > 0
                except (ValueError, AssertionError):
                    print('Value should be a number\n'
                          'Value should be greater than 0')
                else:
                    break
            while True:
                try:
                    min_occurs = int(input('Minimal word occurs: '))
                    assert min_occurs > 0
                except (ValueError, AssertionError):
                    print('Value should be a number\n'
                          'Value should be greater than 0')
                else:
                    break
            while True:
                sort = input(r'Should the subtitles be sorted ascending '
                             r'or descending (by frequency) [asc\desc]').lower()
                if sort == 'asc' or sort == 'ascending':
                    desc = False
                    break
                elif sort == 'desc' or sort == 'descending':
                    desc = True
                    break
                else:
                    print("Error, unknown input, type 'asc' or 'desc' ")

            f_name = input('file name: ')
            words = parser.words_with_frequency(descending=desc, min_len=min_len, min_occurs=min_occurs)
            try:
                print('This command supports translation only from or to English!')
                trans = words_translator.TranslateWordsMicrosoft(words_list=words,
                                                                 api_key=api_key,
                                                                 src_lang=src,
                                                                 dest_lang=dest)
            except ValueError:
                print('Language Error\nTry to run -lang command to be familiar with supported languages')
                exit()
            else:
                for word, translation in trans.translate_words_with_frequency().items():
                    content = word + '-' + translation[0] + ' (' + translation[1] + ')'
                    create_file(f_name, content)

        elif args[1] == '-all':
            pass
        elif args[1] == '-part':
            print('pick the number of the part of subtitles')
        elif args[1] == '-double':
            pass
        else:
            print('unknown command')

    if len(args) == 2:
        if args[1] == '-lang':
            for k, v in words_translator.TranslateWordsMicrosoft.show_all_languages().items():
                print(k, '-', v)
        else:
            print('unknown command')


if __name__ == '__main__':
    args = sys.argv
    # args = ['lefs.py', r'tests\test_utils\part_to_test.srt']
    # args = ['lefs.py', r'tests\test_utils\iZombie.S05E05.srt']
    if len(args) < 2:
        print('\n\t!!! -words and -wordsFreq commands supports translations only from or to English !!!\n')
        print('Usage:\n \'lefs [command] <arg>\'')

        print('\nCommands:')
        print('-lang\tshows all supported languages with codes (use this without arg)')
        print('-wordsFreq\tcreates file which contains words with translations and how many times it occurs')
        print('-words\tcreates file which contains words with translations')
        print('-all\ttranslate whole subtitles')
        print('-part\ttranslate specific part of subtitles')
        print('-double\t generate a srt file which contains subtitles in both languages')

        print('\nargs:')
        print('<file name>\t .srt file (file with subtitles)')
    else:
        main(args)
