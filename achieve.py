import requests
import json
from bs4 import BeautifulSoup

Steamkey = '9D8034447FC4F77028B94766E25A58C7'


def achieve(game):
  
    soup = BeautifulSoup(requests.get('https://steamdb.info/search/?a=app&q=' + game + '&type=1&category=0').content, 'lxml')
    first = soup.find("tr", class_= "app")

    achievements = json.loads(requests.get('http://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/?key=' + Steamkey + '&appid=' 
    + first.find('a').contents[0]).content)['game']['availableGameStats']['achievements']

    achievearray = [] 

    for x in range (0, len(achievements)):
        try:
            achievearray.append(achievements[x]['displayName']  + ': ' + achievements[x]['description'])
        except:
            pass

    return  '\n'.join(achievearray)



    