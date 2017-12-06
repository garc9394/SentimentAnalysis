import tweepy
import json
import apikeys

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

consumer_key = apikeys.TWITTER_CONSUMER_KEY
consumer_secret = apikeys.TWITTER_CONSUMER_SECRET
access_token = apikeys.TWITTER_ACCESS_TOKEN
access_token_secret = apikeys.TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

target_user = '@nytimes'

# Tweet Texts
tweet_texts = []

# Get all tweets from home feed
public_tweets = api.user_timeline(target_user)

# Loop through all tweets
for tweet in public_tweets:

    # Print Tweet
    print(tweet['text'])

    # Store Tweet in Array
    tweet_texts.append(tweet['text'])

# Print the Tweet Count
# print(f'\nTweet Count: {len(tweet_texts)}')