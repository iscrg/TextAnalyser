'''
Popov Ivan 80%
Fisher Daniil 65%
Fedyakin Dmitry 70%
'''

from text_analyser import Analysis


def main():
    text = input('Type in your text: ')

    anls_text = Analysis()
    anls_text.set_text(text)

    print(f'Number of sentences: {anls_text.get_sentences()}')
    print(f'Number of words: {anls_text.get_words()}')
    print(f'Number of syllables: {anls_text.get_syllables()}')
    print(f'Average sentence length: {anls_text.get_asl()}')
    print(f'Average number of syllables per word: {anls_text.get_asw()}')
    print(f'The Flesch Reading Ease Index: {anls_text.get_index()}')
    print(f'Text tone: {anls_text.get_text_tone()}')
    print(f'Objectivity: {anls_text.get_objectivity()}')
    print(f'Result: {anls_text.get_result()}')


if __name__ == '__main__':
    main()
