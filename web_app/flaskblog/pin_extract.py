import requests
import twilio
import twilio.rest
from twilio.rest import Client
location = []
lat1 = []
lang1 = []
dict1 = {}
URL = "https://geocode.search.hereapi.com/v1/geocode"
api_key = 'S3TCHS5oiquFZXVeAbTdJkAYuqxYjddr_RW2lusbWu8' # Acquire from developer.here.com
x = ''


account_sid = 'ACf6c4c0dc88c74c46eb7688882c8f6a25'
auth_token = '458aee4db31a7e3fe20f25877d3f7946'
client = Client(account_sid, auth_token)

message = client.messages.create(
                            body='Hi there!',
                            from_='+18622454115',
                            to='+91'+'8617739525'
                        )

print(message.sid)

# def loc(x):

# 	PARAMS = {'apikey':api_key,'q':x}
# 	r = requests.get(url = URL, params = PARAMS) 
# 	data = r.json()

# 	if (data['items']!=[]): 
# 		# lat1.append(data['items'][0]['position']['lat'])
# 		# lang1.append(data['items'][0]['position']['lng'])
# 		# print(x)
# 		# print(lang1)
# 		dict1[x] = []
# 		dict1[x].append(data['items'][1]['position']['lat'])
# 		dict1[x].append(data['items'][1]['position']['lng'])


# for i in range (700030, 700032):
# 	location.append(i)
# 	# location = [700130, 700129, 700131, 700140]

# for i in range(0, len(location)):
# 	loc(location[i])

# print(dict1)


# from math import sin, cos, sqrt, atan2, radians

# # approximate radius of earth in km
# R = 6373.0

# lat1 = radians(52.2296756)
# lon1 = radians(21.0122287)
# lat2 = radians(52.406374)
# lon2 = radians(16.9251681)

# dlon = lon2 - lon1
# dlat = lat2 - lat1

# a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
# c = 2 * atan2(sqrt(a), sqrt(1 - a))

# distance = R * c

# print("Result:", distance)
# print("Should be:", 278.546, "km")
