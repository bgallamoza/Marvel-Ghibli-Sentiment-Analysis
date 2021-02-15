from bs4 import BeautifulSoup
import requests as re
import time

movies = [
    'Spirited Away',
    'Princess Mononoke',
    'From Up on Poppy Hill',
    'The Secret World of Arietty',
    'Ponyo',
    'Whisper of the Heart',
    'Porco Rosso',
    'Kiki\'s Delivery Service',
    'My Neighbor Totoro',
    'Castle in the Sky',
    'Captain America Civil War',
    'Doctor Strange',
    'Guardians of the Galaxy Vol 2',
    'Spider-Man Homecoming',
    'Thor Ragnarok',
    'Black Panther',
    'Avengers Infinity War',
    'Ant-Man and the Wasp',
    'Captain Marvel',
    'Spider-Man Far From Home'
]

urls = [
    'https://www.scripts.com/script.php?id=spirited_away_17770&p=',
    'https://www.scripts.com/script.php?id=princess_mononoke_13983&p=',
    'https://www.scripts.com/script.php?id=from_up_on_poppy_hill_11969&p=',
    'https://www.scripts.com/script.php?id=the_secret_world_of_arrietty_11617&p=',
    'https://www.scripts.com/script.php?id=gake_no_ue_no_ponyo_%2528ponyo_on_the_cliff_by_the_sea%2529_8743&p=',
    'https://www.scripts.com/script.php?id=whisper_of_the_heart_13792&p=',
    'https://www.scripts.com/script.php?id=porco_rosso_12054&p=',
    'https://www.scripts.com/script.php?id=kiki%2527s_delivery_service_11747&p=',
    'https://www.scripts.com/script.php?id=my_neighbor_totoro_22062&p=',
    'https://www.scripts.com/script.php?id=castle_in_the_sky_5173&p=',
    'https://www.scripts.com/script.php?id=captain_america%253A_civil_war_5035&p=',
    'https://www.scripts.com/script.php?id=doctor_strange_7043&p=',
    'https://www.scripts.com/script.php?id=guardians_of_the_galaxy_vol._2_1437&p=',
    'https://www.scripts.com/script.php?id=spider-man%253A_homecoming_18658&p=',
    'https://www.scripts.com/script.php?id=thor%253A_ragnarok_21816&p=',
    'https://www.scripts.com/script.php?id=black_panther_4193&p=',
    'https://www.scripts.com/script.php?id=avengers%253A_infinity_war_3317&p=',
    'https://www.scripts.com/script.php?id=ant-man_and_the_wasp_2969&p=',
    'https://www.scripts.com/script/captain_marvel_(2019)_24523&p=',
    'https://www.scripts.com/script.php?id=spider-man%253A_far_from_home_24485&p='
    ]

transcripts = []

for url in urls:
    num = 1
    transcript = []
    while num:
        time.sleep(10)
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