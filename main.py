from text_analyser import Analysis


def main():
    text = input('Type in your text: ')

    anls_text = Analysis()
    anls_text.setText(text)

    print(f'Number of sentences: {anls_text.getSentences()}')
    print(f'Number of words: {anls_text.getWords()}')
    print(f'Number of syllables: {anls_text.getSyllables()}')
    print(f'Average sentence length: {anls_text.getAsl()}')
    print(f'Average number of syllables per word: {anls_text.getAsw()}')
    print(f'The Flesch Reading Ease Index: {anls_text.getIndex()}')
    print(f'Text tone: {anls_text.getTextTone()}')
    print(f'Objectivity: {anls_text.getObjectivity()}')
    print(f'Result: {anls_text.getResult()}')


if __name__ == '__main__':
    main()


'''
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from deep_translator import GoogleTranslator


def translate(text):
    translated = GoogleTranslator(source='auto', target='en').translate(text)
    return translated

text = input("Input your text: ")

rus_count=0
rus = False
eng_count=0
eng = False
text_mas=[]


TXT = TextBlob(text)
string = str(TXT.word_counts)
words = 0
rus_letters = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
eng_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
others = ["(", ")", "{", "}", "'", ":", "<", ">", ",", ".", "-", " "]
for s in string:
    if s not in rus_letters and s not in eng_letters and s not in others:
        words+=int(s)

sentences = len(TXT.sentences)

for s1 in text:
    if s1.lower() in vowels_rus:
        rus_count+=1
        rus = True
    elif s1.lower() in vowels_eng:
        eng_count+=1
        eng = True
if rus:
    syllables = rus_count
if eng:
    syllables = eng_count

asl = words/sentences

asw = syllables/words

if rus:
    index = 206.835 - (1.3 * asl) - (60.1 * asw) 
if eng:
    index = 206.835 - (1.015 * asl) - (84.6 * asw)

if index > 80:
    value = 'The text reads easily. (For younger students)'

elif 80 >= index > 50:
    value = 'Plain text. (For school children)'

elif 50 >= index > 25:
    value = 'The text is a little hard to read. (For students)'

elif 25 > index:
    value = 'The text is hard to read. (For university graduates)'

tone = TXT.sentiment.polarity

objectivity = 1-(TXT.sentiment.subjectivity)

print(f'Number of sentences: {sentences}')
print(f'Number of words: {words}')
print(f'Number of syllables: {syllables}')
print(f'Average sentence length: {asl}')
print(f'Average number of syllables per word: {asw}')
print(f'The Flesch Reading Ease Index: {index}')
print(value)
print(f'Text tone: {tone}')
print(f'Objectivity: {objectivity*100}%')
#print(f'Result: {result}')


#У нас росла липа. Липа стала стара. Липа стала суха. Липа упала. Пришли папа и Паша. У папы пила. У Паши топорик. Они распилили липу
#And convergence generally worked the way economists long thought it would in. China, low-wage manufacturing of cheap goods for export eventually evolved into the production of more sophisticated goods and services, as workers and firms accumulated knowledge and experience 

'''