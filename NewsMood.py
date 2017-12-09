import tweepy
import json
import apikeys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

consumer_key = apikeys.TWITTER_CONSUMER_KEY
consumer_secret = apikeys.TWITTER_CONSUMER_SECRET
access_token = apikeys.TWITTER_ACCESS_TOKEN
access_token_secret = apikeys.TWITTER_ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# newsOrg = ("@BBCNews", "@CBSNews", "@CNN", "@FoxNews", "@nytimes")
newsOrg = ("@BBCNews", "@CBSNews")
sentiment_df = pd.DataFrame()
x = {}

for org in newsOrg:
    # compound_list = [org.replace("@", "")]
    compound_list = []
    # oldest_tweet = ""
    # public_tweets = api.search(org, count=5, result_type="recent", max_id=oldest_tweet)
    public_tweets = api.search(org, count=5, result_type="recent")

    for tweet in public_tweets["statuses"]:
        text = tweet['text']
        scores = analyzer.polarity_scores(text)
        compound = scores['compound']

        compound_list.append(compound)

        for x in compound_list:
            x = x
            y = compound_list[0]

        plt.plot(x, y)

        # plt.scatter(temp, sales, marker=\"o\",\n",
        #             facecolors=\"red\", edgecolors=\"black\")

    # print(compound_list)
    # sentiment_df = sentiment_df.append({org.replace("@", ""):compound_list}, ignore_index=True)
    sentiment_df = sentiment_df.append([compound_list], ignore_index=True)
        # oldest_tweet = tweet['id_str']

# compound_mean = np.mean(compound_list)
# print(compound_list)
# print(sentiment_df)
plt.show()