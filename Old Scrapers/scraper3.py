from bs4 import BeautifulSoup
import requests as re
import time

url = 'https://transcripts.fandom.com/wiki/Guardians_of_the_Galaxy_Vol._2'

transcripts = []

html_text = re.get(url).text
soup = BeautifulSoup(html_text, 'lxml')
script = soup.find('div', class_='mw-parser-output')
lines = script.find_all('p')
for line in lines:
    transcripts.append(line.text)

s = ' '
s = s.join(transcripts)

myText = open('transcripts\\Guardians of the Galaxy Vol 2.txt', 'w',)
myText.write(s)
myText.close()