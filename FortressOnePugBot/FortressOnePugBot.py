#!./fortress-one-pug-bot-venv/bin/python3
import asyncio
import logging
import os
import sys
import time
from pprint import pprint
from random import randrange
# https://docs.python.org/3/library/threading.html#timer-objects
from datetime import datetime, timedelta
from pytz import timezone

import discord
from discord.ext import commands

# Enable debugging messages - https://docs.python.org/3/library/asyncio-dev.html#logging
debugging = False
if debugging:
	logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - [%(levelname)s] - %(message)s')
else:
	logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(message)s')
logger = logging.getLogger("asyncio")

# TODO Use 1 for testing
if debugging:
	MIN_TEAM_SIZE = 1
else:
	MIN_TEAM_SIZE = 2
MAX_TEAM_SIZE = 8
DEFAULT_TEAM_SIZE = 4
DEFAULT_MAX_PLAYERS = DEFAULT_TEAM_SIZE * 2
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_UNTIL_TIMEOUT = 4 # Change this to adjust timer
if debugging:
	TIME_OUT_SECONDS = 60
else:
	TIME_OUT_SECONDS = SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_UNTIL_TIMEOUT
TIME_OUT_HUMAN_READABLE = timedelta(seconds=TIME_OUT_SECONDS)



# Print start message and delay slightly	
logging.info('Starting ' + os.path.relpath(sys.argv[0]))
time.sleep(.001)

time_zones = {
	"au_aest": "Australia/Brisbane",
	"au_aedt": "Australia/Sydney",
	"nz_auck": "Pacific/Auckland",
	"kr_seoul": "Asia/Seoul",
	"jp_tokyo": "Asia/Tokyo",
	"us_pst": "America/Los_Angeles",
	"us_cst": "America/Mexico_City",
	"us_est": "America/New_York"
}

# Memes
all_memes = {
	"clans": {
		"a": [],
		"dacc": [],
		"fabb": [],
		"sobar": []
	},
	"players": {
		"basss": [],
		"bigdal": [],
		"loki": [],
		"seano": [],
		"wolv": []
	}
}

# Pugs for each region
all_pugs = {
	"bot-testing": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	},
	"bot-testing-two": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	},
	"oceania": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	},
	"north-america": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	},
	"brazil": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	},
	"europe": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	},
	"east-asia": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	},
	"russia": {
		"active": False,
		"timeoutTimer": None,
		"timeoutTimes": [],
		"teams": {
			"red": [],
			"blue": [],
			"lastAdded": "",
			"size": DEFAULT_TEAM_SIZE,
			"maxPlayers": DEFAULT_MAX_PLAYERS
		}
	}
}


async def get_timeout_times(context):
	channel = context.message.channel
	timeout_times = ""
	for a_time in all_pugs[channel.name]['timeoutTimes']:
		timeout_times += "\t" + a_time + "\n"
	return timeout_times


async def get_player_counts(context):
	channel = context.message.channel
	player_counts = {
		"blue": 0,
		"red": 0,
	}
	count = 0
	for player in all_pugs[channel.name]['teams']['blue']:
		count += 1
	player_counts["blue"] = count

	count = 0
	for player in all_pugs[channel.name]['teams']['red']:
		count += 1
	player_counts["red"] = count

	return player_counts


async def get_red_players(context):
	channel = context.message.channel
	red_players = []
	for player in all_pugs[channel.name]['teams']['red']:
		red_players.append(player)
	return red_players


async def get_red_players_display_names(context):
	channel = context.message.channel
	red_players = ""
	for existing_player in all_pugs[channel.name]['teams']['red']:
		red_players += str(existing_player.name) + ", "
	if not red_players:
		red_players = "no one"
	else:
		# Remove the last , and space
		red_players = red_players[:-2]
	return red_players


async def get_red_players_mention_names(context):
	channel = context.message.channel
	red_players = ""
	for existing_player in all_pugs[channel.name]['teams']['red']:
		red_players += str(existing_player.mention) + ", "
	if not red_players:
		red_players = "no one"
	else:
		# Remove the last , and space
		red_players = red_players[:-2]
	return red_players


