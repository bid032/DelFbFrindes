

logo = """

 _______ _     ____ _______                  _             _             
|__   __| |   |___ \__   __|                (_)           | |            
   | |  | |__   __) | | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
   | |  | '_ \ |__ <  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
   | |  | | | |___) | | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
   |_|  |_| |_|____/  |_|\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_| 
					
		    TH3 TERMINATOR SCRIPT TOOL :")
		   Coded by Bido. => Abdallah Ahmed
		   https://www.facebook.com/bido.32
"""


print(logo)

import requests, json

# Delete friends Script :")
token = input("Enter Your Access Token >> ")

url = 'https://graph.facebook.com/me/friends?limit=5000&fields=id&access_token='+token+'&method=get'
res = requests.get(url)
for item in res.json()['data']:
	del_url = 'https://graph.facebook.com/me/friends/'+item[id]+'?limit=5000&fields=id&access_token='+token+'&method=delete'
	xres = requests.get(del_url)
	print(xres.json())