# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import requests   
import json  
sess = requests.Session()

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
parameters = {
 "status":"SCHEDULED"
}
Headers = {
    "X-Auth-Token":"4ee5678001c048628402771424ad3337"
}
mydict={}
#response = requests.get("https://itunes.apple.com/search?",params=parameters)
response = requests.get("https://api.football-data.org/v2/competitions/", headers=Headers)
""" for i in response.json()['results']:
    print(i['primaryGenreName']) """

print(response.status_code)
for i in response.json()['competitions']:
    mydict[i['name']]= i['id']
    #print(i['name'] , i['id'])
print("===========================")
print(mydict["Premier League"])
print("===========================")
response = requests.get("https://api.football-data.org/v2/competitions/"+ str(mydict['UEFA Champions League'])+"/matches", headers=Headers,params=parameters)
for i in response.json()['matches']:
    print(i['utcDate'],i['homeTeam']['name'],i['awayTeam']['name'])
#print(response.json())