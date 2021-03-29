# Importing required modules
import praw
import random
import time

#Bots id, secret, username etc. goes here
reddit = praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    user_agent="USER_AGENT",
    username = "REDDIT_USERNAME",
    password = "REDDIT_PASSWORD")

# Subreddit name goes here
subreddit = reddit.subreddit("SUBREDDIT_NAME")

# You can pick any quotes which you want to reply with. I picked some generic ones.
quotes = ["Hey, im 100% human","Who said anything about bots ?", "Bots have ruined reddit"]

# I set the sleep timer to 1 hour but you can decrease that down to 10 minutes.
# Anything lower than that you will have some problems with spamming.
# You can change "bot" with whatever keyword you are looking for in a comment
for submission in subreddit.hot(limit=10):

    for comment in submission.comments:
        if hasattr(comment,"body"):
            comment_lower = comment.body.lower()
            if " bot " in comment_lower:
                print("----------------------")
                print(comment.body)
                random_index = random.randint(0, len(quotes) - 1)
                comment.reply(quotes[random_index])
                time.sleep(3600)