async def get_blue_players(context):
	channel = context.message.channel
	blue_players = []
	for player in all_pugs[channel.name]['teams']['blue']:
		blue_players.append(player)
	return blue_players


async def get_blue_players_display_names(context):
	channel = context.message.channel
	blue_players = ""
	for existing_player in all_pugs[channel.name]['teams']['blue']:
		blue_players += str(existing_player.name) + ", "
	if not blue_players:
		blue_players = "no one"
	else:
		# Remove the last , and space
		blue_players = blue_players[:-2]
	return blue_players


async def get_blue_players_mention_names(context):
	channel = context.message.channel
	blue_players = ""
	for existing_player in all_pugs[channel.name]['teams']['blue']:
		blue_players += str(existing_player.mention) + ", "
	if not blue_players:
		blue_players = "no one"
	else:
		# Remove the last , and space
		blue_players = blue_players[:-2]
	return blue_players


async def set_team_sizes(context, argument):
	channel = context.message.channel
	logging.debug(f"set_team_sizes entered - #{channel.name}")
	if argument.isdigit():
		player = context.message.author
		if int(argument) < MIN_TEAM_SIZE or int(argument) > MAX_TEAM_SIZE:
			# await means to wait until this command has been executed, then continue.
			await context.send(
				f"{player.mention}, your inputs aren't sensible. Must be between {MIN_TEAM_SIZE} and {MAX_TEAM_SIZE}, inclusive.")
		elif all_pugs[context.message.channel.name]["active"]:
			await context.send("Team sizes can only be updated before a PUG has started.")
		else:
			all_pugs[context.message.channel.name]["teams"]["size"] = int(argument)
			all_pugs[context.message.channel.name]["teams"]["maxPlayers"] = int(argument) * 2
			await context.send(
				f"{player.mention} set team sizes set to " + argument + ". Total players allowed is " + str(int(argument) * 2))
	else:
		await context.send("Invalid argument. Must be a number.")
	logging.debug(f"set_team_sizes exited - #{channel.name}")


async def start_pug_command(context):
	channel = context.message.channel
	logging.debug(f"start_pug_command entered - #{channel.name}")
	player = context.message.author
	# Check if a PUG is already active for that channel.
	if all_pugs[channel.name]['active']:
		await context.send(
			f"`#{channel.name}` has an existing PUG, {player.name}. Type `{bot.command_prefix}join` to join a team.")
	else:
		# start the PUG
		all_pugs[channel.name]['active'] = True
		# add the player to a random team in the PUG
		prn = randrange(0, 2)
		if prn == 0:
			all_pugs[channel.name]['teams']['red'].append(player)
			all_pugs[channel.name]['teams']['lastAdded'] = "red"
		else:
			all_pugs[channel.name]['teams']['blue'].append(player)
			all_pugs[channel.name]['teams']['lastAdded'] = "blue"
		team_colour = all_pugs[channel.name]['teams']['lastAdded']
		# Using channel.mention here to notify all people in the channel that a PUG has started.
		await context.send(f"{player.name} started a PUG for {channel.mention} and has joined team {team_colour}.\nThis PUG will automatically end in {TIME_OUT_HUMAN_READABLE} HH:MM:SS")
		# TODO add timer
		logging.info(f"#{channel.name} PUG started. Ending PUG after {TIME_OUT_SECONDS} seconds.")
		await start_timer(context)
	logging.debug(f"start_pug_command exited - #{channel.name}")


