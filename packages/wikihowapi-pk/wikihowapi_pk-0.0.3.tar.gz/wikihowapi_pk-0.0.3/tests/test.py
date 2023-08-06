from bs4 import BeautifulSoup
import urllib.request
import re

# content = urllib.request.urlopen("https://www.wikihow.com/Train-a-Dog")
content = urllib.request.urlopen("https://www.wikihow.com/Cook-Chicken")
read_content = content.read()

soup = BeautifulSoup(read_content, 'html.parser')

html = soup.find('div', {'class': "section video sticky"})
