# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import disnake
from disnake.ext import tasks, commands
###########################################

class Tasks(commands.Cog):
    """
    """

    def __init__(self, bot:commands.InteractionBot):
        self.__bot = bot

    @tasks.loop(hours=1.0)
    async def update_activity(self):
        """Appelé toutes les heures pour mettre à jour le status du bot."""
        servers = len(self.__bot.guilds)
        if servers > 1:
            activity = disnake.Game(f'l\'API disnake | {servers} serveurs')
            await self.__bot.change_presence(status=disnake.Status.online, activity=activity)
        else:
            activity = disnake.Game(f'l\'API disnake | {servers} serveur')
            await self.__bot.change_presence(status=disnake.Status.online, activity=activity)

def setup(bot:commands.InteractionBot):
    """Ajout des tâches de fond en tant que rouage."""
    bot.add_cog(Tasks(bot))