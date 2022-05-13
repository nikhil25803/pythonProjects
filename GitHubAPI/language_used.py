import math
import json
import requests

r = requests.get(url="https://api.github.com/repos/nikhil25803/blog_deploy/languages")
data = r.json()
json_data = json.dumps(data, indent=4)

data2 = json.loads(json_data)

key_list = []
value_list = []
for k in data2.keys():
    key_list.append(k)
for v in data2.values():
    value_list.append(v)

print("Languages used are: ")
for i in range(0, len(key_list)):
    print(key_list[i], math.ceil(value_list[i]/sum(value_list)*100))