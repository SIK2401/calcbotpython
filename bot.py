import asyncio, discord
from discord.ext import commands
import os
sttxt = "%"
bot = commands.Bot(command_prefix=sttxt)

ertxt = "Error - %[금액] ex)2000원 일때 ->%2000"


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
                Person1 =  4.0;
                Person2 =  8.0;
                prise = float(CountNum[1])
       
                if (prise>1):
                    FCost = prise * 0.95;
                    FinalCost1 = ((FCost * Person1) - FCost) / Person1
                    TCost1 = int(FinalCost1)  
                    FinalCost2 = ((FCost * Person2) - FCost) / Person2
                    TCost2 = int(FinalCost2) 
                    FinalCost1_2 = (TCost1) / (Person1-1)
                    FinalCost2_2 = (TCost2) / (Person2-1)
                    ICost1 = int(FinalCost1_2)
                    BCost1 = int(TCost1 / 1.08)
                    Bdistutor1 =    int(BCost1/ (Person1-1))
                    ICost2 = int(FinalCost2_2)
                    BCost2 = int(TCost2 / 1.08)
                    Bdistutor2 =    int(BCost2/ (Person2-1))      
                     
                    if(ICost1 < 1):
                        ICost1 = 1                     
                    if(ICost2 < 1):
                        ICost2 = 1  
                    embed = discord.Embed(title = "결과", description = "4인 : " +  f'{TCost1}' + " \n\n" +"분배금 : " +  f'{ICost1}' +  "공팟가 : " +  f'{BCost1}' + " \n\n" +
                                                                        "8인 : " +  f'{TCost2}' + " \n\n" +"분배금 : " +  f'{ICost2}' +  "공팟가 : " +  f'{BCost2}' + " \n\n" + , color = 0x00ffff)
                    await channel.send(embed = embed)
                else :
                    embed = discord.Embed(title = "Error", description = "%[금액] \n\n" +"ex)2000원 일때 \n\n" +"%2000 \n\n" , color = 0xffc0cb)
                    await channel.send(embed = embed)
                    
                    
            except :
                embed = discord.Embed(title = "Error", description = "%[금액] \n\n" +"ex) 2000원 일때 \n\n" +"%2000 \n\n" , color = 0xffc0cb)
                await channel.send(embed = embed)
        else :
            name = message.content.split(sttxt)  
            strmsg = "저요"
            if(name[1].find('다')>-1 and name[1].find('윤')>-1):
                strmsg = "저요 저요 이이이이잉 저요"                
            else:
                if(name[1].find('던') >-1 and name[1].find('바')>-1):
                    strmsg = "이이이이이잉"
                else:
                    strmsg = "저요"
           
           
            await channel.send(strmsg)

      
    else:   # line29 가 아날때
       return None


    
bot.run(os.environ['token'])
