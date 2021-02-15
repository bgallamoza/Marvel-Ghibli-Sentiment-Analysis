from bs4 import BeautifulSoup
import requests as re
import time

movies = [
    'Howls Moving Castle',
    'Spirited Away'
]

urls = [
    'https://www.scripts.com/script.php?id=sen_to_chihiro_no_kamikakushi_howl%27s_moving_castle_17771&p=',
    'https://www.scripts.com/script.php?id=spirited_away_17770&p='
    ]

transcripts = []

for url in urls:
    num = 1
    transcript = []
    while num:
        time.sleep(5)
        new_url = url + str(num)
        html_text = re.get(new_url).text
        soup = BeautifulSoup(html_text, 'lxml')
        check = soup.find('h1')

        if check.text != 'Welcome to Scripts.com':
            script = soup.find('blockquote')
            lines = script.find_all('p')
            for line in lines:
                transcript.append(line.text)
            num += 1
            print(num)
            continue
        else:
            break

    s = ' '
    s = s.join(transcript)
    transcripts.append(s)

for text, movie in zip(transcripts, movies):
    myText = open(f'transcripts\\' + movie + '.txt', 'w')
    myText.write(text)
    myText.close()

print('Done!')