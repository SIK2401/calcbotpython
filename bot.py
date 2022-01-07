import asyncio, discord
from discord.ext import commands
import os
sttxt = "%"
bot = commands.Bot(command_prefix=sttxt)

ertxt = "Error - %[인원] [금액] ex) 8인 2000원 일때 -> %8 2000"


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online) #온라인\
    await bot.change_presence(activity=discord.Game(name="우다윤은 식사"))
    print("We have loggedd in as {0.user}".format(bot))


@bot.event

async def on_message(message):
    # 받은 메시지의 author 가 bot 인 경우 return
    if message.author.bot:
        return None

    # 답장할 채널은 메세지 받은 채널로 설정

    channel = message.channel

    if message.content.startswith(sttxt):   # message 의 contest 가 '#커맨드' 로 시작할때     
        if(message.content.find("죽이실분")==-1):
            commandr = message.content.split(sttxt)     
            CountNum = commandr[1].split()
       
            try:
                Person =  float(CountNum[0])
                prise = float(CountNum[1])
       
                if (Person > 1 and prise>1):
                    FCost = prise * 0.95;
                    FinalCost = ((FCost * Person) - FCost) / Person
                    TCost = int(FinalCost)         
                    FinalCost2 = (FCost) / Person
                    ICost = int(FinalCost2)
                    BCost = int(FinalCost * 0.93)   

                    
                    
                    if(ICost < 1):
                        ICost = 1
                    
      
                    embed = discord.Embed(title = "결과", description = "손익분기 : " +  f'{TCost}' + " \n\n" +"분배금 : " +  f'{ICost}' + " \n\n" +"1입찰이득 : " +  f'{BCost}' + " \n\n" , color = 0x00ffff)
                    await channel.send(embed = embed)
                else :
                    embed = discord.Embed(title = "Error", description = "%[인원] [금액] \n\n" +"ex) 8인 2000원 일때 \n\n" +"%8 2000 \n\n" , color = 0xffc0cb)
                    await channel.send(embed = embed)
            except :
                embed = discord.Embed(title = "Error", description = "%[인원] [금액] \n\n" +"ex) 8인 2000원 일때 \n\n" +"%8 2000 \n\n" , color = 0xffc0cb)
                await channel.send(embed = embed)
        else :
            name = message.content.split(sttxt)  
            strmsg = "저요"
            if(name[1].find('다')>-1 and name[1].find('윤')>-1):
                strmsg = "저요 저요 제발 저요"                
            else:
                if(name[1].find('던') >-1 and name[1].find('바')>-1):
                    strmsg = "이이이이이잉"
                else:
                    strmsg = "저요"
           
            await channel.send(strmsg)

      
    else:   # line29 가 아날때
       return None


    
bot.run(os.environ['token'])
