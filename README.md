# Aplicatie_scraping_internet
## Ziua 1: 17/06/2024
Descriere Proiect

Pentru a crea o aplicatie care trimite notificari despre Euro 2024, am accesat doua surse online si am obtinut doua chei API:  

NewsAPI pentru stiri despre Euro 2024:  

Inregistrare:  
M-am inregistrat pe NewsAPI.
  - Obtinerea cheii API: Am generat o cheie API pentru a accesa stiri relevante despre Euro 2024.
  - Configurare cereri API: Am configurat cererile pentru a cauta stiri in engleza si romana.

Football-Data API pentru clasamentul Euro 2024:
Inregistrare:
M-am inregistrat pe Football-Data API.
  - Obtinerea cheii API: Am primit o cheie API pentru a accesa datele despre clasament.
  - Configurare cereri API: Am configurat cererile pentru a extrage clasamentul actualizat al competitiei.

Actualizare:
Football-Data API pentru meciurile Euro 2024:
  - Înregistrare: M-am înregistrat pe Football-Data API.
  - Obținerea cheii API: Am primit o cheie API pentru a accesa datele despre următoarele meciuri.
  - Configurare cereri API: Am configurat cererile pentru a extrage meciurile planificate, inclusiv gazda, oaspeții și ora de start a fiecărui meci.
Stiri:
  - Am folosit cheia API de la NewsAPI pentru a afisa notificari de tip pop-up pentru stiri noi despre Euro 2024.
  - Astfel, aplicatia ofera utilizatorilor notificari despre stirile competitiei Euro2024

## Ziua 2: 18/06/2024
Rezolvarea problemelor de afisare a notificarilor:  
  - Am identificat si corectat erorile care afectau afisarea corecta a notificarilor.
  - Notificarile sunt acum afisate consistent si fara intreruperi.
Filtrarea notificarilor:
  - Am implementat un sistem de filtrare care asigura ca doar notificarile relevante sunt afisate.
  - Acum, utilizatorii primesc doar notificarile care conteaza pentru ei, fara a fi bombardati cu informatii inutile.
Modificarea functiei de notificare a clasamentului:
  - Am revizuit functia responsabila de notificarea schimbarilor in clasament.
  - Noua versiune a functiei notifica utilizatorii imediat ce apar modificari in clasament, oferind detalii clare si precise despre schimbarile recente.
## Ziua 3: 19/06/2024
Accesarea site-urilor cu stirile provenite din notificari:
  - Am integrat o noua functionalitate care permite utilizatorilor sa acceseze direct site-urile cu stiri relevante printr-un simplu clic pe notificari.
  - Acum, fiecare notificare de stire include un link catre articolul original, oferind utilizatorilor o modalitate rapida si usoara de a accesa informatiile complete.
Acest aspect a fost inclus in functia check_for_news().

## Ziua 4: 20/06/2024
  - Modificarea functiei de notificare in caz de apare o schimbare in clasament cu o functie de notificare in care anunta utilizatorul cu o ora inainte de inceperea unui meci.
  - Astfel prin intermediul chei API furnizate de Football-Data API ,numai extrag date despre clasament ci despre urmatoarele meciuri . 
Acest aspect a fost inclus in functia check_for_matches()
