import os
import discord
import aiohttp
import random
from keep_alive import keep_alive   # 使機器人活著的 code

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# 設定機器人狀態
activity = discord.Activity(type=discord.ActivityType.watching, name="\"兔田佩克拉\"直播")
client = discord.Client( intents = intents,  activity=activity)

# 啟動 client(bot)
@client.event
async def on_ready():
    print('I am >< ', client.user)
  
    # channel = client.get_channel(1007296202057982045)
    # text= "YOUR_MESSAGE_HERE"
    # Moji = await channel.send(text)
    # await Moji.add_reaction('🏃')

# 訊息對話 ================================================
@client.event
async def on_message(message):
    if message.author == client.user:
          return
    # if message.content == '身份組':
    #   await message.channel.send(
    #     '請選擇你的身份 : \n\n'
    #     '- 🧝‍♂️ 冒險者: 社群的朋友們~\n\n'
    #     '- 🧙‍♂️ 宗師: 講師、教學人員~\n\n'
    #     '- 🕵️ 友校大使: 其他學校的朋友們~'
    #   )

    if message.content.startswith('給我錢') or message.content.endswith('給我錢'):
      await message.add_reaction('\U0001F4B5')
      return
  
    # 限制 bot 發出 & 回應訊息的 channel
    channels = ['bot-test']
    if str(message.channel) in channels:
      if message.author == client.user:
          return

      # 指令說明:
      elif message.content == "!ELM.help":
        await message.channel.send(
          '現有指令:\n'
          '> !ELM你是不是在    [玩,看,聽]    [\'ELM的狀態\']  : 更改ELM狀態\n '
          '> !ELM.meme  : random meme (if not working , just try it again~ )\n '
          )
        return
        
      # 設定 bot 狀態
      if message.content.startswith('!ELM你是不是在'):
        x = message.content.split(" ",4)[1:]  
        
        if(len(x) != 2):
          await message.channel.send(
            'Error : 你的格式不對喔~ \n'
            '!ELM你是不是在    [玩,看,聽]    [\'ELM的狀態\']'
          )
          return          
        
        # riptext = x[:4] + ['']*(4-len(x))
        if(x[0] == '玩'):
          activity = discord.Game(name=x[1])
        elif(x[0] == '看'):
          # print("ELM看")
          activity = discord.Activity(type=discord.ActivityType.watching, name=x[1])
        elif(x[0] == '聽'):
          activity = discord.Activity(type=discord.ActivityType.listening, name=x[1])
          # print("ELM聽")
        else:
          await message.channel.send(
            'Error : 你的格式不對喔~ \n'
            '!ELM你是不是在   [玩,看,聽]   [\'ELM的狀態\']'
          )
          return  

        await client.change_presence(status=discord.Status.idle,             activity=activity)
        return


      # 機器人發出隨機 meme
      if message.content == '!ELM.meme':
        embed = discord.Embed(title="", description="")
        async with aiohttp.ClientSession() as cs:
          async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 24)]['data']['url'])
            await message.channel.send(embed=embed)
            return
        
      # hi
      if message.content.startswith('哈摟') or message.content.startswith('hi'):
          await message.channel.send(f'嗨 {message.author.name} ~唉...我窮得只剩錢了... !!')
          return
      
      # 無此指令
      else:
        await message.channel.send(
          '沒有這個指令欸QQ\n'
          '使用  !ELM.help 查詢現有指令 ~ \n'
          )
        return

# 歡迎新人 =================================================
@client.event
async def on_member_join(member):
    guild = member.guild
    print("join!")
    print(f"{member.mention}")
    # if guild.system_channel is not None:
    to_send = f'歡迎 {member.mention} 來到 {guild.name} !! \U0001F61D \U0001F61D \n記得選擇你的身分組 ~'
  
    await guild.system_channel.send(to_send)


# 選擇身分組 ==================================================
@client.event
async def on_raw_reaction_add( payload ):
  # 指定特定留言
  text_id = 1010241128743829625
  if payload.message_id == text_id:  
    
    # 冒險者
    if str(payload.emoji) == '🧝‍♂️' :
      print("ooooooo")    
      guild = client.get_guild(payload.guild_id)  # 獲得伺服器
      role = guild.get_role(1010029791589716048)  # 取得身分組 
      await payload.member.add_roles(role)        # 設定身分組
      await payload.member.send(f"你現在是 {guild.name} 的 [{role}] 啦!!")  # 私訊告知身分組訊息  

    # 宗師
    if str(payload.emoji) == '🧙‍♂️' :
      print("ooooooo")    
      guild = client.get_guild(payload.guild_id)  # 獲得伺服器
      role = guild.get_role(1010030573823213659)  # 取得身分組 
      await payload.member.add_roles(role)        # 設定身分組
      await payload.member.send(f"你現在是 {guild.name} 的 [{role}] 啦!!")  # 私訊

    # 友校使者
    if str(payload.emoji) == '🕵️' :
      print("ooooooo")    
      guild = client.get_guild(payload.guild_id)  # 獲得伺服器
      role = guild.get_role(1010031067048190082)  # 取得身分組 
      await payload.member.add_roles(role)        # 設定身分組
      await payload.member.send(f"你現在是 {guild.name} 的 [{role}] 啦!!")  # 私訊
      

# 移除身分組
@client.event
async def on_raw_reaction_remove( payload ):
  # 指定特定留言
  text_id = 1010241128743829625
  if payload.message_id == text_id:

    # 冒險者
    if str(payload.emoji) == '🧝‍♂️' :
      print("-----------")    
      guild = client.get_guild(payload.guild_id)  # 獲得伺服器
      member = guild.get_member( payload.user_id )  # 取得移除人的身分
      role = guild.get_role(1010029791589716048)  # 取得身分組 
      await member.remove_roles(role)     # 設定身分組
      await member.send(f"你取消成為 {guild.name} 的 [{role}] 了喔 TT")  # 私訊

    # 宗師
    if str(payload.emoji) == '🧙‍♂️' :
      print("-----------")    
      guild = client.get_guild(payload.guild_id)  # 獲得伺服器
      member = guild.get_member( payload.user_id )  # 取得移除人的身分
      role = guild.get_role(1010030573823213659)  # 取得身分組 
      await member.remove_roles(role)     # 設定身分組
      await member.send(f"你取消成為 {guild.name} 的 [{role}] 了喔 TT")  # 私訊  

    # 有效使者
    if str(payload.emoji) == '🕵️' :
      print("-----------")    
      guild = client.get_guild(payload.guild_id)  # 獲得伺服器
      member = guild.get_member( payload.user_id )  # 取得移除人的身分
      role = guild.get_role(1010031067048190082)  # 取得身分組 
      await member.remove_roles(role)     # 設定身分組
      await member.send(f"你取消成為 {guild.name} 的 [{role}] 了喔 TT")  # 私訊  

# ==========================================================================

# 使伺服器活著
keep_alive()

# 讀取 Replit 的 Secreat Code
token = os.environ['TOKEN']

try:
  client.run(token)             # 運作機器人
except:
  print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n") 
  os.system("restarter.py")     # 連到另一文件，重啟此 main.py
  os.system("kill 1")           # 殺死進程
