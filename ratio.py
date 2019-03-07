import sys

import tweepy
from textblob import TextBlob
from polyglot.detect import Detector

auth = tweepy.OAuthHandler("token", "secret")
auth.set_access_token("client", "secret")

api = tweepy.API(auth)

global gd, en
gd = 0
en = 0


class GaelicStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        if "gàidhlig" in status.text:
            gd += 1
            print("gd")
        if "gaelic" in status.text:
            en += 1
            print("en")

    def on_error(self, status_code):
        if status_code == 420:
            print("ERROR 420")
            return False


listen = GaelicStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=listen)
stream.filter(track=['gaelic', 'gàidhlig'])
