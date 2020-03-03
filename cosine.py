import nltk
from sklearn.feature_extraction.text import CountVectorizer
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from scipy import spatial

def case_fold(texts):
    ret = [text.lower() for text in texts]
    return ret

def tokenize(texts):
    ret = [nltk.tokenize.word_tokenize(text) for text in texts]
    return ret

def nlp_filter(data):
    factory = StopWordRemoverFactory()
    sw = factory.get_stop_words()
    ret = [[token for token in sentence if not token in sw] for sentence in data]
    return ret

def stem(data):
    stemmer = StemmerFactory()
    smw = stemmer.create_stemmer()
    ret = [[smw.stem(token) for token in sentence] for sentence in data]
    return ret


def preprocess(texts):
    data = case_fold(texts)
    data = tokenize(data)
    data = nlp_filter(data)
    data = stem(data)
    ret = [' '.join(sentence) for sentence in data]
    return ret


def process(texts):
    vectorizer = CountVectorizer()
    vector = vectorizer.fit_transform(texts)
    vector = vector.toarray()
    similarity = 1 - spatial.distance.cosine(vector[0], vector[1])
    return similarity

def calculate_grade(text1, text2, base_grade):
    similarity = process(preprocess([text1, text2]))
    return similarity * base_grade

if __name__ == '__main__':
    text1 = input('masukkan jawaban : ')
    text2 = input('masukkan kunci jawaban : ')
    base_grade = int(input('masukkan bobot : '))
    print(calculate_grade(text1, text2, base_grade))