import discord
import json
import os
from discord.ext import tasks, commands
from dh_utils import get_details, get_id, get_max
class Haberci(commands.Cog):
    def __init__(self, bot) -> None:
        if not os.path.exists("channels.json"):
            with open("channels.json", "w", encoding="utf-8") as file:
                pass
            self.settings = {}
        elif os.stat("channels.json").st_size != 0:
            with open("channels.json", "r", encoding="utf-8") as f:
                self.settings = json.load(f)
        else:
            self.settings = {}
        self.max = {}
        for key in self.settings:
            self.max[key] = get_max(key)[0]
        self.bot = bot
        self.checker.start()

    def cog_unload(self):
        self.checker.stop()

    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Böyle bir komut yok. help komutunu yazarak tüm komutlara bakabilirsiniz.")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("**Lütfen parametreleri giriniz!**")
        else:
            print(error)

    @tasks.loop(minutes=1.0)
    async def checker(self):
        for link in self.max:
            newest_id = self.max[link]
            linkler = get_id(link=link)
            filtreli = list(filter(lambda x: x[0]>newest_id,linkler))
            if len(filtreli)!=0:
                for i in filtreli:
                    print(f"Yeni konu!!! {i[1]}")
                    for channel in self.settings[link]:
                        details = get_details(i[1])
                        embed = discord.Embed(title="Yeni konu!",
                                url=f"{i[1]}",
                                description=f"{details[0]} forumunda yeni konu açıldı!",
                                colour=0xf57307)

                        embed.add_field(name=f"{details[1]}",
                            value=f"{details[2]}",
                            inline=False)
                        await self.bot.get_channel(channel).send(embed=embed)
                self.max[link] = max(filtreli,key=lambda x: x[0])[0]
            else:
                print(f"Aynı {link}")
    
    @commands.command()
    async def ekle(self, ctx, link):
        """
        Verilen altforum linkini kontrol edilecekler listesine ekler
        """


        with open("channels.json","r+", encoding="utf-8") as f:
            if os.stat("channels.json").st_size == 0:
                data = {}
                data[link] = [ctx.channel.id,]
                self.settings[link] = [ctx.channel.id,]
                f.seek(0)
                json.dump(data, f)
                await ctx.send("Eklendi.")
            else:
                data = json.load(f)
                if link in data and ctx.channel.id in data[link]:
                    await ctx.send("Zaten eklenmiş.")
                elif link in data:    
                    data[link].append(ctx.channel.id)
                    self.settings[link].append(ctx.channel.id)
                    await ctx.send("Eklendi.")
                else:
                    data[link] = [ctx.channel.id,]
                    self.settings[link] = [ctx.channel.id,]
                    await ctx.send("Eklendi.")
            f.seek(0)
            json.dump(data, f)
        for key in self.settings:
            if key not in self.max.keys():
                self.max[key] = get_max(key)[0]
    
    @commands.command()
    async def sitecikar(self, ctx, link):
        """
        Bu komutun çalıştırıldığı kanal verilen altforumun haber verilecekler listesinden çıkarır
        """
        self.settings[link].remove(ctx.channel.id)
        with open("channels.json", "w") as f:
            json.dump(self.settings, f)
        await ctx.send("Çıkarıldı.")
    @commands.command()
    async def cikar(self, ctx):
        """
        Komutun çalıştırıldığı kanalı haber verilecekler listesinden çıkarır
        """

        for key in self.settings:
            if ctx.channel.id in self.settings[key]:
                self.settings[key].remove(ctx.channel.id)
        with open("channels.json", "w") as f:
            json.dump(self.settings, f)
async def setup(bot):
    await bot.add_cog(Haberci(bot=bot))
