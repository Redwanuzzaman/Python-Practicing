"""
 Find geolocation information from an IP address:
For this problem, the main objective is to write a program that finds geolocation information about an IP. This programming assignment is nice, because it is practical, and could indeed be something that happens in the workplace.
The requirements are listed below:
The program will ask for an IP as input from a user. Now use the API of http://ip-api.com and find geolocation
information about it. Return the city, region name and country as the following output: city, region name(country).

Sample Input:
63.70.164.200
168.12.13.1
Sample Output:
Lincoln (Highlands), Nebraska (United States)
Atlanta (150), Georgia (United States)
"""


import requests
import json
 
ip = input()
 
api = "http://i...content-available-to-author-only...i.com/json/{}".format(ip)
 
ip_details = requests.get(api).content
ip_details = json.loads(ip_details.decode('utf-8'))
 
print("{}, {}({})".format(ip_details['city'], ip_details['regionName'], ip_details['country']))
