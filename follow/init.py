import time
import tweepy
import random

auth = tweepy.OAuthHandler("token", "secret")
auth.set_access_token("client", "secret")

api = tweepy.API(auth)


def add_followers(user_list, user_to_add):
    c = tweepy.Cursor(api.followers_ids, id=user_to_add)
    for page in c.pages():
        user_list.extend(page)
        print(len(user_list))
        time.sleep(20)

users = []
add_followers(users, "BBCRnG")
print("done 1")
add_followers(users, "bbcalba")
print("done 2")
add_followers(users, "bbcnaidheachdan")
print("done 3")

with open('users', 'a') as f:
    for user in users:
        f.write('\n' + str(user))
