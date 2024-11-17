#!py-env/bin/python3
# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
###########################################

###########################################
#                 modules                 #
###########################################
from cogs.Events import Events
from cogs.Slashs import Slashs
from cogs.Tasks import Tasks
###########################################

if __name__ == '__main__' :

    #flag configuration
    flag = commands.CommandSyncFlags.default()
    flag.sync_commands_debug = True
    intents = disnake.Intents.all()

    bot = commands.InteractionBot(command_sync_flags=flag, intents=intents)

    #charger les extensions (rouages)
    bot.load_extensions("cogs")

    #démarrage du bot
    load_dotenv()
    token = os.getenv('BOT_TOKEN')
    bot.run(token)