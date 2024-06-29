import tweepy
import os

# Autenticação com as credenciais do Twitter
def authenticate_twitter():
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

# Função para coletar tweets
def collect_tweets(api, query, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count)
    tweet_data = [[tweet.created_at, tweet.user.screen_name, tweet.text] for tweet in tweets]
    return tweet_data
