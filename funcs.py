# Andy Wu
# November 5th, 2020

# Global vars
admin_role_name = "commander"

user_command_list = ['!commands - List all commands',
                     '!cheer [amount] - Increase server cheer count by [amount]',
                     '!role [role name] - Assign yourself an avaiable role from [!rolelist]']

admin_command_list = ['!kick [userID] - Kicks user from server',
                      '!ban [userID] - Bans user from server',
                      '!clear - Clears chat history of channel typed in',
                      '!ucount - Displays # of users currently online in server',
                      '!setrole [user] [role] - Assign a member a specific role, regardless of permissions',
                      '!mems - Display usernames of all members in server']

# This part of the file contains the various functions to be used by MODS for mikasaBot.py
async def delete_channel_history(mess_channel):
    deleted = await mess_channel.purge()
    await mess_channel.send('Deleted {} message(s) for you!'.format(len(deleted)))

async def list_admin_commands(mess_channel):
    list_message = '-----------\nADMIN-ONLY COMMANDS\n-----------\n'
    for command in admin_command_list:
        list_message = list_message + command + '\n'
    await mess_channel.send(list_message)

async def override_role(member, role_name):
    role = str_to_role(role_name, member.guild.roles)
    if member is not None:
        await member.add_roles(role)

# This part of the file contains the various functions to be used by anyone for mikasaBot.py
async def list_user_commands(mess_channel):
    list_message = '-----------\nUSER COMMANDS\n-----------\n'
    for command in user_command_list:
        list_message = list_message + command + '\n'
    await mess_channel.send(list_message)


async def set_role(member, role_name):
    if role_name.lower() == "commander":
        return
    else:
        role = str_to_role(role_name, member.guild.roles)
        if role is not None:
            await member.add_roles(role)

# This part of the file contains helper functions for the methods in the two sections above
def valid_num_strings(strng_list, req_num):
    if len(strng_list) != req_num:
        return False
    return True

def str_to_role(role_name, role_list):  # role_list should be a List[Role] passed into the function from mikasaBot.py
    for role in role_list:
        if str(role) == role_name:
            return role
    return None

def str_to_member(member_name, mem_list):  # mem_list should be a List[Role] passed into the function from mikasaBot.py
    for member in mem_list:
        # print(member.display_name.lower() + '--------' + member_name)
        if member.display_name.lower() == member_name:
            return member
    return None

def is_admin(member):
    return member.top_role.name == admin_role_name

async def print_all_members(mess_channel, guild):
    # print(len(guild.members))
    for member in guild.members:
        await mess_channel.send(member.name)
