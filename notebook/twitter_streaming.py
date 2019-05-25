#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream

import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

env_path = Path('..') / '.env'
print(env_path)
load_dotenv(dotenv_path=env_path)

# Environemnt variables that contains the user credentials to access Twitter API
access_token = os.getenv("Access_token")
access_token_secret = os.getenv("Access_token_secret")
consumer_key = os.getenv("API_key")
consumer_secret = os.getenv("API_secret_key")

# This handles Twitter authetification and the connection to Twitter Streaming API
print(consumer_key, consumer_secret, access_token, access_token_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

try:
    redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
    print('Error! Failed to get request token.')

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


# This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
stream = Stream(auth, l)

# This line filter Twitter Streams to capture data by the keywords: 'GoT'
stream.filter(track=['GameofThrones'])

