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
from db.UserDB import UserDB
from API.ApiClan import ApiClan
from API.ApiPlayer import ApiPlayer
###########################################

class Slashs(commands.Cog):

    def __init__(self, bot:commands.InteractionBot):
        self.__bot = bot
    
    @commands.slash_command(name="me", dm_permission=True)
    async def me(self, inter):
        """
        """
        await inter.response.defer(ephemeral=False)
        player, user = ApiPlayer(), UserDB()
        res = player.get_player(user.get_tag(int(inter.author.id)))
        if player.is_player(res):
            embed = disnake.Embed()
            embed.set_author(
                name=res["name"],
                url=inter.author.avatar.url,
                icon_url=inter.author.avatar.url
            )
            embed.add_field(name="Level", value=f"+ {res["expLevel"]}", inline=False)
            embed.add_field(name="Role", value=f"+ {res["role"]}", inline=False)
            embed.add_field(name="HDV", value=f"+ Niveau : {res["townHallLevel"]}\n+ Trophées : {res["trophies"]}\n+ Record trophées : {res["bestTrophies"]}", inline=False)
            embed.add_field(name="MDO", value=f"+ Niveau : {res["builderHallLevel"]}\n+ Trophées : {res["builderBaseTrophies"]}\n+ Record trophées : {res["bestBuilderBaseTrophies"]}", inline=True)
            await inter.followup.send(embed=embed, ephemeral=False)
        else:
            await inter.followup.send(content=f"Erreur : Ce compte COC n'existe plus.", ephemeral=False)

    @commands.slash_command(name="clan", dm_permission=True)
    async def clan(self, inter):
        """
        """
        await inter.response.defer(ephemeral=False)
        player, user = ApiPlayer(), UserDB()
        res_player = player.get_player(user.get_tag(int(inter.author.id)))
        if player.is_player(res_player):
            if player.is_player_have_clan(res_player):
                clan = ApiClan()
                tag_clan = res_player["clan"]["tag"]
                res_clan = clan.get_clan(tag_clan[1:])
                embed = disnake.Embed(title="Description", description=res_clan["description"])
                embed.set_author(
                    name=res_clan["name"],
                    url=res_clan["badgeUrls"]["large"],
                    icon_url=res_clan["badgeUrls"]["large"]
                )
                embed.add_field(name="Type", value=f"+ {res_clan["type"]}", inline=True)
                embed.add_field(name="Level", value=f"+ {res_clan["clanLevel"]}", inline=True)
                embed.add_field(name="Membres", value=f"+ {res_clan["members"]}", inline=True)
                embed.add_field(name="Ligue", value=f"+ {res_clan["warLeague"]["name"]}", inline=False)
                embed.add_field(name="Total de trophées HDV", value=f"+ {res_clan["clanPoints"]}", inline=True)
                embed.add_field(name="Total de trophées MDO", value=f"+ {res_clan["clanBuilderBasePoints"]}", inline=True)
                embed.add_field(name="Total de trophées Capital", value=f"+ {res_clan["clanCapitalPoints"]}", inline=True)
                await inter.followup.send(embed=embed, ephemeral=False)
            else:
                await inter.followup.send(content=f"Erreur : Vous n'êtes pas dans un clan.", ephemeral=False)
        else:
            await inter.followup.send(content=f"Erreur : Ce compte COC n'existe plus.", ephemeral=False)

    @commands.slash_command(name="synchro", dm_permission=True)
    async def synchro(self, inter, tag:str):
        """
        """
        await inter.response.defer(ephemeral=True)
        player = ApiPlayer()
        tag = tag[1:] if tag[0] == '#' else tag
        res = player.get_player(str(tag))
        if player.is_player(res):
            user = UserDB()
            if user.is_user(int(inter.author.id)):
                user.set_tag(int(inter.author.id), str(tag))
            else:
                user.add_user(int(inter.author.id), str(tag))
            await inter.followup.send(content=f"Vous êtes synchronisé avec le compte COC **{res["name"]}**.", ephemeral=True)
        else:
            await inter.followup.send(content=f"Erreur : Ce compte COC n'existe pas.", ephemeral=True)

    @commands.slash_command(name="help", dm_permission=True)
    async def help(self, inter):
        """
        """
        await inter.response.defer(ephemeral=True)
        await inter.followup.send(content=f"Pour synchroniser votre compte COC à votre compte Discord, vous devez utiliser \\synchro.\nLe tag (#UDJFHBZ) que vous devez renseigner se trouver dans votre profil COC, en dessous de votre pseudo", ephemeral=True)

def setup(bot:commands.InteractionBot):
    """Ajout des slashs commandes en tant que rouage."""
    bot.add_cog(Slashs(bot))

