import json
import requests
file = open("nikhil25803_repos.json")
data = json.load(file)
print(type(data))

for i in range(0,25):
    print("Repository name:", data[i]["name"])
    print("Owned By: ", data[i]["owner"])

    if data[i]["fork"] == False:
        print("Forked")
    else:
        print("Created on: ", data[i]["created_at"])
    
    print("Prime Language: ", data[i]["languages"])
    print("Fork Count: ")
    print("Stars Count: ")
    print("Watchers Count: ")
    print("Issue Counts: ")
    

    