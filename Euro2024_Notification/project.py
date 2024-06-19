# -*- coding: utf-8 -*-
import requests
from plyer import notification
import time
import json
import webbrowser
from win10toast_click import ToastNotifier


FOOTBALL_API_KEY = '097ab494621643829a7d1f1cba4fa521'
NEWS_API_KEY = '6368f55812f94137b2e82d45007560be'

NEWS_API_URL = 'https://newsapi.org/v2/everything'
STANDINGS_URL = 'https://api.football-data.org/v2/competitions/EC/standings'

toaster = ToastNotifier()

def show_notification(title, message, url=None):
    if url:
        toaster.show_toast(
            title,
            message,
            duration=10,
            callback_on_click=lambda: open_url(url)
        )
    else:
        notification.notify(
            title=title,
            message=message,
            app_name='Euro 2024 Notifier',
            timeout=10
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

            if title not in latest_news:
                new_articles.append((title, url))
                latest_news.append(title)  

        if new_articles:
            with open(f'latest_news_{lang}.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(latest_news))

    for title, url in new_articles:
        show_notification('New Euro 2024 News!', title, url)

def check_for_standings():
    headers = {'X-Auth-Token': FOOTBALL_API_KEY}
    response = requests.get(STANDINGS_URL, headers=headers)
    standings_data = response.json()

    try:
        with open('latest_standings.json', 'r', encoding='utf-8') as f:
            latest_standings = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
<<<<<<< HEAD
        latest_standings = {}
=======
        latest_standings = {}  
>>>>>>> 5bc37c3aee6626b60c47a82701919c6919fd2f67

    current_standings = standings_data['standings'][0]['table']

    if current_standings != latest_standings:
<<<<<<< HEAD
=======
       
>>>>>>> 5bc37c3aee6626b60c47a82701919c6919fd2f67
        changes_detected = find_standings_changes(latest_standings, current_standings)

        if changes_detected:
            with open('latest_standings.json', 'w', encoding='utf-8') as f:
                json.dump(current_standings, f, indent=4)

            message = "Standings have been updated:\n"
            for change in changes_detected:
                team_name = change['team']['name']
                position = change['position']
                message += f"{position}. {team_name}\n"

            show_notification('Euro 2024 Standings Update', message)

def find_standings_changes(old_standings, new_standings):
    changes = []
    new_standings_dict = {team['team']['id']: team for team in new_standings}

    for position, team in enumerate(old_standings, start=1):
        team_id = team['team']['id']
        if team_id in new_standings_dict:
            new_position = new_standings_dict[team_id]['position']
            if new_position != position:
                changes.append({
                    'team': team,
                    'position': new_position
                })

    return changes

while True:
    try:
        check_for_news()
        check_for_standings()
    except Exception as e:
        print(f"Error occurred: {str(e)}")

    time.sleep(60)
