import soundcloud
import requests
import time

def upload_track(title, url):

    querystring = {
        "id": url
        }

    headers = {
        "X-RapidAPI-Key": "api key here",
        "X-RapidAPI-Host": "host here"
    }

    response = requests.get('https://youtube-mp36.p.rapidapi.com/dl', headers=headers, params=querystring)

    if response.json()['status'] != 'ok':
        time.sleep(3)
        response = requests.get('https://youtube-mp36.p.rapidapi.com/dl', headers=headers, params=querystring)
        mp3_url = (response.json()['link'])

    else:
        mp3_url = (response.json()['link'])
        print(mp3_url)

    response = requests.get(mp3_url)

    with open('track.mp3', 'wb') as f:
        f.write(response.content)


    client = soundcloud.Client(access_token='OAUTH access token here')
    track = client.post('/tracks', track={
        'title': title,
        'sharing': 'public',
        'asset_data': open('track.mp3', 'rb')
    })