async def end_pug_command(context, pug_timed_out):
	channel = context.message.channel
	logging.debug(f"end_pug_command entered - #{channel.name}")
	player = context.message.author

	if all_pugs[channel.name]['active']:
		# TODO test cancel timer
		#await cancel_timer(context)
		timer_task = all_pugs[channel.name]['timeoutTimer']
		await reset_pug(channel)

		if pug_timed_out:
			await context.send(f"`#{channel.name}` PUG ended due to timeout after {TIME_OUT_HUMAN_READABLE} HH:MM:SS")
			logging.info(f"#{channel.name}` PUG ended due to timeout.")
		else:
			await context.send(f"{player.name} stopped the PUG for `#{channel.name}`")
			logging.info(f"#{channel.name}` PUG ended due to players.")
	else:
		timer_task = None
		await context.send(
			f"{player.mention}, there is no PUG for `#{channel.name}`. Type `{bot.command_prefix}startpug` to start one.")

	logging.debug(f"end_pug_command exited - #{channel.name}")
	if timer_task is not None and timer_task is not True:
		await timer_task.cancel()


async def join_pug_command(context):
	channel = context.message.channel
	player = context.message.author
	logging.debug(f"join_pug_command entered - #{channel.name}")
	team_colour = ""
	already_joined = False
	# Check if the PUG is active for the channel, if not start one
	if not all_pugs[channel.name]['active']:
		await context.send(f"There is no PUG for this channel, starting one now.")
		await start_pug_command(context)
		#await context.send(f"{player.mention}, there is no PUG for #`#{channel.name}`. Type `{bot.command_prefix}startpug` to start one.",	help="Start PUG.")
	else:
		# Check if the player has already joined a team.
		for existing_player in all_pugs[channel.name]['teams']['red']:
			if existing_player == player:
				already_joined = True
				team_colour = 'red'
				break
		if not already_joined:
			for existing_player in all_pugs[channel.name]['teams']['blue']:
				if existing_player == player:
					already_joined = True
					team_colour = 'blue'
					break
		# Add the player if they haven't already joined a team
		if not already_joined:
			# Add to blue if red has more players.
			if len(all_pugs[channel.name]['teams']['red']) > len(all_pugs[channel.name]['teams']['blue']):
				all_pugs[channel.name]['teams']['blue'].append(player)
				all_pugs[channel.name]['teams']['lastAdded'] = "blue"
			# Add to red if blue has more players.
			elif len(all_pugs[channel.name]['teams']['red']) < len(all_pugs[channel.name]['teams']['blue']):
				all_pugs[channel.name]['teams']['red'].append(player)
				all_pugs[channel.name]['teams']['lastAdded'] = "red"
			# Add to the next team, the opposite of the last team that got a player.
			else:
				if all_pugs[channel.name]['teams']['lastAdded'] == 'red':
					all_pugs[channel.name]['teams']['blue'].append(player)
					all_pugs[channel.name]['teams']['lastAdded'] = "blue"
				else:
					all_pugs[channel.name]['teams']['red'].append(player)
					all_pugs[channel.name]['teams']['lastAdded'] = "red"
			team_colour = all_pugs[channel]['teams']['lastAdded']
			pprint(all_pugs[channel.name])
			await context.send(f"{player} has been added to the {team_colour} team.")
			# Start the timer if they are the first player to join
			if len(all_pugs[channel.name]['teams']['red']) == 0 and len(all_pugs[channel.name]['teams']['blue']) == 1 or \
				len(all_pugs[channel.name]['teams']['red']) == 1 and len(all_pugs[channel.name]['teams']['blue']) == 0:
				await start_timer(context)
			# TODO test restart timer
			# Restart the timer if they aren't the first player to join
			else:
				await restart_timer(context)
			# TODO teams are full
			if await are_teams_full(channel.name):
				all_players = await start_the_game(context)
				await context.send("Game has started, time to join the server. " + all_players +
								   f"\nThis PUG will automatically end in {TIME_OUT_HUMAN_READABLE} HH:MM:SS")

		else:
			await context.send(f"You are on the {team_colour} team already {player.name}")
	logging.debug(f"join_pug_command exited - #{channel.name}")


