import requests 
from bs4 import BeautifulSoup
from requests.models import Response


url = "https://www.reuters.com/article/us-health-coronavirus-global-deaths/global-coronavirus-deaths-pass-agonizing-milestone-of-1-million-idUSKBN26K08Y"
page = requests.get(url) # fetches URL from page. 
status = requests.status_codes  

print (Response.content)   # Returns response object from URL  

soup = BeautifulSoup(page, 'html parser')
print (soup.prettify()) # prints all html tags and parse tree 

title = soup.find('title')
content = soup.find('content')
