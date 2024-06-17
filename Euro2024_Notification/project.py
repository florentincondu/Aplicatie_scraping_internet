# -*- coding: utf-8 -*-
import requests
from plyer import notification
import time
import json
import webbrowser

FOOTBALL_API_KEY = '097ab494621643829a7d1f1cba4fa521'

NEWS_API_KEY = '6368f55812f94137b2e82d45007560be'


NEWS_API_URL = 'https://newsapi.org/v2/everything'


STANDINGS_URL = 'https://api.football-data.org/v2/competitions/EC/standings'

def show_notification(title, message, url=None):
    notification.notify(
        title=title,
        message=message,
        app_name='Euro 2024 Notifier',
        timeout=10,
        app_icon='Logo.png',
        callback=lambda: open_url(url) if url else None
    )

def open_url(url):
    webbrowser.open(url)


def check_for_news():
    languages = ['en', 'ro']
    new_articles = []

    for lang in languages:
        params = {
            'q': 'Euro 2024',
            'language': lang,
            'sortBy': 'publishedAt',
            'apiKey': NEWS_API_KEY
        }

        response = requests.get(NEWS_API_URL, params=params)
        news_data = response.json()

        try:
            with open(f'latest_news_{lang}.txt', 'r') as f:
                latest_news = f.read().splitlines()
        except FileNotFoundError:
            latest_news = []

        for article in news_data['articles']:
            title = article['title']
            url = article['url']

            if title not in latest_news:
                new_articles.append((title, url))

        if new_articles:
            with open(f'latest_news_{lang}.txt', 'w', encoding='utf-8') as f:
                for article in news_data['articles']:
                    title = article['title']
                    f.write(title + '\n')


    for title, url in new_articles:
        show_notification('New Euro 2024 News!', title, url)

def check_for_standings():
    headers = {'X-Auth-Token': FOOTBALL_API_KEY}
    response = requests.get(STANDINGS_URL, headers=headers)
    standings_data = response.json()

    try:
        with open('latest_standings.json', 'r') as f:
            latest_standings = json.load(f)
    except FileNotFoundError:
        latest_standings = {}

    current_standings = standings_data

    if current_standings != latest_standings:
        with open('latest_standings.json', 'w') as f:
            json.dump(current_standings, f)
        show_notification('Euro 2024 Standings Update', 'The standings have been updated.')


while True:
    check_for_news()
    check_for_standings()
    time.sleep(300)
