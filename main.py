from textblob import TextBlob
from deep_translator import GoogleTranslator


def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated


class Analysis:
    def __init__(self, txt):
        self.text = txt
        self.translated = translate(txt)

        self.sentences = None
        self.words = None
        self.syllables = None
        self.asl = None
        self.asw = None
        self.index = None
        self.textTone = None
        self.objectivity = None
        self.result = None

    def sentencesHandler(self):
        self.sentences = None

    def wordsHandler(self):
        self.words = None

    def syllablesHandler(self):
        self.syllables = None

    def aslHandler(self):
        # Average sentence length

        self.asl = None

    def aswHandler(self):
        # Average number of syllables per word

        self.asw = None

    def indexHandler(self):
        self.index = None

    def textToneHandler(self):
        self.textTone = None

    def objectivityHandler(self):
        self.objectivity = None

    def resultHandler(self):
        index = self.index

        if index is None:
            value = 'Error! The index was not calculated.'

        elif index > 80:
            value = 'The text reads easily. (For younger students)'

        elif 80 >= index > 50:
            value = 'Plain text. (For school children)'

        elif 50 >= index > 25:
            value = 'The text is a little hard to read. (For students)'

        elif 25 > index:
            value = 'The text is hard to read. (For university graduates)'

        else:
            value = 'Error! Incorrect value.'

        self.result = value

    def mainHandler(self):
        self.sentencesHandler()
        self.wordsHandler()
        self.syllablesHandler()
        self.aslHandler()
        self.aswHandler()
        self.indexHandler()
        self.textToneHandler()
        self.objectivityHandler()
        self.resultHandler()


def main():
    text = input('Type in your text: ')

    anls_text = Analysis(text)
    anls_text.mainHandler()

    print(f'Number of sentences: {anls_text.sentences}')
    print(f'Number of words: {anls_text.words}')
    print(f'Number of syllables: {anls_text.syllables}')
    print(f'Average sentence length: {anls_text.asl}')
    print(f'Average number of syllables per word: {anls_text.asw}')
    print(f'The Flesch Reading Ease Index: {anls_text.index}')
    print(f'Text tone: {anls_text.index}')
    print(f'Objectivity: {anls_text.objectivity}')
    print(f'Result: {anls_text.result}')


if __name__ == '__main__':
    main()
