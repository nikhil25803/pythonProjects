import math
import requests
import json

def fetch_data(user_name):
    profile_url = "https://api.github.com/users/"+user_name
    read1 = requests.get(url = profile_url)
    user_data = read1.json()
    json_data_user = json.dumps(user_data, indent=4)
    with open(f"{user_name}.json", "w") as f1:

        f1.write(json_data_user)

        print("User details fetching ...")

        print(user_data["name"])
        print("Avatar URL: ", user_data["avatar_url"])
        print(user_data["location"])
        print(user_data["followers"])
        print(user_data["following"])
        print(user_data["created_at"])
        print(user_data["updated_at"])

        print("User deta fetched!\n")

    read2 = requests.get(url = user_data["repos_url"])
    repo_data = read2.json()
    json_data_repo = json.dumps(repo_data, indent=4)
    with open(f"{user_name}_repos.json", "w") as f2:

        f2.write(json_data_repo)

        print("Repo data fetching ...")

        num = int(user_data["public_repos"])


        for i in range(0, num):
            name = repo_data[i]["name"]
            print("Repository name:", name)
            print("Owned By: ", repo_data[i]["owner"]["login"])

            if repo_data[i]["fork"] == False:
                print("Forked")
            else:
                print("Created on: ", repo_data[i]["created_at"])
    
            print("Prime Language: ", repo_data[i]["language"])
            print("Fork Count: ", repo_data[i]["forks"])
            print("Stars Count: ", repo_data[i]["stargazers_count"])
            print("Watchers Count: ", repo_data[i]["watchers"])
            print("Issue Counts: ", repo_data[i]["open_issues_count"])


            read3 = requests.get(url = repo_data[i]["languages_url"])
            lang_data = read3.json()
            lang_data_repo = json.dumps(lang_data, indent=4)
            with open(f"{name}_langs.json", "w") as f3:

                f3.write(lang_data_repo)

                print(f"Fetching languages of the repo {name} ...")

                data2 = json.loads(lang_data_repo)
                key_list = []
                value_list = []
                for k in data2.keys():
                    key_list.append(k)
                for v in data2.values():
                    value_list.append(v)

                print("Languages used are: ")
                for i in range(0, len(key_list)):
                    print(key_list[i], math.ceil(value_list[i]/sum(value_list)*100))

                print(f"Fetching languages of the repo {name} fetched {i}\n")
                

        print("Repo data have been fetched\n\n")

fetch_data("nikhil25803")