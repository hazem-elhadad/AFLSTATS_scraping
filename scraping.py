import requests
import json
import pandas as pd
url = "https://api.afl.com.au/statspro/playersStats/seasons/CD_S2023014?includeBenchmarks=false"

payload={}
headers = {
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'x-media-mis-token': 'c301c47f56f090f58ea55da2c94d20ad',
  'Referer': 'https://www.afl.com.au/',
  'sec-ch-ua-mobile': '?1',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
  'sec-ch-ua-platform': '"Android"',
  'Cookie': 'JSESSIONID=ED84F88388D2A17D27789655B8ABB923'
}

r = requests.get( url, headers=headers)

player_data = r.json()
df = pd.json_normalize(player_data['players'])
df.to_csv('AFLplayersData.csv' , index= False)