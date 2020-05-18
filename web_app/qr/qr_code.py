import qrcode
import requests

# def uniqueNo(id1, times):
# 	n = (id1*id1)+times
# 	return n


# def qr_code(state, id1, times, username):
# 		n = uniqueNo(id1, times)
# 		p = username + "/" +str(state)+"/"+str(n)
# 		qr = qrcode.make(p)
# 		qr.save(username+'.png')
# 		return p






# # qr = qrcode.QRCode(
# # 	version=1,
# # 	box_size=15,
# # 	border=5
# # 	)

# # data = "https://youtube.com"
# ps = qr_code(1,3,1, 'sam')
# print (ps)
# Your payloads


# params = {
#     "X-Parse-Application-Id": "Ei9jVRLzJGUI7Vvop2vwpyyrW73B3NEABijvJr4c",
#     "X-Parse-REST-API-Key": "1WfLLcWCfb7dYRp7Q49VkiBUNQp0LJODnOOOvgiz"


# }


# url = 'https://parseapi.back4app.com/classes/IOT'


# # GET method, with URI parameters
# response = requests.get(url, params=params)

# print(response.url)

# # Get json data from a response.
# print(response.json())

import json
import http.client as httplib

connection = httplib.HTTPSConnection('parseapi.back4app.com', '443')

connection.connect()
connection.request('GET', '/classes/IOT', '', {
   "X-Parse-Application-Id": "Ei9jVRLzJGUI7Vvop2vwpyyrW73B3NEABijvJr4c",
   "X-Parse-REST-API-Key": "1WfLLcWCfb7dYRp7Q49VkiBUNQp0LJODnOOOvgiz"
})
result = json.loads(connection.getresponse().read())

print(result)
print(result['results'][0]['state'])