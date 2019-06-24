# aplikacja pobiera z pliku srt slowka bez powtorzen
# sortowanie wg najczesciej wystepujacych (for i in slowa: slowa.count(i)), usuwanie powtorzen po tym
# przepuszcza przez api google translator, lub (BeautifulSoup + bab.la w formie scrappera, pobiera definicje)
# i zapiuje do pliku w formie slowko-definicja (+ ile razy zostalo powtorzone w napisach)
#

# druga apka pobiera dane i dziala na zasadzie quizletu, gdzie uzytkownik moze sie sprawdzic
import sys

import words_translator

from srt_parser import SrtToWords


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
        print('-t\t tlumaczy cale kwestie (dialogi)')

        print('\nargs:')
        print('<file name>\t file with subtitles (srt)')
        print()
    else:
        main(args[1])
        # main(args)
