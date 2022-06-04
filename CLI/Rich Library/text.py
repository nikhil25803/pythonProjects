import requests

url = "https://twitter-followers.p.rapidapi.com/elonmusk/profile"

headers = {
	"X-RapidAPI-Host": "twitter-followers.p.rapidapi.com",
	"X-RapidAPI-Key": "dc7e47c1c0mshe1fb9e4db7f2448p107746jsn740937a93e85"
}

response = requests.request("GET", url, headers=headers)

print(response.text)