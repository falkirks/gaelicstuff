import sys

import tweepy
from textblob import TextBlob
from polyglot.detect import Detector

auth = tweepy.OAuthHandler("token", "secret")
auth.set_access_token("client", "secret")

api = tweepy.API(auth)


class GaelicStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            det = Detector(status.text, True)
            if det.language.code == "gd" or det.languages[1].code == "gd":  # run local check
                print("double checking..." + str(status.id))
                if TextBlob(status.text).detect_language() == "gd":  # and we send to google to double check
                    print(status.text)
                    with open('tweets', 'a') as f:
                        f.write('\n' + str(status.id))
        except:
            print("error")

    def on_error(self, status_code):
        if status_code == 420:
            print("ERROR 420")
            return False


listen = GaelicStreamListener()
stream = tweepy.Stream(auth=api.auth, listener=listen)
stream.filter(track=['gaelic', 'gàidhlig', 'bheil', 'nach', 'robh', 'gach', 'Chuir', 'chaidh', 'Thainig', 'Nuair', 'Dheanamh', 'aghaidh', 'Biodh', 'Bhiodh'])
