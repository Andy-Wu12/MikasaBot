# Andy Wu
# November 5th, 2020

import discord
from datetime import datetime, timezone, timedelta

# Global vars
timezone_offset = timezone(timedelta(hours=-5))  # Specifically for UTC to EST

# <date_time> -- the datetime.datetime object indicating the END of the countdown
	# Make sure tzinfo is set as -timedelta(5) for EST
# <channel> -- the channel object indicating which channel to send updates to
async def run_timer(date_time, channel):
	currTime = datetime.now(timezone_offset)
	timeStr = format_date(currTime)
	message = await channel.send("@everyone\nCurrent time: " + timeStr)

	while currTime < date_time:
		currTime = datetime.now(timezone_offset)
		timeStr = format_date(currTime)
		try:
			await message.edit(content=str("@everyone\nCurrent time: " + timeStr))

		except discord.errors.NotFound:
			message = await channel.send("@everyone\nCurrent time: " + timeStr)

def format_date(date_time):
	return date_time.strftime('%B %d, %Y -- %I:%M:%S %p')
