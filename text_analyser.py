import string
from textblob import TextBlob
from deep_translator import GoogleTranslator


class Analysis:
    def __init__(self):
        self.__text = None
        self.__text_translated = None

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

    def __translate(self):
        self.__text_translated = GoogleTranslator(source='auto', target='en').translate(self.__text)

    def __sentences_handler(self):
        self.__sentences = None

    def __words_sentences_handler(self):
        marks = ['.', '?', '!']

        words_counter = 0
        sentences_counter = 0

        for i in range(len(self.__text) - 1):
            if (self.__text[i] in string.whitespace and
                    self.__text[i + 1] not in string.whitespace):
                words_counter += 1

            elif self.__text[i] in marks and self.__text[i + 1] not in marks:
                sentences_counter += 1

            else:
                pass

        if sentences_counter == 0:
            sentences_counter = 1
        words_counter += 1

        if self.__text[-1] in marks:
            sentences_counter += 1

        self.__words = words_counter
        self.__sentences = sentences_counter

    def __syllables_handler(self):
        rus_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
        eng_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
        rus_counter = 0
        eng_counter = 0

        for letter in self.__text:
            if letter.lower() in rus_vowels:
                rus_counter += 1
            elif letter.lower() in eng_vowels:
                eng_counter += 1

        if rus_counter > eng_counter:
            self.__language = 'rus'
            self.__syllables = rus_counter
        else:
            self.__language = 'eng'
            self.__syllables = eng_counter

    def __asl_handler(self):
        self.__asl = self.__words / self.__sentences

    def __asw_handler(self):
        self.__asw = self.__syllables / self.__words

    def __index_handler(self):
        if self.__language == 'rus':
            self.__index = 206.835 - (1.3 * self.__asl) - (60.1 * self.__asw)
        elif self.__language == 'eng':
            self.__index = 206.835 - (1.015 * self.__asl) - (84.6 * self.__asw)

    def __text_tone_handler(self):
        emotion = TextBlob(self.__text_translated)
        emotion_index = emotion.sentiment.polarity
        if emotion_index > (1 / 3):
            self.__textTone = 'positive'
        elif -(1 / 3) <= emotion_index <= (1 / 3):
            self.__textTone = 'neutral'
        else:
            self.__textTone = 'negative'

    def __objectivity_handler(self):
        emotion = TextBlob(self.__text_translated)
        self.__objectivity = f'{round((1 - emotion.sentiment.subjectivity)*100, 1)}%'

    def __result_handler(self):
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

    def set_text(self, txt):
        self.__text = txt

        self.__translate()
        self.__sentences_handler()
        self.__words_sentences_handler()
        self.__syllables_handler()
        self.__asl_handler()
        self.__asw_handler()
        self.__index_handler()
        self.__text_tone_handler()
        self.__objectivity_handler()
        self.__result_handler()

    def get_sentences(self):
        return self.__sentences

    def get_words(self):
        return self.__words

    def get_syllables(self):
        return self.__syllables

    def get_asl(self):
        return self.__asl

    def get_asw(self):
        return self.__asw

    def get_index(self):
        return self.__index

    def get_objectivity(self):
        return self.__objectivity

    def get_text_tone(self):
        return self.__textTone

    def get_result(self):
        return self.__result
