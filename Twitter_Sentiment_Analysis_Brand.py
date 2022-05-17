# Import required libraries
import tweepy as tw
import streamlit as st
import pandas as pd
from transformers import pipeline
import tensorflow as tf

# Get authorization to extract tweets
consumer_key = 'zxQklJv949O0M58c90mH0OdZR'
consumer_secret = 'eSjGZX7Z6gVrnq7MFXDTz29n73J4C8fgsxLKgZOo7bngUwMs3a'
access_token = '1157400281094774785-Q41eNXVxH2RIFQwWCAqhXZRK2qmDTp'
access_token_secret = 'fWhXOYPjZx2p5YqltKjIWCixiZOY36R20uJZGlnWG9lKQ'
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# define sentiment analysis using pipeline of hugging face transformers
classifier = pipeline('sentiment-analysis')
st.title('Branding Procurement based on Sentiment Analysis of Tweets')
st.header("Changing the Face of Retail Brand Procurement")
st.subheader('Advanced approach to help procurement process to get in shape for the future')
st.markdown('A tool that surpasses the traditional branding procurement, by deriving the latest tweets from Twitter along with its corresponding Sentiment Analysis based on what is included in the below box.')

# Create the app
def run():
    with st.form(key='Enter name'):
        search_words = st.text_input('Enter the Brand name for which you want to know the tendency')
        number_of_tweets = st.number_input('Enter the number of latest tweets for which you want to know the sentiment (Max 50 tweets)', 0,50,10)
        submit_button = st.form_submit_button(label='Submit')
        if submit_button:
            tweets =tw.Cursor(api.search_tweets,q=search_words,lang="en").items(number_of_tweets)
            tweet_list = [i.text for i in tweets]
            p = [i for i in classifier(tweet_list)]
            q=[p[i]['label'] for i in range(len(p))]
            df = pd.DataFrame(list(zip(tweet_list, q)),columns =['Latest '+str(number_of_tweets)+' Tweets'+' on '+search_words, 'sentiment'])
            st.write(df)

if __name__=="__main__":
        run()

