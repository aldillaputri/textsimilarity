#%% nyoba
import time
import nltk
import pprint
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial

def case_folding(x):
    case_fold = x.lower()
    return case_fold

def tokenizing(x):
    case_folding(x)
    tokenized_word = nltk.tokenize.word_tokenize(x)
    return tokenized_word

def filtering(x):
    factory = StopWordRemoverFactory()
    sw = factory.get_stop_words()
    filtered_word = [i for i in x if not i in sw]
    return filtered_word

def stemming(x):
    stemmer = StemmerFactory()
    smw = stemmer.create_stemmer()
    temp = []
    for i in x:
        temp.append(smw.stem(i))
    return temp

def proses_input(text): 
    input = text
    hasil = case_folding(input)
    hasil = tokenizing(hasil)
    hasil = filtering(hasil)
    hasil = stemming(hasil)
    hasil = ' '.join(hasil)
    return [hasil]

def proses_data(text):
    df = pd.read_excel(r'data/data.xlsx')
    data = df.keyword
    data1 = df.overview
    vectorizer = CountVectorizer()
    X = []
    for x,i in enumerate(data):
        hasil = case_folding(i)
        hasil = tokenizing(hasil)
        hasil = filtering(hasil)
        hasil = stemming(hasil)
        hasil = ' '.join(hasil)
        X.append(hasil)
    
    X = vectorizer.fit_transform(X)


    Y = vectorizer.transform(proses_input(text))
    # similarity = np.sum(X.toarray() * Y.toarray(), axis=1)
    similarity = 1 - spatial.distance.cosine(X.toarray(), Y.toarray())

    print(similarity)
    val = np.max(similarity)
    if val>0:
        idx = np.argmax(similarity)
        return data1.iloc[idx], val   
    else:
        return "Maaf saya tidak mengerti maksud anda"
        
if __name__ == '__main__':
    text = input()
    print(*proses_data(text))