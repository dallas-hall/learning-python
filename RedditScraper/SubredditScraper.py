#!/usr/bin/python3
import logging
import os
import sys
import time
from pprint import pprint

import asyncpraw
import discord
from discord.ext import commands
from discord.ext import tasks

# Define logging output
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')

# Enable debugging messages
debugging = True
if not debugging:
	logging.disable(logging.DEBUG)
# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

subreddits = {
	'SFW': {
		'funny': {},
		'linuxmasterrace': {},
		'memes': {},
		'ProgrammerHumor': {},
		'TikTokCringe': {}
	},
	"NSFW": {
		'AsianCumSluts': {},
		'AsianPornIn1Minute': {},
		'AsianBlowjobs': {},
		'AsiansGoneWild': {},
		'nextdoorasians': {}
	}
}

if debugging:
	for k in subreddits['SFW']:
		subreddits['SFW'][k]['discordChannel'] = 'bot-testing'
	for k in subreddits['NSFW']:
		subreddits['NSFW'][k]['discordChannel'] = 'bot-testing-two'
	pprint(subreddits)
else:
	for k in subreddits['SFW']:
		if subreddits['SFW'][k] == 'funny' or subreddits['SFW'][k] == 'memes' or subreddits['SFW'][k] == 'TikTokCringe':
			subreddits['SFW'][k]['discordChannel'] = 'meme-spew'
		elif subreddits['SFW'][k] == 'linuxmasterrace':
			subreddits['SFW'][k]['discordChannel'] = 'linux-guru'
		elif subreddits['SFW'][k] == 'ProgrammerHumor':
			subreddits['SFW'][k]['discordChannel'] = 'code-review'
	for k in subreddits['NSFW']:
		subreddits['NSFW'][k]['discordChannel'] = 'nsfw-view'
	pprint(subreddits)

# https://github.com/reddit-archive/reddit/wiki/API
# https://github.com/reddit-archive/reddit/wiki/OAuth2
REDDIT_API_CLIENT_ID = os.environ['REDDIT_API_CLIENT_ID']
REDDIT_API_CLIENT_SECRET = os.environ['REDDIT_API_CLIENT_SECRET']
REDDIT_API_CLIENT_USER_AGENT = os.environ['REDDIT_API_CLIENT_USER_AGENT']
REDDIT_URL = 'https://reddit.com/'
REDDIT_POST_RETURN_LIMIT = 1

# https://praw.readthedocs.io/en/v7.2.0/getting_started/quick_start.html#read-only-reddit-instances
reddit = asyncpraw.Reddit(
	client_id=REDDIT_API_CLIENT_ID,
	client_secret=REDDIT_API_CLIENT_SECRET,
	user_agent=REDDIT_API_CLIENT_USER_AGENT
)
logging.debug('Connected to Reddit as read only? ' + str(reddit.read_only))

# Create a Bot instance - https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#bot
discordBot = commands.Bot(
	command_prefix='$',
	case_insensitive=True,
	self_bot=False
)

discordBot.description = f"Reddit scraper."
DISCORD_GUILD_ID = 251648924060876801


# https://stackoverflow.com/questions/56122336/discord-py-rewrite-setting-up-background-tasks-background-tasks-not-loading
@tasks.loop(seconds=1, count=1)
async def get_content():
	logging.info('During task loop.')
	guild = discordBot.get_guild(DISCORD_GUILD_ID)
	for subreddit in subreddits['SFW']:
		logging.debug('Processing safe for work sub-reddits.')
		current_subreddit = await reddit.subreddit(subreddit)
		# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/subreddit.html?highlight=top#praw.models.Subreddit.top
		async for submission in current_subreddit.top("day", limit=REDDIT_POST_RETURN_LIMIT):
			# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/submission.html?highlight=submission#praw.models.Submission
			print(submission.title)
			print(REDDIT_URL + submission.permalink)
			print(submission.url)
			desired_channel = subreddits['SFW'][subreddit]['discordChannel']
			for channel in guild.channels:
				if channel.name == desired_channel:
					post_channel_id = discordBot.get_channel(channel.id)
					# await post_channel_id.send(REDDIT_URL + submission.permalink)
					await post_channel_id.send(submission.url)
					break

	for subreddit in subreddits['NSFW']:
		logging.debug('Processing not safe for work sub-reddits.')
		current_subreddit = await reddit.subreddit(subreddit)
		# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/subreddit.html?highlight=top#praw.models.Subreddit.top
		async for submission in current_subreddit.top("day", limit=REDDIT_POST_RETURN_LIMIT):
			# https://praw.readthedocs.io/en/v7.2.0/code_overview/models/submission.html?highlight=submission#praw.models.Submission
			print(submission.title)
			print(REDDIT_URL + submission.permalink)
			print(submission.url)
			desired_channel = subreddits['NSFW'][subreddit]['discordChannel']
			for channel in guild.channels:
				if channel.name == desired_channel:
					post_channel_id = discordBot.get_channel(channel.id)
					# await post_channel_id.send(REDDIT_URL + submission.permalink)
					await post_channel_id.send(submission.url)
					break


@get_content.before_loop
async def before():
	await discordBot.wait_until_ready()
	logging.info("Logged in as " + str(discordBot.user.name) + " with the ID " + str(discordBot.user.id))
	logging.info("The current version of Discord is " + str(discord.version_info))
	logging.info('Before task loop.')


@get_content.after_loop
async def after():
	logging.info('After task loop.')
	await discordBot.close()


# Call our task
get_content.start()

# Token goes here.
discordBot.run(os.environ['DISCORD_BOT_TOKEN'])
