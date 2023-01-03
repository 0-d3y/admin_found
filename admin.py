import requests
import os
import  webbrowser
os.system("clear")

#======== color ======#
la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
#======== color ======#

print("""\033[0;96m
░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗  ░██╗░░░░░░░██╗██████╗░
██╔══██╗██╔══██╗████╗░████║██║████╗░██║  ░██║░░██╗░░██║██╔══██╗
███████║██║░░██║██╔████╔██║██║██╔██╗██║  ░╚██╗████╗██╔╝██████╔╝
██╔══██║██║░░██║██║╚██╔╝██║██║██║╚████║  ░░████╔═████║░██╔═══╝░
██║░░██║██████╔╝██║░╚═╝░██║██║██║░╚███║  ░░╚██╔╝░╚██╔╝░██║░░░░░
╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝  ░░░╚═╝░░░╚═╝░░╚═╝░░░░░
            Channel Telegram : @TYG_YE
""")
webbrowser.open("https://t.me/TYG_YE")
url = input("\033[90m╔═══[root@Sami]\n╚══>>>   \033[32m")
print("\n\n")
lists = ['/wp-login.php','/admin/','/wp-config.php','/admin.php','/cpanal','/cpanal','','/wp-content/plugins/wp-useronline/','/wp-content/plugins/imagemagick-engine/','/wp-content/plugins/3dady-real-time-web-stats/','/admin/index.php'] 

for inn in lists:
    try:
      target_url = f"{url}{inn}"
      response = requests.get(target_url)
      if response.status_code == 200:
          print (f"\033[32m[+] {url}{inn} ==> Found")
          sami = open("sites.txt","a")
          sami.write(f"Ok : {url}{inn}")
          sami.close()
      else:
          print (f"\033[31m[-] {url}{inn} ==> Not Found")
      print("\n\n\033[0;96m[!] Save The Site File Name ==:> sites.txt")
    except:
      print("Error The Site https:// or http://")
      slact = input("Exit write (e) restart write (y) ?")
      if slact == "y":
          os.system("python admin.py")
          print("Exit Now ...")
os.system("exit")
