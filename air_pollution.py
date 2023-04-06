#get the API key
import requests, json

with open('keys.json') as f:
    keys = json.load(f)
api_key = keys['open_weather']['api_key'] 

#fill the latitude and longtitude information of London into the API call
url = f'http://api.openweathermap.org/data/2.5/air_pollution?lat=51.5002&lon=-000.1262&appid={api_key}'
r = requests.get(url)

#get current air quality index
parsed_data = json.loads(r.text)
# print(parsed_data)
air_quality_index = parsed_data['list'][0]['main']['aqi']
# print(air_quality_index)