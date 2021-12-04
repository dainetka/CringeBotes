import discord,sys
bot = discord.Client()


@bot.event
async def on_message(message):
    if(message.author.id==412663918780219394):
        try:
            ans = eval(message.content)
            await message.channel.send(ans)
        except Exception as e:
            print(e)

bot.run(sys.argv[1])