async def leave_pug_command(context):
	channel = context.message.channel
	player = context.message.author
	logging.debug(f"leave_pug_command entered.- #{channel.name}")
	team_colour = ""
	already_joined = False
	# Check if a pug exists for this channel
	if not all_pugs[context.message.channel.name]["active"]:
		await context.send(f"{player.name}, there is no PUG for #`#{channel.name}`. Type `{bot.command_prefix}startpug` to start one.")
	else:
	# Check if the player has already joined
		for existing_player in all_pugs[channel.name]['teams']['red']:
			if existing_player == player:
				already_joined = True
				team_colour = "red"
				break
		if not already_joined:
			for existing_player in all_pugs[channel.name]['teams']['blue']:
				if existing_player == player:
					already_joined = True
					team_colour = "blue"
					break
		if already_joined:
			all_pugs[channel.name]['teams'][team_colour].remove(player)
			if await are_teams_empty(channel):
				# await reset_pug(channel)
				#await context.send(f"{player.mention} has left the {team_colour} team and ended the PUG for `#{channel.name}`. Type `{bot.command_prefix}startpug` to start one.")
				await context.send(f"The PUG is ending because you were the last player.")
				msg = f"{player.name} stopped the PUG for `#{channel.name}`"
				await end_pug_command(context, False)
				pprint(all_pugs[channel.name])
			else:
				# Reset the last added colour so the correct team gets the next player
				if team_colour == 'red':
					all_pugs[channel.name]['teams']['lastAdded'] = 'blue'
				else:
					all_pugs[channel.name]['teams']['lastAdded'] = 'red'
				# TODO Update current player count display
				await context.send(f"{player.name} has left the {team_colour} team.")
		else:
			await context.send(f"You can't leave since you aren't in a team {player.name}.")
	logging.debug(f"leave_pug_command exited - #{channel.name}")


async def team_pug_status_command(context):
	channel = context.message.channel
	player = context.message.author
	logging.debug(f"team_pug_status_command entered.- #{channel.name}")
	if not all_pugs[channel.name]['active']:
		await context.send(
			f"{player.name}, there is no PUG for `#{channel.name}`. Type `{bot.command_prefix}startpug` to start one.")
	else:
		# Get the players from both teams
		blue_players = await get_blue_players_display_names(context)
		red_players = await get_red_players_display_names(context)

		# TODO add current player count display
		player_counts = await get_player_counts(context)
		pprint(player_counts)
		blue = player_counts["blue"]
		red = player_counts["red"]
		team_size = all_pugs[channel.name]["teams"]["size"]
		current_count = blue + red
		expire_times = await get_timeout_times(context)
		max_players = all_pugs[channel.name]["teams"]["maxPlayers"]
		await context.send(f"For the PUG in `#{channel.name}`, there are {current_count}/{max_players} players, and it will currently expire at\n{expire_times}" +
							f"Blue team currently has {blue}/{team_size} - " + blue_players +
							f".\nRed team currently has {red}/{team_size} - " + red_players + ".")
		pprint(all_pugs[channel.name])
		logging.debug(f"team_pug_status_command exited - #{channel.name}")


async def are_teams_empty(channel):
	logging.debug(f"are_teams_empty entered and exited.- #{channel.name}")
	# Check the length of both teams, if they are both 0 we will return True.
	return len(all_pugs[channel.name]['teams']['red']) == 0 and \
		   len(all_pugs[channel.name]['teams']['blue']) == 0


async def are_teams_full(channel):
	logging.debug(f"are_teams_full entered and exited.- #{channel.name}")
	# Check the length of both teams, if they both match team size then return True
	return len(all_pugs[channel.name]['teams']['red']) == all_pugs[channel.name]['teams']['size'] and \
		   len(all_pugs[channel.name]['teams']['blue']) == all_pugs[channel.name]['teams']['size']


#TODO UPDATE THIS WITH NEW FIELDS
async def reset_pug(channel):
	logging.debug(f"reset_pug entered - #{channel.name}")
	all_pugs[channel.name]['active'] = False
	all_pugs[channel.name]['timeoutTimer'] = None
	all_pugs[channel.name]['teams']['lastAdded'] = ""
	all_pugs[channel.name]['teams']['blue'] = []
	all_pugs[channel.name]['teams']['red'] = []
	all_pugs[channel.name]['teams']['size'] = DEFAULT_TEAM_SIZE
	all_pugs[channel.name]['teams']['maxPlayers'] = DEFAULT_MAX_PLAYERS
	logging.debug(f"reset_pug exited - #{channel.name}")


