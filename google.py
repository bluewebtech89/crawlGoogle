#developer - rajat
#version - python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re

#Forming query
query=input("query>>")
query=query.strip().split()
query="+".join(query)

html = "https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl"
req = urllib.request.Request(html, headers={'User-Agent': 'Mozilla/5.0'})

soup = BeautifulSoup(urlopen(req).read(),"html.parser")

#Regex
reg=re.compile(".*&sa=")

links = []
#Parsing web urls
for item in soup.find_all('h3', attrs={'class' : 'r'}):
    
    line = (reg.match(item.a['href'][7:]).group())
    links.append(line[:-4])


#printing links scrapped as a list
print(links)

