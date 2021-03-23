#!/usr/bin/python3
import logging
import os
import sys
import time

import praw

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

# https://github.com/reddit-archive/reddit/wiki/API
# https://github.com/reddit-archive/reddit/wiki/OAuth2

REDDIT_API_CLIENT_ID = os.environ['REDDIT_API_CLIENT_ID']
REDDIT_API_CLIENT_SECRET = os.environ['REDDIT_API_CLIENT_SECRET']
REDDIT_API_CLIENT_USER_AGENT = os.environ['REDDIT_API_CLIENT_USER_AGENT']

# https://praw.readthedocs.io/en/v7.2.0/getting_started/quick_start.html#read-only-reddit-instances
reddit = praw.Reddit(
	client_id=REDDIT_API_CLIENT_ID,
	client_secret=REDDIT_API_CLIENT_SECRET,
	user_agent=REDDIT_API_CLIENT_USER_AGENT
)

logging.debug('Connected to Reddit as read only? ' + str(reddit.read_only))

SFW_SUBREDDITS = [
	'ProgrammerHumor',  # code-review
	'linuxmasterrace',  # linux-guru
	'memes',  # meme-spew
	'TikTokCringe',  # meme-spew
	'funny'  # meme-spew
]

REDDIT_URL = 'https://reddit.com/'

for subreddit in SFW_SUBREDDITS:
	logging.debug('Processing safe for work sub-reddits.')
	# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/subreddit.html?highlight=top#praw.models.Subreddit.top
	for submission in reddit.subreddit(subreddit).top("day", limit=3):
		# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/submission.html?highlight=submission#praw.models.Submission
		print(submission.title)
		print(REDDIT_URL + submission.permalink)
		print(submission.url)
	# TODO write logic to post into #code-review, #meme-spew, and #linux-guru

NSFW_SUBREDDITS = [
	'AsianCumSluts',
	'AsianPornIn1Minute',
	'AsianBlowjobs',
	'AsiansGoneWild',
	'nextdoorasians'
]

for subreddit in NSFW_SUBREDDITS:
	logging.debug('Processing not safe for work sub-reddits.')
	# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/subreddit.html?highlight=top#praw.models.Subreddit.top
	for submission in reddit.subreddit(subreddit).top("day", limit=3):
		# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/submission.html?highlight=submission#praw.models.Submission
		print(submission.title)
		print(REDDIT_URL + submission.permalink)
		print(submission.url)
# TODO write logic to post into #nsfw-view
