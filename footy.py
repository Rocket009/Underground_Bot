import requests
import json
from private.config import footyKey
import os





""" url='https://api.football-data.org/v4/competitions/PL/standings'
headers = { 'X-Auth-Token': footyKey }

response= requests.get(url, headers=headers)

standings=response.json()['standings']


for (i) in range(0,20):
    team=standings[0]['table'][i]['team']['shortName']
    j=i+1
    print (str(j)+". "+team)
    if j==4 or j==17 or j==5:
        print('-----------------------')

 """


class footydb:


    def __init__(self) -> None:
      url='https://api.football-data.org/v4/competitions/PL/standings'
      headers= { 'X-Auth-Token': footyKey } 
      self.response= requests.get(url, headers=headers)

    
    def get_table(self):
        standings=self.response.json()['standings']
        table=[]
        for (i) in range(0,20):
            team=standings[0]['table'][i]['team']['shortName']
            j=i+1
            table.append(str(j)+". "+team)
            if j==4 or j==17 or j==5:
                table.append('-----------------------')
        return table

football=footydb()
print(football.get_table())




