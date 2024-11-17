# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import disnake
from disnake.ext import commands
###########################################

###########################################
#                 modules                 #
###########################################
from cogs.Tasks import Tasks
###########################################

class Events(commands.Cog):
    """
    """
    
    def __init__(self, bot:commands.InteractionBot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """
        """
        await Tasks(self.__bot).update_activity.start()

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, error):
        """
        """
        if isinstance(error, commands.errors.CommandOnCooldown):
            await inter.response.defer(ephemeral=True)
            await inter.followup.send(content=f':no_entry: Du calme, réesayez dans {round(error.retry_after, 1)} secondes')
        else:
            print(error)

def setup(bot:commands.InteractionBot):
    """
    """
    bot.add_cog(Events(bot))