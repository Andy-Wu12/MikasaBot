# Andy Wu
# November 5th, 2020

# Custom files
import funcs
import timer

# Official imports
import discord
from datetime import datetime

# Environment variables
from os import environ
from dotenv import load_dotenv

load_dotenv()

# Discord API key should be read in from a .env file in the same directory where you are running this bot
TOKEN = environ['DISCORD_TOKEN']

# Global vars
cheer_count = 0

# Modify these accordngly for new episode releases - Better to make it a command instead of hard-coding
timer_channel = "Countdown Timer"
timer_end = datetime(2020, 11, 12, 11, 45, 0, 0, timer.timezone_offset)

# Bot functions
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Message sender, name of guild, etc
    guild = client.guilds[0]
    member = message.author

    # Number of strings in list after split is called for most command inputs.
    # Make sure to modify appropriately for those that need it
    command_strings_req = 2
    lowercase_message = message.content.lower()

    # Prevents Bot from responding to its own messages
    if message.author == client.user:
        return

    # MOD ONLY COMMANDS #
    # Clear channel chat history
    if lowercase_message == '!clear' and funcs.is_admin(message.author):
        await funcs.delete_channel_history(message.channel)

    elif lowercase_message == '!ucount' and funcs.is_admin(message.author):
        guild_name = message.author.guild
        await message.channel.send('{} user(s) in the server'.format(len(guild_name.members)))

    # Assigning role to specific server member
    elif lowercase_message.startswith('!setrole ') and funcs.is_admin(message.author):
        # validate input before doing anything else
        mess_args = lowercase_message.split()
        # This command requires 3 inputs - !command, user to change, role to assign
        if funcs.valid_num_strings(mess_args, command_strings_req + 1):
            mem_to_change = funcs.str_to_member(mess_args[1], guild.members)
            # print(mem_to_change.display_name)
            if mem_to_change is not None:
                await funcs.override_role(mem_to_change, mess_args[2])
                await message.channel.send('{} has been overidden into {}!'.format(mess_args[1], mess_args[2]))

    elif lowercase_message == '!mems' and funcs.is_admin(message.author):
        await funcs.print_all_members(message.channel, guild)
        return

    elif lowercase_message == '!countdown' and funcs.is_admin(message.author):
        await timer.run_timer(timer_end, message.channel)

    elif lowercase_message == '!stop' and funcs.is_admin(message.author):
        await message.channel.send("Bot offline on " + timer.format_date(datetime.now(timer.timezone_offset)))
        await client.logout()

    # Regular user commands #
    # Lists all possible commands for the bot
    elif lowercase_message == '!commands':
        await funcs.list_user_commands(message.channel)
        # Listing admin-only commands
        if message.author.top_role.name == funcs.admin_role_name:
            await funcs.list_admin_commands(message.channel)

    # Server cheering (just for fun) 
    elif lowercase_message.startswith('!cheer '):
        global cheer_count

        try:
            cheer_amount = int(lowercase_message.split()[1])
        except ValueError:
            # Don't need to send error message to end-user, just ignore
            print("Error converting cheer amount to a number")
            return
        cheer_count += cheer_amount
        await message.channel.send('{} has cheered {} bits, bringing the server total to {}.'.format(
            message.author.name, cheer_amount, cheer_count))

    # Users can self-assign roles as long as they are not admin roles #
    elif lowercase_message.startswith('!role '):
        # validate input before doing anything else
        message_args = lowercase_message.split()
        if funcs.valid_num_strings(message_args, command_strings_req):
            await funcs.set_role(member, message_args[1])
            await message.channel.send('{} is now a {}!'.format(member.name, message_args[1].upper()))

if __name__ == '__main__':
    client.run(TOKEN)

