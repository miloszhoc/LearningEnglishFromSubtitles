import sys

from utils import words_translator as words_translator

from utils import srt_parser


def main(args):
    # lefs [command] <arg>

    # parser = srt_parser.SrtParser(args[2])
    # without_freq = parser.words_without_repetitions()
    # trans = words_translator.TranslateMicrosoft(without_freq,
    #                                             api_key='')

    if len(args) == 3:
        if args[1] == '-q':
            print('Pick the number of subtitles source')
            # 1 African (af)
            # 2 English (en)
            # user input
            print('Pick the number of subtitles language destination')

        elif args[1] == '-t_all':
            pass
        elif args[1] == '-t_part':
            print('pick the  of dialogue')
        else:
            print('unknown command')
    if len(args) == 2:
        if args[1] == '-lang':
            for k, v in words_translator.TranslateMicrosoft.show_all_languages().items():
                print(k, '-', v)
        else:
            print('unknown command')
    # trans.translate_words()
    # print(trans.translated_words)


# args = r'tests\test_utils\part_to_test.srt'
if __name__ == '__main__':
    args = sys.argv
    # args = ['lefs.py', '-lang']
    if len(args) < 2:
        print('Usage:\n \'lefs [command] <arg>\'')

        print('\nCommands:')
        print('-lang\tshows all supported languages (with codes)')
        print('-q\tcreates file with words following by translations(which can be uploaded for example to quizlet.com)')
        print('-t_all\ttranslate whole subtitles')
        print('-t_part\ttranslate specific part of subtitles')

        print('\nargs:')
        print('<file name>\t .srt file (file with subtitles)')
    else:
        main(args)
