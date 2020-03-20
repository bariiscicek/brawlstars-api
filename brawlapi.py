import requests
class Player:
    def __init__(self,player_tag,token):
        headers={
            'authorization':token,
        }
        Ver=requests.get('https://api.brawlstars.com/v1/players/%23'+player_tag,headers=headers)
        infos=Ver.json()
        self.token=token
        self.response=infos
        if Ver.status_code==200:
            self.tag=infos['tag']
            self.name=infos['name']
            self.trophies=infos['trophies']
            self.highestTrophies=infos['highestTrophies']
            self.expLevel=infos['expLevel']
            self.expPoints=infos['expPoints']
            self.isQualifiedFromChampionshipChallenge=infos['isQualifiedFromChampionshipChallenge']
            self.vs3Victories=infos['3vs3Victories']
            self.soloVictories=infos['soloVictories']
            self.duoVictories=infos['duoVictories']
            self.bestRoboRumbleTime=infos['bestRoboRumbleTime']
            self.bestTimeAsBigBrawler=infos['bestTimeAsBigBrawler']
            self.club=infos['club']
            self.brawlers=infos['brawlers']
            try:
                self.nameColor=infos['nameColor']
                self.highestPowerPlayPoints=infos['highestPowerPlayPoints']
            except:
                pass
        else:
            print(infos['message'])
    def getClub(self):
        return Club(self.club['tag'][1:],self.token)
    def getBrawlers(self):
        import pandas as pd
        df=pd.DataFrame(columns=['Brawler','Power','Trophy','HighestTrophy','StarPower1','StarPower2','Gain'])
        for i in self.brawlers:
            sps=i['starPowers']
            l=len(sps)
            if l==2:
                sp1=sps[0]['name']
                sp2=sps[1]['name']
            elif l==1:
                sp1=sps[0]['name']
                sp2='None'
            else:
                sp1='None'
                sp2='None'
            trp=i['trophies']
            if trp<550:
                gain=0
            elif trp<600:
                gain=70
            elif trp<650:
                gain=120
            elif trp<700:
                gain=160
            elif trp<750:
                gain=200
            elif trp<800:
                gain=220
            elif trp<850:
                gain=240
            elif trp<900:
                gain=260
            elif trp<950:
                gain=280
            elif trp<1000:
                gain=300
            elif trp<1050:
                gain=320
            elif trp<1100:
                gain=340
            elif trp<1150:
                gain=360
            elif trp<1200:
                gain=380
            elif trp<1250:
                gain=400
            elif trp<1300:
                gain=420
            elif trp<1350:
                gain=440
            elif trp<1400:
                gain=460
            else:
                gain=480
            df=df.append({
                'Brawler':i['name'],
                'Power':i['power'],
                'Trophy':i['trophies'],
                'HighestTrophy':i['highestTrophies'],
                'StarPower1':sp1,
                'StarPower2':sp2,
                'Gain':gain
            },ignore_index=True)
        return df
    def getResponse(self):
        return self.respons
    def getBattleLog(self):
        headers={
            'authorization':self.token,
        }
        url='https://api.brawlstars.com/v1/players/%23'+self.tag[1:]+'/battlelog'
        Ver=requests.get(url,headers=headers)
        return Ver.json()['items']
class Club():
    def __init__(self,club_tag,token):
        headers={
            'authorization':token,
        }
        Ver=requests.get('https://api.brawlstars.com/v1/clubs/%23'+club_tag,headers=headers)
        infos=Ver.json()
        self.token=token
        self.response=infos
        if Ver.status_code==200:
            self.tag=infos['tag']
            self.name=infos['name']
            self.description=infos['description']
            self.type=infos['type']
            self.requiredTrophies=infos['requiredTrophies']
            self.trophies=infos['trophies']
            self.members=infos['members']
        else:
            print(infos['message'])
    def getPlayers(self):
        return self.members
    def getResponse(self):
        return self.response
def playerRanking(country,token):
    headers={
        'authorization':token,
    }
    Ver=requests.get('https://api.brawlstars.com/v1/rankings/'+country+'/players',headers=headers)
    return Ver.json()['items']
def clubRanking(country,token):
    headers={
        'authorization':token,
    }
    Ver=requests.get('https://api.brawlstars.com/v1/rankings/'+country+'/clubs',headers=headers)
    return Ver.json()['items']
def brawlerRanking(country,token,brawler):
    brawlist={
    'shelly':16000000,
    'shelly':16000001,
    'shelly':16000002,
    'shelly':16000003,
    'shelly':16000004,
    'shelly':16000005,
    'shelly':16000006,
    'shelly':16000007,
    'shelly':16000008,
    'shelly':16000009,
    'shelly':16000010,
    'shelly':16000011,
    'shelly':16000012,
    'shelly':16000013,
    'shelly':16000014,
    'shelly':16000015,
    'shelly':16000016,
    'shelly':16000017,
    'shelly':16000018,
    'shelly':16000019,
    'shelly':16000020,
    'shelly':16000021,
    'shelly':16000022,
    'shelly':16000023,
    'shelly':16000024,
    'shelly':16000025,
    'shelly':16000026,
    'shelly':16000027,
    'shelly':16000028,
    'shelly':16000029,
    'shelly':16000030,
    'shelly':16000031,
    'shelly':16000032,
    'shelly':16000033,
    'shelly':16000034
    }
    brawlid=brawlist[brawler]
    headers={
        'authorization':token,
    }
    Ver=requests.get('https://api.brawlstars.com/v1/rankings/'+country+'/brawlers/'+str(brawlid),headers=headers)
    return Ver.json()['items']
