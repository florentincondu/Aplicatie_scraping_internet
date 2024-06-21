import requests
import json
import webbrowser
import threading
import time
from datetime import datetime
from plyer import notification
from win10toast_click import ToastNotifier
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import io

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

def load_stored_news(lang):
    try:
        with open(f'latest_news_{lang}.txt', 'r', encoding='utf-8') as f:
            stored_news = f.read().splitlines()
            return stored_news
    except FileNotFoundError:
        return []

def store_news(lang, news_list):
    with open(f'latest_news_{lang}.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(news_list))

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

        stored_news = load_stored_news(lang)
        latest_news = []

        for article in news_data.get('articles', []):
            title = article['title']
            url = article['url']
            image_url = article['urlToImage']
            if title not in stored_news and title != "[Removed]":
                new_articles.append((title, url, image_url))
            latest_news.append(title)

        store_news(lang, latest_news)

    new_articles.sort(key=lambda x: x[0], reverse=True)
    return new_articles

def check_for_matches():
    headers = {'X-Auth-Token': FOOTBALL_API_KEY}
    response = requests.get(MATCHES_URL, headers=headers)
    matches_data = response.json()

    today = datetime.now().date()
    upcoming_matches = []

    for match in matches_data['matches']:
        match_time = datetime.fromisoformat(match['utcDate'].replace('Z', '+00:00'))
        if match_time.date() >= today:
            upcoming_matches.append({
                'home_team': match['homeTeam']['name'],
                'away_team': match['awayTeam']['name'],
                'match_time': match_time,
                'notified': False
            })

    return upcoming_matches

def update_news():
    news_listbox.delete(0, END)
    all_articles = []

    for lang in ['en', 'ro']:
        stored_news = load_stored_news(lang)
        for title in stored_news:
            response = requests.get(NEWS_API_URL, params={
                'qInTitle': title,
                'apiKey': NEWS_API_KEY
            })
            news_data = response.json()
            for article in news_data.get('articles', []):
                all_articles.append((article['title'], article['url'], article['urlToImage']))

    all_articles.sort(key=lambda x: x[0], reverse=True)
    news_images.clear()

    for title, url, image_url in all_articles:
        news_images.append((title, url, image_url))
        add_news_to_listbox(title, url, image_url)

def update_matches():
    match_listbox.delete(0, END)
    upcoming_matches = check_for_matches()
    for match in upcoming_matches:
        home_team = match['home_team']
        away_team = match['away_team']
        match_time = match['match_time'].strftime('%Y-%m-%d %H:%M:%S')

        message = f'{home_team} vs {away_team} starts at {match_time}'
        match_listbox.insert(END, message)

def add_news_to_listbox(title, url, image_url):
    news_frame = Frame(news_listbox, bg='black')
    news_frame.pack(fill=X, pady=5)

    try:
        response = requests.get(image_url)
        image_data = response.content
        image = Image.open(io.BytesIO(image_data))
        image = image.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label = Label(news_frame, image=photo, bg='black')
        image_label.image = photo
        image_label.pack(side=LEFT)
    except Exception as e:
        print(f"Failed to load image for {title}: {e}")
        image_label = Label(news_frame, text="No Image", bg='black', fg='white')
        image_label.pack(side=LEFT)

    title_label = Label(news_frame, text=title, fg='white', bg='black', cursor='hand2', wraplength=200, justify=LEFT)
    title_label.pack(side=LEFT, fill=X, expand=True)
    title_label.bind("<Button-1>", lambda e: open_url(url))

def update_news_and_matches():
    while True:
        update_news()
        if receive_match_notifications.get():
            update_matches()
        time.sleep(60)

def search_news():
    query = search_var.get().lower()
    news_listbox.delete(0, END)
    for title, url, image_url in news_images:
        if query in title.lower():
            add_news_to_listbox(title, url, image_url)

def reset_news():
    news_listbox.delete(0, END)
    for title, url, image_url in news_images:
        add_news_to_listbox(title, url, image_url)

def on_select_match(event):
    selected_index = match_listbox.curselection()
    if selected_index:
        selected_match = match_listbox.get(selected_index)
        if messagebox.askyesno("Notification", f"Would you like to be notified for this match?\n\n{selected_match}"):
            for match in upcoming_matches:
                if f"{match['home_team']} vs {match['away_team']} starts at {match['match_time'].strftime('%Y-%m-%d %H:%M:%S')}" == selected_match:
                    match['notified'] = True

def show_upcoming_fixtures():
    news_frame.pack_forget()
    fixtures_frame.pack(fill=BOTH, expand=True)
    update_matches()

def show_news():
    fixtures_frame.pack_forget()
    news_frame.pack(fill=BOTH, expand=True)

# GUI setup
root = Tk()
root.title("Euro 2024 Notifier")

receive_news_notifications = BooleanVar(value=True)
receive_match_notifications = BooleanVar(value=True)

control_frame = Frame(root, bg='black')
control_frame.pack(side=TOP, fill=X)

news_notification_check = Checkbutton(control_frame, text="News Notifications", variable=receive_news_notifications, bg='black', fg='white')
news_notification_check.pack(side=LEFT)

match_notification_check = Checkbutton(control_frame, text="Match Notifications", variable=receive_match_notifications, bg='black', fg='white')
match_notification_check.pack(side=LEFT)

search_var = StringVar()
search_entry = Entry(control_frame, textvariable=search_var)
search_entry.pack(side=LEFT, fill=X, expand=True, padx=5)

search_button = Button(control_frame, text="Search", command=search_news, bg='black', fg='white')
search_button.pack(side=LEFT)

reset_button = Button(control_frame, text="Reset", command=reset_news, bg='black', fg='white')
reset_button.pack(side=LEFT)

fixtures_button = Button(control_frame, text="Upcoming Fixtures", command=show_upcoming_fixtures, bg='black', fg='white')
fixtures_button.pack(side=LEFT)

news_frame = Frame(root, bg='black')
news_frame.pack(side=LEFT, fill=BOTH, expand=True)

news_label = Label(news_frame, text="Latest News", font=("Helvetica", 16), bg='black', fg='white')
news_label.pack()

news_canvas = Canvas(news_frame, bg='black')
news_canvas.pack(side=LEFT, fill=BOTH, expand=True)

news_scrollbar = Scrollbar(news_frame, orient=VERTICAL, command=news_canvas.yview)
news_scrollbar.pack(side=RIGHT, fill=Y)

news_listbox = Listbox(news_canvas, bg='black', fg='white')
news_listbox.pack(side=LEFT, fill=BOTH, expand=True)

news_canvas.create_window((0, 0), window=news_listbox, anchor="nw")

def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

news_listbox.bind("<Configure>", lambda event, canvas=news_canvas: on_frame_configure(canvas))
news_canvas.configure(yscrollcommand=news_scrollbar.set)

fixtures_frame = Frame(root, bg='black')

fixtures_label = Label(fixtures_frame, text="Upcoming Matches", font=("Helvetica", 16), bg='black', fg='white')
fixtures_label.pack()

match_listbox = Listbox(fixtures_frame, bg='black', fg='white')
match_listbox.pack(fill=BOTH, expand=True)
match_listbox.bind('<<ListboxSelect>>', on_select_match)

back_button = Button(fixtures_frame, text="Back to News", command=show_news, bg='black', fg='white')
back_button.pack()

news_images = []
upcoming_matches = check_for_matches()

update_thread = threading.Thread(target=update_news_and_matches, daemon=True)
update_thread.start()

root.mainloop()
