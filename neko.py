# discord.pyのインポート
import discord
client = discord.Client()
# ねこくんのトークン設定
TOKEN =　'NjgxNzQ3OTk1MTU0NDQ4NDU4.XlS9dA.YurRox1N86zzL7l4hjZGzqdn3gw'
client = discord.Client()

# ログイン処理
@client.event
async def on_ready():
    msg = "おいすおいすー"
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# ねこくんお喋り処理
@client.event
async def on_message(message):
# 発言者がBOTなら無視
   if message.author.bot:
       return
   if message.content == 'ねこぴっぴ':
       await message.channel.send('なんですか,どーされましたかー？,呼んだ？')