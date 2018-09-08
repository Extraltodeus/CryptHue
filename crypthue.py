import requests
import threading
import json
import time
from qhue import Bridge

b = Bridge("bride_ip_address_here", "hashed_valid_username_here").lights
url = 'https://api.coinmarketcap.com/v2/ticker/'
lampe = 8
varia = 5
loopTime = 300
CMCid = 1975  #This ID is for Chainlink, put 1 if you want Bitcoin

def daemonizer(fName):
    try:
        daemon = threading.Thread(target=fName)
        daemon.daemon = True
        daemon.start()
    except Exception as e:
        pass

def getCoins(id):
    try:
        coins = requests.get(url+str(id)).json()
        with open('./coins.json', 'w') as fp:
            json.dump(coins, fp)
        return coins
    except Exception as e:
        time.sleep(60)
        return getCoins()

def variator(percentage,min,max,varia):
    hue = varia + percentage
    if hue > varia*2: hue = varia*2
    if hue < 0: hue = 0
    hue = hue*max/(varia*2)
    hue = int(hue)
    return hue

def huedicator(lampe,hue):
    b[lampe].state(transitiontime=100, on=True, hue=hue, sat=255, bri=40)

def cryptHue():
    while True:
        link = getCoins(CMCid)
        varDay = link['data']['quotes']['USD']['percent_change_24h']
        hue = variator(varDay,0,20000,varia)
        daemonizer(huedicator(lampe,hue))
        time.sleep(loopTime)

cryptHue()
