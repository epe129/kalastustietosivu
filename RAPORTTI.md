# Kalasaaliiden Tallennusnettisivu – raportti

Versio: 0.2

## Johdanto

Tämän projektin tavoitteena oli toteuttaa kalasaaliiden tallennukseen tarkoitettu nettisivu, jossa käyttäjät voivat lisätä ja tarkastella kalastustietoja. Projektin avulla harjoittelin ohjelmointia, tietokantoja ja web-kehitystä.
---

# Projektin tavoite

Projektin tavoitteena oli tehdä toimiva nettisivu kalasaaliiden tallentamiseen ja hallintaan. Nettisivun avulla käyttäjät voivat:

* rekisteröityä
* kirjautua sisään
* lisätä kalasaaliita
* tarkastella omia tallennettuja kalatietoja

---

# Käytetyt teknologiat

Projektissa käytettiin seuraavia teknologioita:

* Frontend: PHP 
* Database: MySQL 
* Backend: Python 
* Tkinter Python-pohjaisen käyttöliittymän tekemiseen
* XAMPP paikallisen palvelinympäristön käyttämiseen

---

# Tietokanta

Tietokanta suunniteltiin kalasaaliiden tallennukseen. Tietokannassa on omat taulut:

* tarpeille
* käyttäjille
* kaloille
* kalalajeille
* vieheille
* vavoille

Tietokannan relaatiot mahdollistavat tietojen yhdistämisen ja hakemisen tehokkaasti.

## Tietokantarakenne

* KALASTAJA → käyttäjätiedot
* TARPPI → yksi saatu kala / tapahtuma
* KALA → kalan tiedot
* LAJI → kala lajit
* VIEHE → vieheet
* VAPA → vavat

![Kuva tietokannasta](database.png)

---

# Ohjelman rakenne

## Frontend

Frontend toteutettiin PHP:lla. Frontendissä käyttäjä voi:

* rekisteröityä
* kirjautua
* lisätä saaliita
* tarkastella tietoja

Frondnend rakenne:

data kansio:

* data/db_connetion.php: Luodaan yhteys tietokantaan
* data/handleAdd.php: käsittelee uuden kalasaaliin lisäämisen
* data/handleLogin.php: käsittelee sisään kirjautumisen.
* data/handleLogout.php: käsittelee ulos kirjautumisen.
* data/handleMuuAdd.php: käsittelee uuden vapa, laji ja viehe arvon lisäämisen.
* data/handleRegister.php: käsittelee rekisteröitymisen.

login kansio:

* login/login.php: kirjautumis-sivu.

main kansio:

* main/index.php: näytetään kalasaaliiden eri tiedot.
* main/lisaa.php: uusien kalalajien lisäämis sivu.

Frondend:

* /index.php: rekisteröitymis-sivu.

## Backend

Backend toteutettiin Pythonilla ja Tkinterillä. Backendin tarkoituksena on ylläpitää tietokannan sisältöä.

Backendissä voidaan:

* admin voi kirjautua sisään
* poistaa käyttäjiä
* poistaa vieheitä
* poistaa vapoja
* poistaa kalalajeja

Backend rakenne:

* backend.py: Luodaan adminin kirjautumis ikkuna.
* admin_window.py: Luodaan adminin ikkuna jossa admin voi poistaa esimerkiksi käyttäjiä
* poista_moduuli.py: Tiedosto eri tietojen poisto fucntioille. 
* tarkista_moduuli.py: Tiedosto fucntioille jotkaa päivittää input hakua.
* createdb.py: Tiedosto databasen luontiin.

---

# Tietoturva

Projektissa huomioitiin perustason tietoturva:

* käyttäjien salasanat tallennetaan password_hash()-hashattuina
* SQL-injektioita estetään prepared statementien avulla

---

# Mikä onnistui

Frontend onnistui hyvin. Käyttöliittymästä tuli toimiva ja käyttäjä pystyy lisäämään sekä tarkastelemaan kalasaaliita helposti.
Tietokannan rakenne onnistui myös hyvin ja eri taulujen väliset suhteet toimivat suunnitellusti.

---

# Kehitys ideoita tulevaisuudelle

Kun jatkan projektia tulevaisuudessa, toteutan backendin Flaskilla Tkinterin sijaan. Flask sopii paremmin web-pohjaiseen sovellukseen ja helpottaa backendin laajentamista tulevaisuudessa. Parantaa tietoturvaa frondendissä.

---

# Mitä opin

Projektin aikana opin lisää:

* PHP-ohjelmoinnista
* Python-ohjelmoinnista
* Tietokantojen käytöstä ja tekemisestä

Opin myös käyttämään prepared statementteja sekä salasanojen turvallista hashäystä.

---

# Yhteenveto

Projektissa toteutettiin toimiva kalasaaliiden tallennusnettisivu käyttäen PHP:tä, Pythonia ja MySQL-tietokantaa. Projekti kehitti osaamistani erityisesti web-kehityksessä, tietokannoissa ja ohjelmistojen rakenteen suunnittelussa.
