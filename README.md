# Aplicatie_scraping_internet
## Ziua 1: 17/06/2024
Descriere Proiect

Pentru a crea o aplicatie care trimite notificari despre Euro 2024, am accesat doua surse online si am obtinut doua chei API:

NewsAPI pentru stiri despre Euro 2024:

Inregistrare: M-am inregistrat pe NewsAPI.
Obtinerea cheii API: Am generat o cheie API pentru a accesa stiri relevante despre Euro 2024.
Configurare cereri API: Am configurat cererile pentru a cauta stiri in engleza si romana.
Football-Data API pentru clasamentul Euro 2024:

Inregistrare: M-am inregistrat pe Football-Data API.
Obtinerea cheii API: Am primit o cheie API pentru a accesa datele despre clasament.
Configurare cereri API: Am configurat cererile pentru a extrage clasamentul actualizat al competitiei.
Integrare

Am integrat cele doua chei API in aplicatia Python:

Stiri: Am folosit cheia API de la NewsAPI pentru a afisa notificari de tip pop-up pentru stiri noi despre Euro 2024.
Clasament: Am folosit cheia API de la Football-Data API pentru a trimite notificari cu actualizarile de clasament.
Astfel, aplicatia ofera utilizatorilor notificari atat despre stiri, cat si despre modificarile din clasamentul Euro 2024.

## Ziua 2: 18/06/2024
Rezolvarea problemelor de afisare a notificarilor:

Am identificat si corectat erorile care afectau afisarea corecta a notificarilor.
Notificarile sunt acum afisate consistent si fara intreruperi.
Filtrarea notificarilor:

Am implementat un sistem de filtrare care asigura ca doar notificarile relevante sunt afisate.
Acum, utilizatorii primesc doar notificarile care conteaza pentru ei, fara a fi bombardati cu informatii inutile.
Modificarea functiei de notificare a clasamentului:

Am revizuit functia responsabila de notificarea schimbarilor in clasament.
Noua versiune a functiei notifica utilizatorii imediat ce apar modificari in clasament, oferind detalii clare si precise despre schimbarile recente.
## Ziua 3: 19/06/2024
Adaugarea unei functionalitati esentiale:

Accesarea site-urilor cu stirile provenite din notificari:
Am integrat o noua functionalitate care permite utilizatorilor sa acceseze direct site-urile cu stiri relevante printr-un simplu clic pe notificari.
Acum, fiecare notificare de stire include un link catre articolul original, oferind utilizatorilor o modalitate rapida si usoara de a accesa informatiile complete.

Acest aspect a fost inclus in functia check_for_news().

## Ziua 4: 20/06/2024

Modificarea functiei de notificare in caz de apare o schimbare in clasament cu o functie de notificare in care anunta utilizatorul cu o ora inainte de inceperea unui meci.
Acest aspect a fost inclus in functia check_for_matches()
