import praw
import re
import random

bot_quotes = \
[
" Wow that's great!. ",
" Can't hear you over my spaghetti code",
"Don't you dare touch that. ",
"we have that in home. ",
" you are a funny guy ",
" Nothing to see here.",
"FBI, open up!.",
"Oh, Dear Lord Banana! ",
"Need more JPG ",
" Tell that to 4chan guys ",

]

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("funny")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("coronavirus", comment.body, re.IGNORECASE):
            bot_reply = "Punk_bot says: " + random.choice(bot_quotes)
            comment.reply(bot_reply)
            print(bot_reply)
            