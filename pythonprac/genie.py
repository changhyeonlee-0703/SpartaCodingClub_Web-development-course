import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


songs= soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    song_title = song.select_one('td.info > a.title.ellipsis').text.strip()
    if '19금' in song_title:
        song_title=song_title.replace('19금','').strip()
        #song_title=song_title[3:].strip()

    song_rank = song.select_one('td.number').text[0:2].strip()

    song_artist = song.select_one('td.info > a.artist.ellipsis').text

    print(song_rank,end='. ')
    print(song_title, song_artist, sep=' - ')