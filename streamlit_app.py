import streamlit as st
import sentiment

analyze = False
st.title("Introduction to Sentiment Analysis")

user_input = st.text_area(label="Enter some text", height=150)
col1, col2 = st.columns(2)

with col1:
    if st.button("Analyze", use_container_width=True, type="primary"):
        clean_word = sentiment.preprocessing(user_input)
        score = sentiment.analyze_sentiment(clean_word)
        analyze = True
        st.write(sentiment.anso(clean_word))

with col2:
    if st.button("Clear", use_container_width=True, type="secondary"):
        analyze = False

if analyze:
    con = st.container()
    if score > 0:
        st.header("Sentiment: :green[Positive]")
    elif score < 0:
        st.header("Sentiment: :red[Negative]")
    else:
        st.header("Sentiment: :grey[Neutral]")
    st.subheader(f"Score: {round(score, 2)}")
