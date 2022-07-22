# [Attack-on-Titan](https://myanimelist.net/anime/16498/Shingeki_no_Kyojin) Themed Discord Bot

This was a discord bot that I built for fun to use with my friends in our private server a few years ago.
The main goal was to have a countdown timer that we could see daily showing the amount of time 
left until the newest season / episodes of our favorite show(s) premiered.

The bot has a very limited amount of commands built in, but it should be easy to add more if desired.

The code definitely isn't clean or efficient (hard-coded premiere date? YIKES!), but this was a great introduction to me in using APIs and building software
out of any ideas that came to mind.

## Dependencies
1. At least Python 3.0
2. Discord module, installed with `pip3 install discord`
3. python-dotenv for reading environment variables, installed with `pip3 install python-dotenv`
4. certifi for handling SSL Certificate Verification, installed with `pip3 install certifi`

## How to set up and run your own copy
1. Clone the repository onto wherever you plan to run the bot
2. Login to in the discord [developer portal](https://discord.com/developers/applications) and create a "New Application"
3. Select the application in the "My Applications" section
4. Open the navigation menu on the top left and click "Bot"
5. Click "Add Bot" (Make sure your application name isn't extremely common or else you will get an error)
6. Click "Reset Token" then "Yes, do it!"
   1. If you have 2FA setup, you will have to enter your authenticator code.
7. Create a .env file in the project's root directory and type `DISCORD_TOKEN=<YOUR_TOKEN_HERE>`, 
   replacing the entire right-hand side with the token that shows up after step 6
   1. **NOTE**: If you are hosting the server on a cloud service, you should be able to provide the environment variables directly in the application
   settings.
8. Run the bot with the command `python3 mikasaBot.py`
