import os

directory = os.fsencode("data")

num_users = 0
num_tweets = 0

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    with open("data/" + filename) as f:
        lines = f.read().splitlines()
    if len(lines) > 0:
        num_users += 1
    num_tweets += len(lines)

print("users: " + str(num_users))
print("tweets: " + str(num_tweets))
