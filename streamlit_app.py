import streamlit as st
import sentiment


# import numpy as np
# from sklearn.datasets import make_regression
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
remarks = 0
processed_word = ""
st.title("Introduction to Sentiment Analysis")
# sentiment_analyzer.preprocessing("hello world bruh")
user_input = st.text_area(label="Enter some text", height=150)
col1, col2 = st.columns(2)
with col1:
    if st.button("Analyze", use_container_width=True, type="primary"):
        clean_word = sentiment.preprocessing(user_input)
        remarks, processed_word = sentiment.analyze_sentiment(clean_word)

with col2:
    if st.button("Clear", use_container_width=True, type="secondary"):
        remarks = 0


if remarks > 0:
    st.header(":green[Positive]")
elif remarks < 0:
    st.header(":red[Negative]")
elif remarks == 0:
    st.header(":grey[Neutral]")
