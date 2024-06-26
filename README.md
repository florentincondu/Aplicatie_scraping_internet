# Aplicatie_scraping_internet: Euro 2024 News and Fixtures
## Ziua 1: 17/06/2024
Descriere Proiect

### Pentru a crea o aplicatie care trimite notificari despre Euro 2024, am accesat doua surse online si am obtinut doua chei API:  

#### NewsAPI pentru stiri despre Euro 2024:  

#### Inregistrare:  
M-am inregistrat pe NewsAPI.
  - Obtinerea cheii API: Am generat o cheie API pentru a accesa stiri relevante despre Euro 2024.
  - Configurare cereri API: Am configurat cererile pentru a cauta stiri in engleza si romana.

### Football-Data API pentru clasamentul Euro 2024:
#### Inregistrare:
M-am inregistrat pe Football-Data API.
  - Obtinerea cheii API: Am primit o cheie API pentru a accesa datele despre clasament.
  - Configurare cereri API: Am configurat cererile pentru a extrage clasamentul actualizat al competitiei.

### Actualizare:
#### Football-Data API pentru meciurile Euro 2024:
  - Înregistrare: M-am înregistrat pe Football-Data API.
  - Obținerea cheii API: Am primit o cheie API pentru a accesa datele despre următoarele meciuri.
  - Configurare cereri API: Am configurat cererile pentru a extrage meciurile planificate, inclusiv gazda, oaspeții și ora de start a fiecărui meci.
#### Stiri:
  - Am folosit cheia API de la NewsAPI pentru a afisa notificari de tip pop-up pentru stiri noi despre Euro 2024.
  - Astfel, aplicatia ofera utilizatorilor notificari despre stirile competitiei Euro2024

## Ziua 2: 18/06/2024
#### Rezolvarea problemelor de afisare a notificarilor:  
  - Am identificat si corectat erorile care afectau afisarea corecta a notificarilor.
  - Notificarile sunt acum afisate consistent si fara intreruperi.
#### Filtrarea notificarilor:
  - Am implementat un sistem de filtrare care asigura ca doar notificarile relevante sunt afisate.
  - Acum, utilizatorii primesc doar notificarile care conteaza pentru ei, fara a fi bombardati cu informatii inutile.
#### Modificarea functiei de notificare a clasamentului:
  - Am revizuit functia responsabila de notificarea schimbarilor in clasament.
  - Noua versiune a functiei notifica utilizatorii imediat ce apar modificari in clasament, oferind detalii clare si precise despre schimbarile recente.
## Ziua 3: 19/06/2024
#### Accesarea site-urilor cu stirile provenite din notificari:
  - Am integrat o noua functionalitate care permite utilizatorilor sa acceseze direct site-urile cu stiri relevante printr-un simplu clic pe notificari.
  - Acum, fiecare notificare de stire include un link catre articolul original, oferind utilizatorilor o modalitate rapida si usoara de a accesa informatiile complete.
Acest aspect a fost inclus in functia check_for_news().

## Ziua 4: 20/06/2024
  - Modificarea functiei de notificare in caz de apare o schimbare in clasament cu o functie de notificare in care anunta utilizatorul cu o ora inainte de inceperea unui meci.
  - Astfel prin intermediul chei API furnizate de Football-Data API ,numai extrag date despre clasament ci despre urmatoarele meciuri . 
Acest aspect a fost inclus in functia check_for_matches()

## Ziua 5: 21/06/2024
  - Implementarea unei interfete grafice pentru o gestionare mai usoara a aplicatiei si pentru adaugare de noi utilitati .
  - Interfata grafica inca este in mod de testare si mai are nevoie de ajustari.


