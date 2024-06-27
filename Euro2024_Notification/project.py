import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
from plyer import notification
import threading
from datetime import datetime, timedelta

FOOTBALL_API_KEY = '097ab494621643829a7d1f1cba4fa521'
NEWS_API_KEY = '6368f55812f94137b2e82d45007560be'
NEWS_API_URL = 'https://newsapi.org/v2/everything'
MATCHES_URL = 'https://api.football-data.org/v4/competitions/EC/matches'
TEAM_URL = 'https://api.football-data.org/v4/teams/'

class Euro2024App:
    def __init__(self, root):
        self.root = root
        self.root.title("Euro 2024 News and Fixtures")

        self.news_frame = tk.Frame(root)
        self.fixtures_window = None
        self.matches = []
        self.all_news = []
        self.last_news_notification_time = datetime.min

        self.news_notification_enabled = tk.BooleanVar()
        self.fixtures_notification_enabled = tk.BooleanVar()

        self.create_main_page()
        self.schedule_updates()

    def create_main_page(self):
        self.clear_frame(self.news_frame)

        self.news_canvas = tk.Canvas(self.news_frame, width=800, height=600)
        self.news_scrollbar = tk.Scrollbar(self.news_frame, orient="vertical", command=self.news_canvas.yview)
        self.news_scrollable_frame = tk.Frame(self.news_canvas)

        self.news_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.news_canvas.configure(
                scrollregion=self.news_canvas.bbox("all")
            )
        )

        self.news_canvas.create_window((0, 0), window=self.news_scrollable_frame, anchor="nw")
        self.news_canvas.configure(yscrollcommand=self.news_scrollbar.set)

        self.news_canvas.pack(side="left", fill="both", expand=True)
        self.news_scrollbar.pack(side="right", fill="y")

        self.search_var = tk.StringVar()
        search_frame = tk.Frame(self.news_frame)
        search_label = tk.Label(search_frame, text="Search")
        search_label.pack(side="left", padx=5)
        self.search_bar = tk.Entry(search_frame, textvariable=self.search_var)
        self.search_bar.pack(side="left", pady=10)
        self.search_bar.bind('<KeyRelease>', self.search_news)
        search_frame.pack(pady=10)

        self.button_frame = tk.Frame(self.news_frame)
        self.button_frame.pack(pady=10)

        self.notifications_checkbox = tk.Checkbutton(
            self.button_frame, text="Enable News Notifications", variable=self.news_notification_enabled)
        self.notifications_checkbox.pack(side="left", padx=5)

        self.fixtures_button = tk.Button(self.button_frame, text="Upcoming Fixtures", command=self.show_fixtures)
        self.fixtures_button.pack(side="left", padx=5)

        self.news_frame.pack(fill="both", expand=True)

        threading.Thread(target=self.fetch_news).start()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def fetch_news(self):
        try:
            params = {
                'q': 'Euro 2024 football',
                'apiKey': NEWS_API_KEY,
                'language': 'en',
                'sortBy': 'publishedAt'
            }
            response = requests.get(NEWS_API_URL, params=params)
            response.raise_for_status()
            news_data = response.json()

            news = set()
            articles = news_data.get('articles', [])
            for article in articles:
                if "Removed" in article.get('title', ''):
                    continue
                title = article.get('title')
                link = article.get('url')
                img_url = article.get('urlToImage')
                published_at = datetime.strptime(article.get('publishedAt'), "%Y-%m-%dT%H:%M:%SZ")
                news.add((title, link, img_url, published_at))

            self.all_news = list(news)
            self.update_news(self.all_news)

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch news: {e}")

    def update_news(self, news):
        for widget in self.news_scrollable_frame.winfo_children():
            widget.destroy()

        for title, link, img_url, published_at in news:
            self.display_article(title, link, img_url)

        if self.news_notification_enabled.get() and news:
            latest_news_time = max([article[3] for article in news])
            if latest_news_time > self.last_news_notification_time:
                self.send_news_notification(news[0][0])
                self.last_news_notification_time = latest_news_time

    def display_article(self, title, link, img_url):
        article_frame = tk.Frame(self.news_scrollable_frame, pady=10)

        if img_url:
            threading.Thread(target=self.load_image, args=(article_frame, img_url)).start()

        text_frame = tk.Frame(article_frame)
        text_frame.pack(side="left", padx=10)

        title_label = tk.Label(text_frame, text=title, wraplength=600, justify="left")
        title_label.pack(anchor="w")

        link_label = tk.Label(text_frame, text=link, fg="blue", cursor="hand2")
        link_label.pack(anchor="w")
        link_label.bind("<Button-1>", lambda e: self.open_link(link))

        article_frame.pack(fill="x", pady=10)

    def load_image(self, frame, img_url):
        response = requests.get(img_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        image = image.resize((150, 150), Image.LANCZOS)
        photo = ImageTk.PhotoImage(image)

        img_label = tk.Label(frame, image=photo)
        img_label.image = photo
        img_label.pack(side="left")

    def open_link(self, link):
        import webbrowser
        webbrowser.open(link)

    def search_news(self, event):
        search_term = self.search_var.get().lower()
        if search_term == "":
            self.update_news(self.all_news)
        else:
            filtered_news = [article for article in self.all_news if search_term in article[0].lower()]
            self.update_news(filtered_news)

    def send_news_notification(self, title):
        notification.notify(
            title="Euro 2024 News",
            message=f"New article: {title}",
            timeout=10
        )

    def show_fixtures(self):
        self.fixtures_window = tk.Toplevel(self.root)
        self.fixtures_window.title("Upcoming Fixtures")
        self.create_fixtures_page()

    def create_fixtures_page(self):
        self.fixtures_frame = tk.Frame(self.fixtures_window)

        self.fixtures_canvas = tk.Canvas(self.fixtures_frame, width=800, height=600)
        self.fixtures_scrollbar = tk.Scrollbar(self.fixtures_frame, orient="vertical", command=self.fixtures_canvas.yview)
        self.fixtures_scrollable_frame = tk.Frame(self.fixtures_canvas)

        self.fixtures_scrollable_frame.bind(
            "<Configure>",
            lambda e: self.fixtures_canvas.configure(
                scrollregion=self.fixtures_canvas.bbox("all")
            )
        )

        self.fixtures_canvas.create_window((0, 0), window=self.fixtures_scrollable_frame, anchor="nw")
        self.fixtures_canvas.configure(yscrollcommand=self.fixtures_scrollbar.set)

        self.fixtures_canvas.pack(side="left", fill="both", expand=True)
        self.fixtures_scrollbar.pack(side="right", fill="y")

        self.fixtures_frame.pack(fill="both", expand=True)

        self.notify_checkbox = tk.Checkbutton(
            self.fixtures_frame, text="Enable Match Notifications", variable=self.fixtures_notification_enabled)
        self.notify_checkbox.pack(side="bottom", pady=10)

        threading.Thread(target=self.fetch_fixtures).start()

    def fetch_fixtures(self):
        try:
            headers = {'X-Auth-Token': FOOTBALL_API_KEY}
            response = requests.get(MATCHES_URL, headers=headers)
            response.raise_for_status()
            matches_data = response.json()

            self.matches = []
            for match in matches_data.get('matches', []):
                match_date = datetime.strptime(match['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
                if match_date >= datetime.now():
                    home_team = match['homeTeam']['name']
                    away_team = match['awayTeam']['name']
                    home_team_id = match['homeTeam']['id']
                    away_team_id = match['awayTeam']['id']
                    self.matches.append((home_team, away_team, match_date, home_team_id, away_team_id))

            self.update_fixtures(self.matches)

        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch fixtures: {e}")

    def update_fixtures(self, matches):
        for widget in self.fixtures_scrollable_frame.winfo_children():
            widget.destroy()

        for home_team, away_team, match_date, home_team_id, away_team_id in matches:
            match_frame = tk.Frame(self.fixtures_scrollable_frame, pady=10)

            home_team_label = tk.Label(match_frame, text=home_team, fg="blue", cursor="hand2")
            home_team_label.pack(side="left")
            home_team_label.bind("<Button-1>", lambda e, team_id=home_team_id: self.show_team_info(team_id))

            vs_label = tk.Label(match_frame, text=" vs ")
            vs_label.pack(side="left")

            away_team_label = tk.Label(match_frame, text=away_team, fg="blue", cursor="hand2")
            away_team_label.pack(side="left")
            away_team_label.bind("<Button-1>", lambda e, team_id=away_team_id: self.show_team_info(team_id))

            match_date_label = tk.Label(match_frame, text=f" - {match_date.strftime('%Y-%m-%d %H:%M:%S')}")
            match_date_label.pack(side="left")

            match_frame.pack(fill="x", pady=10)

        if self.fixtures_notification_enabled.get() and matches:
            self.enable_match_notifications()

    def get_team_id(self, team_name):
        try:
            response = requests.get(f"{TEAM_URL}", headers={'X-Auth-Token': FOOTBALL_API_KEY})
            response.raise_for_status()
            teams_data = response.json()
            for team in teams_data['teams']:
                if team['name'].lower() == team_name.lower():
                    return team['id']
            return None
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch team ID: {e}")
            return None

    def get_team_details(self, team_id):
        try:
            response = requests.get(f"{TEAM_URL}{team_id}", headers={'X-Auth-Token': FOOTBALL_API_KEY})
            response.raise_for_status()
            team_data = response.json()
            return team_data
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Failed to fetch team details: {e}")
            return None

    def show_team_info(self, team_id):
        team_data = self.get_team_details(team_id)
        if team_data:
            team_info_window = tk.Toplevel(self.root)
            team_info_window.title("Team Information")

            team_info_frame = tk.Frame(team_info_window)
            team_info_frame.pack(fill="both", expand=True)

            self.update_team_info(team_data, team_info_frame)
        else:
            messagebox.showerror("Error", "Failed to fetch team information.")

    def fetch_team_info(self, team_id, frame):
        team_data = self.get_team_details(team_id)
        if team_data:
            self.update_team_info(team_data, frame)
        else:
            messagebox.showerror("Error", "Failed to fetch team information.")

    def update_team_info(self, team_data, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        team_name = team_data.get('name')
        squad = team_data.get('squad', [])
        squad_value = team_data.get('squadMarketValue', 'N/A')

        team_label = tk.Label(frame, text=f"Team: {team_name}", font=("Arial", 14))
        team_label.pack(pady=5)

        value_label = tk.Label(frame, text=f"Squad Value: {squad_value}", font=("Arial", 12))
        value_label.pack(pady=5)

        squad_label = tk.Label(frame, text="Squad:", font=("Arial", 12))
        squad_label.pack(pady=5)

        for player in squad:
            player_name = player.get('name')
            position = player.get('position')
            shirt_number = player.get('shirtNumber') if 'shirtNumber' in player else 'N/A'
            player_label = tk.Label(frame, text=f"{player_name} - {position} - #{shirt_number}")
            player_label.pack(anchor="w")

    def ask_for_match_notifications(self, home_team, away_team, match_date):
        result = messagebox.askyesno("Match Notification", f"Do you want to receive notifications for {home_team} vs {away_team} match?")
        if result:
            self.schedule_single_match_notification(home_team, away_team, match_date)

    def schedule_single_match_notification(self, home_team, away_team, match_date):
        notification_time = match_date - timedelta(minutes=5)
        if datetime.now() < notification_time:
            threading.Timer((notification_time - datetime.now()).total_seconds(),
                            self.send_match_notification,
                            [home_team, away_team, match_date]).start()

    def enable_match_notifications(self):
        for home_team, away_team, match_date in self.matches:
            self.schedule_single_match_notification(home_team, away_team, match_date)

    def send_match_notification(self, home_team, away_team, match_date):
        notification.notify(
            title="Upcoming Match",
            message=f"{home_team} vs {away_team} is starting at {match_date.strftime('%Y-%m-%d %H:%M:%S')}",
            timeout=10
        )

    def schedule_updates(self):
        self.root.after(60000, self.fetch_news)
        self.root.after(60000, self.fetch_fixtures)

if __name__ == "__main__":  
    root = tk.Tk()
    app = Euro2024App(root)
    root.mainloop()
