import tweepy
import os


auth = tweepy.OAuthHandler("token", "secret")
auth.set_access_token("client", "secret")

api = tweepy.API(auth)

with open('users') as f:
    lines = f.read().splitlines()

for uid in lines:
    if not os.path.isfile('data/' + str(uid)):
        print('working on ' + str(uid))
        try:
            with open('data/' + str(uid), 'a') as f:
                for status in tweepy.Cursor(api.user_timeline, user_id=uid, tweet_mode="extended", wait_on_rate_limit=True, wait_on_rate_limit_notify=True).items():
                    f.write('\n' + status.full_text.replace('\n', ''))
        except tweepy.TweepError as e:
            print("other error, skipping this user")

    else:
        print('skipping ' + str(uid))