async def start_the_game(context):
	channel = context.message.channel
	logging.debug(f"start_the_game entered - #{channel.name}")
	all_players = ""
	for existing_player in all_pugs[channel.name]['teams']['red']:
		all_players += discord.utils.find(lambda m: m.name == existing_player, context.message.channel.members) + ", "

	for existing_player in all_pugs[channel.name]['teams']['blue']:
		all_players += discord.utils.find(lambda m: m.name == existing_player, context.message.channel.members) + ", "
	# Remove the last space and comma
	logging.debug(f"start_the_game exited - #{channel.name}")
	return all_players[:-2]


async def do_function_after(delay, function):
	logging.debug("do_after_function entered.")
	await asyncio.sleep(delay)
	if debugging:
		logging.debug("do_after_function object print.")
		print(function)
	await function
	logging.debug("do_after_function exited.")


async def start_timer(context):
	channel = context.message.channel
	logging.debug(f"start_timer entered - #{channel.name}")
	# TODO start the timer for the channel when a pug starts
	# Create the async task
	timer_task = asyncio.create_task(
		# Delay running the passed in function
		do_function_after(delay=TIME_OUT_SECONDS, function=end_pug_command(context, True))
	)
	# TODO store the timer for the channel
	all_pugs[channel.name]['timeoutTimer'] = timer_task
	if channel.name is 'oceania' or channel.name == 'bot-testing' or channel.name == 'bot-testing-two':
		all_pugs[channel.name]['timeoutTimes'].append("Sydney - " + (datetime.now(timezone(time_zones["au_aedt"])) +
			timedelta(seconds=TIME_OUT_SECONDS)).strftime("%Y-%m-%d %H:%M:%S"))
		all_pugs[channel.name]['timeoutTimes'].append("Auckland - " + (datetime.now(timezone(time_zones["nz_auck"])) +
			timedelta(seconds=TIME_OUT_SECONDS)).strftime("%Y-%m-%d %H:%M:%S"))
		all_pugs[channel.name]['timeoutTimes'].append("zel - some time way after what was expected.")
	elif channel.name == 'north-america':
		all_pugs[channel.name]['timeoutTimes'].append("L.A. - " + (datetime.now(timezone(time_zones["us_pst"])) +
			timedelta(seconds=TIME_OUT_SECONDS)).strftime("%Y-%m-%d %H:%M:%S"))
		all_pugs[channel.name]['timeoutTimes'].append("Mexico - " + (datetime.now(timezone(time_zones["us_cst"])) +
			timedelta(seconds=TIME_OUT_SECONDS)).strftime("%Y-%m-%d %H:%M:%S"))
		all_pugs[channel.name]['timeoutTimes'].append("N.Y - " + (datetime.now(timezone(time_zones["us_est"])) +
			timedelta(seconds=TIME_OUT_SECONDS)).strftime("%Y-%m-%d %H:%M:%S"))
	elif channel.name == 'east-asia':
		all_pugs[channel.name]['timeoutTimes'].append("Tokyo/Seoul - " + (datetime.now(timezone(time_zones["jp_tokyo"])) +
			timedelta(seconds=TIME_OUT_SECONDS)).strftime("%Y-%m-%d %H:%M:%S"))
	else:
		all_pugs[channel.name]['timeoutTimes'].append("No one use this here so fuck your time.")

	# TODO start the timer
	logging.info(f"#{channel.name} timer started.")
	pprint(all_pugs[channel.name])
	await all_pugs[channel.name]['timeoutTimer']
	logging.debug(f"start_timer exited - #{channel.name}")
	

