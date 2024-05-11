import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.stem import PorterStemmer
from textblob import TextBlob


# pip install -r requirements.txt
def preprocessing(text):
    text_token = word_tokenize(text, language="english")
    stopwords_english = stopwords.words("english")
    clean_words = []
    for word in text_token:
        if word not in stopwords_english and word not in punctuation:
            clean_words.append(word)

    stemmer = PorterStemmer()
    stem_words = []
    for word in clean_words:
        stem_word = stemmer.stem(word)
        stem_words.append(stem_word)
    return " ".join(stem_words)


def analyze_sentiment(clean_words):
    textblob = TextBlob(clean_words)
    return textblob.sentiment.polarity, clean_words
