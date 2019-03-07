from textblob import TextBlob
from polyglot.detect import Detector
import os
import re

directory = os.fsencode("data")

tweet_regex = re.compile(r"(^|[^@\w])@(\w{1,15})\b", re.IGNORECASE)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if not os.path.isfile('sorted/en/' + filename):
        print("working on " + filename)
        with open("data/" + filename) as f:
            lines = f.read().splitlines()
        with open('sorted/en/' + filename, 'a') as en:
            with open('sorted/gd/' + filename, 'a') as gd:
                with open('sorted/na/' + filename, 'a') as na:
                    for tweet in lines:
                        tweet = ''.join(x for x in tweet if x.isprintable()) # workaround for bug in lib
                        det = Detector(re.sub(tweet_regex, "", tweet), True)
                        if det.language.code == "gd" or det.languages[1].code == "gd":  # run local check
                            if not det.reliable:
                                na.write(tweet)
                            else:
                                gd.write(tweet + '\n')
                        else:
                            en.write(tweet + '\n')
    else:
        print("skipping " + filename)
