# Aplicatie_scraping_internet
##Ziua1:17/06/2024
Descriere Proiect
Pentru a crea o aplicatie care trimite notificari despre Euro 2024, am accesat doua surse online și am obținut doua chei API:

NewsAPI pentru stiri despre Euro 2024

Inregistrare: M-am inregistrat pe NewsAPI.
Obtinerea cheii API: Am generat o cheie API pentru a accesa stiri relevante despre Euro 2024.
Configurare cereri API: Am configurat cererile pentru a cauta știri în engleza si romana.

Football-Data API pentru clasamentul Euro 2024

Inregistrare: M-am inregistrat pe Football-Data API.
Obținerea cheii API: Am primit o cheie API pentru a accesa datele despre clasament.
Configurare cereri API: Am configurat cererile pentru a extrage clasamentul actualizat al competiției.
Integrare
Am integrat cele două chei API în aplicația Python:

Știri: Am folosit cheia API de la NewsAPI pentru a afișa notificări de tip pop-up pentru știri noi despre Euro 2024.
Clasament: Am folosit cheia API de la Football-Data API pentru a trimite notificări cu actualizările de clasament.
Astfel, aplicația oferă utilizatorilor notificări atât despre știri, cât și despre modificările din clasamentul Euro 2024.


##Ziua 2: 18/06/2024
Rezolvarea problemelor de afișare a notificărilor:

Am identificat și corectat erorile care afectau afișarea corectă a notificărilor.
Notificările sunt acum afișate consistent și fără întreruperi.
Filtrarea notificărilor:

Am implementat un sistem de filtrare care asigură că doar notificările relevante sunt afișate.
Acum, utilizatorii primesc doar notificările care contează pentru ei, fără a fi bombardați cu informații inutile.
Modificarea funcției de notificare a clasamentului:

Am revizuit funcția responsabilă de notificarea schimbărilor în clasament.
Noua versiune a funcției notifică utilizatorii imediat ce apar modificări în clasament, oferind detalii clare și precise despre schimbările recente.

##Ziua 3: 19/06/2024
Astăzi am adăugat o funcționalitate esențială în proiect:

Accesarea site-urilor cu știrile provenite din notificări:
Am integrat o nouă funcționalitate care permite utilizatorilor să acceseze direct site-urile cu știri relevante printr-un simplu clic pe notificări.
Acum, fiecare notificare de știre include un link către articolul original, oferind utilizatorilor o modalitate rapidă și ușoară de a accesa informațiile complete.

