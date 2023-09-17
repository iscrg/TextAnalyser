import string
from textblob import TextBlob


class Analysis:
    def __init__(self):
        self.__text = None

        self.__language = None
        self.__sentences = None
        self.__words = None
        self.__syllables = None
        self.__asl = None
        self.__asw = None
        self.__index = None
        self.__textTone = None
        self.__objectivity = None
        self.__result = None

    def __sentencesHandler(self):
        self.__sentences = None

    def __wordsSentencesHandler(self):
        marks = ['.', '?', '!']

        wordsCounter = 0
        sentencesCounter = 0

        for i in range(len(self.__text) - 1):
            if (self.__text[i] in string.whitespace and
                    self.__text[i + 1] not in string.whitespace):
                wordsCounter += 1

            elif self.__text[i] in marks and self.__text[i + 1] not in marks:
                sentencesCounter += 1

            else:
                pass

        if sentencesCounter == 0:
            sentencesCounter = 1
        wordsCounter += 1

        self.__words = wordsCounter
        self.__sentences = sentencesCounter

    def __syllablesHandler(self):
        rusVowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
        engVowels = ['a', 'e', 'i', 'o', 'u', 'y']
        rusCounter = 0
        engCounter = 0

        for letter in self.__text:
            if letter.lower() in rusVowels:
                rusCounter += 1
            elif letter.lower() in engVowels:
                engCounter += 1

        if rusCounter > engCounter:
            self.__language = 'rus'
            self.__syllables = rusCounter
        else:
            self.__language = 'eng'
            self.__syllables = engCounter

    def __aslHandler(self):
        self.__asl = self.__words / self.__sentences

    def __aswHandler(self):
        self.__asw = self.__syllables / self.__words

    def __indexHandler(self):
        if self.__language == 'rus':
            self.__index = 206.835 - (1.3 * self.__asl) - (60.1 * self.__asw)
        if self.__language:
            self.__index = 206.835 - (1.015 * self.__asl) - (84.6 * self.__asw)

    def __textToneHandler(self):
        self.__textTone = None

    def __objectivityHandler(self):
        emotion = TextBlob(self.__text)
        self.__objectivity = emotion.sentiment

    def __resultHandler(self):
        index = self.__index

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

        self.__result = value

    def setText(self, txt):
        self.__text = txt

        self.__sentencesHandler()
        self.__wordsSentencesHandler()
        self.__syllablesHandler()
        self.__aslHandler()
        self.__aswHandler()
        self.__indexHandler()
        self.__textToneHandler()
        self.__objectivityHandler()
        self.__resultHandler()

    def getSentences(self):
        return self.__sentences

    def getWords(self):
        return self.__words

    def getSyllables(self):
        return self.__syllables

    def getAsl(self):
        return self.__asl

    def getAsw(self):
        return self.__index

    def getIndex(self):
        return self.__index

    def getObjectivity(self):
        return self.__objectivity

    def getTextTone(self):
        return self.__textTone

    def getResult(self):
        return self.__result