## Ziua 6: 25/06/2024  
### Actualizare informatii proiect:   
#### Aceasta aplicatie ofera o interfata utilizator pentru accesarea stirilor Euro 2024 și a meciurilor de fotbal viitoare. Include functionalitati precum o bara de cautare pentru filtrarea articolelor de stiri si notificari pentru stiri si meciuri.  
#### Caracteristici:
  - Bara de Cautare: Permite utilizatorilor să caute articole de stiri specifice pe baza cuvintelor cheie.
  - Sectiune de Stiri: Afiseaza articolele de stiri recuperate legate de Euro 2024.
  - Notificari pentru Stiri: Optiune pentru activarea notificarilor pentru articolele noi de stiri recuperate.
  - Meciuri Viitoare: Afiseaza meciurile de fotbal programate pentru Euro 2024.
  - Notificari pentru Meciuri: Optiune pentru activarea notificarilor pentru meciurile viitoare.  
#### Componente:
  - Pagina Principala: Afiseaza articole de stiri cu titluri, link-uri și imagini optionale.
  - Pagina Meciuri: Arata meciurile de fotbal viitoare cu numele echipelor si datele meciurilor.
  - Notificari: Foloseste biblioteca Plyer pentru a trimite notificari desktop pentru actualizari de stiri si meciuri.  
#### Dependinte:
  - Python 3
  - tkinter (pentru GUI)
  - requests (pentru efectuarea cererilor HTTP)
  - Pillow (varianta PIL pentru manipularea imaginilor)
  - Plyer (pentru notificari desktop)
  - datetime (pentru operatii cu date si timp)  
#### API-uri Utilizate:
  - News API: Obtine articole de stiri legate de Euro 2024.
  - Football API: Obtine meciuri de fotbal viitoare pentru Euro 2024.  
#### Cum sa Utilizati:
  - Clonează repozitia.
  - Instalează dependintele.
  - Rulează python project.py pentru a porni aplicatia.  
#### Navigheaza prin interfata:
  - Foloseste bara de cautare pentru a filtra articolele de stiri.
  - Click pe "Upcoming fixtures" pentru a vedea meciurile programate.
  - Activeaza casetele de bifare pentru notificări pentru stiri si meciuri.  
## Pagina Principala:
![Screenshot 2024-06-25 091348](https://github.com/florentincondu/Aplicatie_scraping_internet/assets/162702746/9a383c82-164c-42ca-9a82-b289f489102c)

## Pagina Upcoming fixtures:  
![Screenshot 2024-06-25 091406](https://github.com/florentincondu/Aplicatie_scraping_internet/assets/162702746/764ab75d-27eb-4d16-90d7-5aa27eab3361)

## Ziua 7: 26/06/2024  
### Actualizare:
  - Functionalitatea barei de cautare a fost actualizata si acum functioneaza complet. Aceasta actualizare include imbunatatiri ale procesului de filtrare a stirilor, facandu-l mai eficient si mai usor de utilizat.
### Structura Aplicatiei
#### Clasa Principala a Aplicatiei: Euro2024App
#### Functii Principale:
  - create_main_page(): Initializeaza layout-ul paginii principale.
  - fetch_news(): Recupereaza cele mai recente articole de stiri.
  - update_news(news): Actualizeaza afisarea stirilor.
  - search_news(event): Filtreaza articolele de stiri pe baza interogarii de cautare.
  - show_fixtures(): Deschide o fereastra noua care afiseaza programarile viitoare.
  - fetch_fixtures(): Recupereaza programarile viitoare ale meciurilor.
  - update_fixtures(matches): Actualizeaza afisarea programarilor.
  - schedule_updates(): Programeaza actualizari regulate pentru stiri si programari.
### Utilizarea Barei de Cautare:
  - Situata pe pagina principala, bara de cautare permite utilizatorilor sa filtreze articolele de stiri.
#### Functionalitatea de Cautare:
  - Eveniment Declansator: Bara de cautare asculta pentru eliberarile de taste (<KeyRelease>) pentru a declansa functia search_news.
  - Logica de Filtrare: Functia search_news filtreaza prin self.all_news si actualizeaza afisarea pe baza termenului de cautare.

