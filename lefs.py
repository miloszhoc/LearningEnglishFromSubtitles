import sys

from utils import words_translator as words_translator

from utils import srt_parser


def main(arg):
    parser = srt_parser.SrtParser(arg)
    without_freq = parser.words_without_repetitions()
    parser.get_words_from_file()
    # with_freq = parser.words_with_frequency()

    trans = words_translator.TranslateMicrosoft(without_freq,
                                                api_key='')
    trans.translate_words()
    print(trans.translated_words)


if __name__ == '__main__':
    args = sys.argv
    # args = 'utils/Breaking Bad - 5x08 - Gliding Over All.srt'
    if len(args) < 2:
        print('Usage:\n \'lefs [command] <arg>\'')
        print('\n Commands:')
        print('-q\t creates file witch words which can be uploaded for example to quizlet.com')
        print('-t\t translate whole subtitles')

        print('\nargs:')
        print('<file name>\t .srt file (file with subtitles)')
        print()
    else:
        main(args[1])
        # main(args)
