#!/usr/bin/python3

import sys,getopt,urllib.request,urllib.parse,base64,requests

banner = """
  _   _            _    _____ _          ____              _   _ _       _     ____        __   ____            _               ____                _             
 | | | | __ _  ___| | _|_   _| |__   ___| __ )  _____  __ | | | (_) __ _| |__ |  _ \  ___ / _| | __ )  __ _  __| | __ _  ___   / ___|_ __ ___  __ _| |_ ___  _ __ 
 | |_| |/ _` |/ __| |/ / | | | '_ \ / _ \  _ \ / _ \ \/ / | |_| | |/ _` | '_ \| | | |/ _ \ |_  |  _ \ / _` |/ _` |/ _` |/ _ \ | |   | '__/ _ \/ _` | __/ _ \| '__|
 |  _  | (_| | (__|   <  | | | | | |  __/ |_) | (_) >  <  |  _  | | (_| | | | | |_| |  __/  _| | |_) | (_| | (_| | (_| |  __/ | |___| | |  __/ (_| | || (_) | |   
 |_| |_|\__,_|\___|_|\_\ |_| |_| |_|\___|____/ \___/_/\_\ |_| |_|_|\__, |_| |_|____/ \___|_|   |____/ \__,_|\__,_|\__, |\___|  \____|_|  \___|\__,_|\__\___/|_|   
                                                                   |___/                                          |___/                                           

By Flangvik
																   """
def generateHTB(htbId):
        print(banner)
        htbUrl = "https://www.hackthebox.com/badge/" + htbId

        headers = {
          'Host': 'www.hackthebox.com',
          'User-Agent': 'curl/8.3.0',
          'Accept': '*/*'
        }

        #signatureReq = urllib.request.urlopen(urllib.request.Request(htbUrl, headers={ 'Host' : 'www.hackthebox.com', 'User-Agent' : 'curl/8.3.0', 'Accept' : '*/*' }))
        #signatureRaw =  signatureReq.read().decode('utf-8')
        #signatureBase64 = signatureRaw.split('document.write(window.atob("')[1].split('"))')[0]

        response = requests.get(htbUrl, headers=headers)
        if response.status_code == 200 or response.status_code == 403:
          signatureRaw = response.text
          signatureBase64 = signatureRaw.split('document.write(window.atob("')[1].split('"))')[0]
          # Use signatureBase64 variable as needed
          signatureHTML = base64.b64decode(signatureBase64).decode('utf-8')

          signatureHTML = signatureHTML.replace('https://www.hackthebox.com/images/screenshot.png',"https://www.ppeinecke.de/custom_assets/images/htb_crosshair.png")
          signatureHTML = signatureHTML.replace('_thumb.png',".png")
          signatureHTML = signatureHTML.replace('https://www.hackthebox.com/images/star.png',"https://www.ppeinecke.de/custom_assets/images/star.png")
          signatureHTML = signatureHTML.replace('url(https://www.hackthebox.com/images/icon20.png); ',"url('https://www.ppeinecke.de/custom_assets/images/htb_logo.webp'); background-size: 20px;")

          signatureFile = open(htbId + '.html','w')
          signatureFile.write(signatureHTML)
          signatureFile.close()

          print("Check " + htbId + ".html!")

        else:
          print("Failed to fetch the data. Status code:", response.status_code)
          print("Response: ", response.text)

try:
    options, remainder = getopt.getopt(
        sys.argv[1:],
        '',
        ['htbid='])
except getopt.GetoptError as err:
    print ('HTBHDBadgeGenerator.py -htbid <HackTheBoxProfileID>')
    sys.exit(1)

for opt, arg in options:
    if opt == '--htbid':
        htbId = arg

generateHTB(htbId)
