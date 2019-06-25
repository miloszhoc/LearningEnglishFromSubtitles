import sys

import lefs.words_translator as words_translator

from lefs.srt_parser import SrtToWords


def main(arg):
    parser = SrtToWords(arg)
    without_freq = parser.words_without_repetitions()
    # with_freq = parser.words_with_frequency()

    trans = words_translator.TranslateMicrosoft(without_freq,
                                                api_key='9dcd4058b8ee4bd88b9838bda9a6f890')
    trans.translate_words()


if __name__ == '__main__':
    args = sys.argv
    # args = 'Breaking Bad - 5x08 - Gliding Over All.srt'
    if len(args) < 2:
        print('Usage:\n \'lefs [command] <arg>\'')
        print('\n Commands:')
        print('-q\t creates file witch words which can be uploaded to quizlet')
        print('-t\t translate dialogues')

        print('\nargs:')
        print('<file name>\t .srt file (subtitles)')
        print()
    else:
        main(args[1])
        # main(args)
