from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='test')
    async def test(self, ctx, *args):
        await ctx.send(' '.join(args))

def setup(bot):
    bot.add_cog(TestCog(bot))