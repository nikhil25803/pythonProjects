from email import contentmanager
from bs4 import BeautifulSoup
import requests
import re

# repository = input("Enter the repository you wan tot scrap: ")

URL = "https://github.com/nikhil25803/python_problems"
content = requests.get(url=URL).text
soup = BeautifulSoup(content, "html.parser")

# print(soup)

commits = soup.find(class_="d-none d-sm-inline").strong
# print(type(commits))
commit_count = commits.string
print(commit_count)


