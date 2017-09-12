import discord
import math
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from discord.ext import commands
from discord.ext.commands import Context


class GravityCalc:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def gravstrength(self, ctx: Context, obj1: int, obj2: int, dist: int):
        """Calculates gravitational strength between two objects."""
        G = 6.67e-11
        ans = (obj1 * obj2 * G) / (dist ** 2)
        await self.bot.say(ans)

    async def tonum(obj1: str):
        if str =="sun": return 0
        if str =="earth": return 1
        if str =="moon": return 3

    @commands.command(pass_context=True)
    async def dist(self, ctx: Context, mass1: str, mass2: str):
        """distance from sun/earth/moon to each other"""
        x1 = tonum( mass1 )
        x2 = tonum(mass2)

        if abs(x1-x2)==1:
            await self.bot.say("1.5e11")
        if abs(x1-x2)==2:
            await self.bot.say("3.84e8")


    @commands.command(pass_context=True)
    async def mass(self, ctx: Context, mass1: str):
        """Mass of proton/electron/sun/moon/earth"""
        if mass1=="proton" or mass1=="p":
            await self.bot.say("1.7e-27")

        if mass1=="electron" or mass1=="e-" or mass1=="e":
            await self.bot.say("9e-31")

        if mass1=="sun" or mass1=="S":
            await self.bot.say("2e30")

        if mass1=="moon" or mass1=="M":
            await self.bot.say("7e22")

        if mass1=="earth" or mass1=="E":
            await self.bot.say("6e24")

    @commands.command(pass_context=True)
    async def value(self, ctx: Context, value: str):
        """Values of important constant"""
        if value=="G":
            await self.bot.say("6.67e-11 Nm^2/kg^2")

        if value=="c"
            await self.bot.say("3e8 m/s")

        if value=="e" or value=="electron" or value=="proton" or value=="p":
            await self.bot.say("1.6e-19 C")

        if value=="h" or value=="planck":
            await self.bot.say("6.63e-34 Js or 4.14e-15 eVs")

        if value=="e0" or value=="electric constant" or value=="permittivity of free space" or value=="vacuum permittivity":
            await self.bot.say("8.85e-12 C^2/(Nm^2)")

        if value=="u0" or value=="magnetic constant" or value=="permeability of free space" or value=="vacuum permeability":
            await self.bot.say("8.85e-12 C^2/(Nm^2)")

        if value=="avogadro" or value=="A":
            await self.bot.say("6.023e23 1/mol")

        if value=="gas" or value=="R":
            await self.bot.say("8.31 J/molK")






def setup(bot):
    n = GravityCalc(bot)
    bot.add_cog(n)