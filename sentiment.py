from math import e
import streamlit as st
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


# pip install -r requirements.txt
def preprocessing(text):
    text_token = word_tokenize(text, language="english")
    stopwords_english = stopwords.words("english")
    clean_words = []
    for word in text_token:
        if word not in stopwords_english and word not in punctuation:
            clean_words.append(word)

    lemmatizer = WordNetLemmatizer()
    lemmatize_words = []
    for word in clean_words:
        lematize_word = lemmatizer.lemmatize(word)
        lemmatize_words.append(lematize_word)
    return " ".join(lemmatize_words)


def analyze_sentiment(clean_words):
    textblob = TextBlob(clean_words)
    score = textblob.sentiment.polarity
    return score


def anso(clean_words):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(clean_words)
