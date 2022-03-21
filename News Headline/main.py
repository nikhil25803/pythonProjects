import imp
from urllib import response
import requests

# For web Scraping
from bs4 import BeautifulSoup

# Send the mail
import smtplib

# Email Body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# system date and time manipulation
import datetime


content =''

# Extracting Stories
def extract_news(url):
    # Extract fromt page

    #Passing URL
    print("Extrating the url: ")

    # Creating titles
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'+'*50'+'<br>')
    response = requests.get(url)

    # Creating soup to extract title
    soup = BeautifulSoup(content, 'html.parser')

    for i, tag in enumerate(soup.find_all('td', attrs={'class':'title', 'valign':''})):

        cnt += ((str(i+1)+'::'+ tag.text + "\n" + "<br>") if tag.text!= 'More' else '')

    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>---------------<br>')
content += ('<br><br>End of the Messages')

print(cnt)