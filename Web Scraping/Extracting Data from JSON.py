from urllib.request import urlopen
import json

address = input('Enter location: ')
data = urlopen(address).read().decode()

# data collected from web represents as a JSON string
json_data = json.loads(data)

ans = 0
for item in json_data["comments"]:
    # print(item['count'])
    ans += int(item["count"])

print(ans)
