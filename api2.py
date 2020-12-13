import requests
Headers = {
   "x-rapidapi-host": "api-football-beta.p.rapidapi.com",
   "x-rapidapi-key": "169a5a783fmsh50a8e0e96324e24p144dc5jsne4f6f8530565"
}
Params = {
    "type":"league"
}
mydict={}
response = requests.get("https://rapidapi.p.rapidapi.com/leagues", headers=Headers,params=Params)

print(response.status_code)
for i in response.json()['response']:
    #print(i , type(i))
    #print(i['league']['name'],i['league']['id'] )
    mydict[i['league']['name']+ "_" + i['country']['name']] = i['league']['id']


#print(mydict["Serie A_italy"])

response = requests.get("https://rapidapi.p.rapidapi.com/fixtures", headers=Headers,params={'league': mydict['Serie A_Italy'],'season':'2020',"date":"2020-10-04"})
for i in response.json()['response']:
    print(i)