async def cancel_timer(context):
	channel = context.message.channel
	logging.debug(f"cancel_timer entered - #{channel.name}")
	# TODO cancel the existing timer for the channel
	all_pugs[channel.name]['timeoutTimer'].cancel()
	logging.info(f"#{channel.name} timer cancelled.")
	if debugging:
		print(all_pugs[channel.name]['timeoutTimer'])
	logging.debug(f"cancel_timer exited - #{channel.name}")


async def restart_timer(context):
	channel = context.message.channel
	logging.debug(f"restart_timer entered - #{channel.name}")
	logging.info(f"#{channel.name} timer restarted with {TIME_OUT_SECONDS} seconds.")
	# TODO cancel the existing timer for the channel
	await cancel_timer(context)
	# TODO start the timer for the channel when a new player joins the pug
	await start_timer(context)
	logging.debug(f"restart_timer exited - #{channel.name}")


# Create a Bot instance - https://discordpy.readthedocs.io/en/latest/ext/commands/api.html#bot
bot = commands.Bot(command_prefix='$')
bot.case_insensitive = True
bot.description = f"FortressOne PUG bot. Type {bot.command_prefix}help to see available commands."
bot.self_bot = False # Ignore itself

# Wait for the bot to login and be ready
@bot.event
async def on_ready():
	print("Logged in as " + str(bot.user.name) + " with the ID " + str(bot.user.id))
	print("The current version of Discord is " + str(discord.version_info))
	if debugging:
		print("The all_pugs dictionary currently is:\n")
		pprint(all_pugs)


# TODO use cogs to group commands into categories (PUG and meme)
# https://discordpy.readthedocs.io/en/latest/ext/commands/cogs.html#quick-example
# This automatically adds the command - https://discordpy.readthedocs.io/en/latest/ext/commands/commands.html#
@bot.command(description=
			 f"Set the amount of players per team for the PUG on this channel."
			 "Default is {DEFAULT_TEAM_SIZE}, so {DEFAULT_TEAM_SIZE} vs {DEFAULT_TEAM_SIZE}.",
			 aliases=["ts"],
			 help="Change team sizes.")
async def teamsize(context, argument):
	await set_team_sizes(context, argument)


@bot.command(description="Start a PUG for this channel.", aliases=["s", "start"], help="Start PUG.")
async def startpug(context):
	# Allows me to call this function from other areas
	await start_pug_command(context)


@bot.command(description="End the PUG for this channel.", aliases=["e", "end"], help="End PUG.")
async def endpug(context):
	# Allows me to call this function from other areas
	await end_pug_command(context, False)


@bot.command(description="Join a team on the PUG for this channel.", aliases=["j"], help="Join team.")
async def join(context):
	await join_pug_command(context)


@bot.command(description="Leave a team on the PUG for this channel.", aliases=["l"], help="Leave PUG.")
async def leave(context):
	await leave_pug_command(context)


@bot.command(description="Print the current teams and PUG status for the PUG on this channel.",
			 aliases=["pug", "p"], help="Print teams/PUG status.")
async def pugstatus(context):
	await team_pug_status_command(context)


@bot.command(description="Print common Australian and American timezones.", aliases=["t"], help="Print time.")
async def time(context):
	message = ""
	for k,v in time_zones.items():
		message += f"Current time in {v} is " + datetime.now(timezone(v)).strftime("%Y-%m-%d %H:%M:%S\n")

	await context.send(message)


# @bot.command(aliases=["tst"])
# async def test_start_timer(context):
# 	await context.send(f"Start test timer with {TIME_OUT_HUMAN_READABLE} HH:MM:SS")
# 	await start_timer(context)
# 
# 
# @bot.command(aliases=["tct"])
# async def test_cancel_timer(context):
# 	await context.send(f"Cancelling test timer.")
# 	await cancel_timer(context)
# 
# 
# @bot.command(aliases=["trt"])
# async def test_restart_timer(context):
# 	await context.send(f"Restarting test timer with {TIME_OUT_HUMAN_READABLE} HH:MM:SS")
# 	await restart_timer(context)

# Token goes here. TODO change to environment variable.
bot.run(os.environ['FORTRESSONE_PUG_BOT_TOKEN'])
