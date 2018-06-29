from requests import get
import re
r = get('http://192.168.31.200:8080/getSonars')

# data = json.loads(r.text)
# # print(data)
# # print(json.loads(data['result'])['sonar0'])
#
# print(re.findall('"sonar\d":"\d.\d+"', data['result']))

data = []

for i in re.findall('"sonar\d":"\d.\d+"', r.json()['result']):
    # print(i)
    data.append(i[10:-1])
print(data)


