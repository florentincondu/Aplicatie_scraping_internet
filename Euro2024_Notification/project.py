import requests
from plyer import notification
import time
import json
import webbrowser
from datetime import datetime, timedelta
from win10toast_click import ToastNotifier

FOOTBALL_API_KEY = '097ab494621643829a7d1f1cba4fa521'
NEWS_API_KEY = '6368f55812f94137b2e82d45007560be'

NEWS_API_URL = 'https://newsapi.org/v2/everything'
MATCHES_URL = 'https://api.football-data.org/v2/competitions/EC/matches'

toaster = ToastNotifier()

def show_notification(title, message, url=None):
    if url:
        toaster.show_toast(
            title,
            message,
            duration=None,
            callback_on_click=lambda: open_url(url)
        )
    else:
        notification.notify(
            title=title,
            message=message,
            app_name='Euro 2024 Notifier',
            timeout=None,
        )

def open_url(url):
    webbrowser.open(url)

def check_for_news():
    languages = ['en', 'ro']
    new_articles = []

    for lang in languages:
        params = {
            'q': 'Euro 2024 football',
            'language': lang,
            'sortBy': 'publishedAt',
            'apiKey': NEWS_API_KEY
        }

        response = requests.get(NEWS_API_URL, params=params)
        news_data = response.json()

        try:
            with open(f'latest_news_{lang}.txt', 'r', encoding='utf-8') as f:
                latest_news = f.read().splitlines()
        except FileNotFoundError:
            latest_news = []

        for article in news_data.get('articles', []):
            title = article['title']
            url = article['url']

            if title not in latest_news and title != "[Removed]":
                new_articles.append((title, url))
                latest_news.append(title)

        if new_articles:
            with open(f'latest_news_{lang}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(latest_news))

    for title, url in new_articles:
        show_notification('New Euro 2024 News!', title, url)

def check_for_matches():
    headers = {'X-Auth-Token': FOOTBALL_API_KEY}
    response = requests.get(MATCHES_URL, headers=headers)
    matches_data = response.json()

    upcoming_matches = []

    for match in matches_data['matches']:
        match_time = datetime.fromisoformat(match['utcDate'].replace('Z', '+00:00'))
        time_to_match = match_time - datetime.now()

        if 0 < time_to_match.total_seconds() <= 3600:
            upcoming_matches.append(match)

    for match in upcoming_matches:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        match_time = datetime.fromisoformat(match['utcDate'].replace('Z', '+00:00')).strftime('%Y-%m-%d %H:%M:%S')

        message = f'{home_team} vs {away_team} starts at {match_time}'
        show_notification('Upcoming Euro 2024 Match', message)

while True:
    try:
        check_for_news()
        check_for_matches()
    except Exception as e:
        print(f"Error occurred: {str(e)}")

    time.sleep(60)
