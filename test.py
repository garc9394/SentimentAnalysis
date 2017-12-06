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

newsOrg = ("@BBCNews", "@CBSNews")

for org in newsOrg:
    print(org)

# target_user = "@BBCNews"

# public_tweets = api.user_timeline(target_user, count=25)

# print(len(public_tweets))

# for tweet in public_tweets:
#     print(json.dumps(tweet, sort_keys=True, indent=4))