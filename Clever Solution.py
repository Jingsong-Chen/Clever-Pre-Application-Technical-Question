# solution in Python
# API Reference: https://dev.clever.com/reference
import requests
url = "https://api.clever.com/v3.0/sections"
querystring = {"limit":"500"}
headers = {
    "Accept": "application/json",
    "Authorization": "Bearer DEMO_TOKEN"
}
response = requests.request("GET", url, headers=headers, params=querystring).json()

total_students = 0
for section in response['data']:
    total_students += len(section['data']['students'])
print(total_students)
print(len(response['data']))
print(total_students / len(response['data']))

# 8966
# 379
# 23.65699208443272
