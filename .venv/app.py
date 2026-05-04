from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import dbinfo
# tarkistaa että db on olemassa
import createdb

# luodaan flask app
app = Flask(__name__)
# tietokannan yhdistämistiedot
app.config['MYSQL_HOST'] = dbinfo.data["HOST"]
app.config['MYSQL_USER'] = dbinfo.data["USER"]
app.config['MYSQL_PASSWORD'] = dbinfo.data["PASSWORD"]
app.config['MYSQL_DB'] = dbinfo.data["DBNIMI"]
mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    text = ""
    lajit = []
    # luo yhteyden tietokannan taluihin
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT laji FROM laji")

    lajit_tulos = cursor.fetchall()

    for x in lajit_tulos:
        res = ' '.join(x)
        lajit.append(res)
    
    # print(lajit)
    
    if request.method == 'POST':
        # saa inputtien arvot html formista
        nimi = request.form.get("nimi")
        pituus = request.form.get("pituus")
        paino = request.form.get("paino")
        laji = request.form.get("laji").lower()
        aika = request.form.get("aika")
        paikka = request.form.get("paikka")
        viehe = request.form.get("viehe")
        vapa = request.form.get("vapa")
        # print(laji)
        # tarkistaa pitääkö ottaa muu input

        # vielä tarkistus ettei mikään ole tyhjä 
        if nimi == "" or pituus == "" or paino == "" or laji == "" or paikka == "" or viehe == "" or vapa == "":
            text = "Jokin kohta oli tyhjä"
        else:
            cursor.execute(f"SELECT * FROM kalastaja WHERE nimi ='{nimi}'")
            select_nimi = cursor.fetchall()
            print(len(select_nimi))
            if len(select_nimi) == 0:
                # lähettää datan tietokantaan
                cursor.execute(f'INSERT INTO kalastaja (nimi) VALUES ("{nimi}")')        
                # saa aina edellisen taulun id:n
                kalastaja_id = cursor.lastrowid
            else:
                kalastaja_id = select_nimi[0][0]
            cursor.execute(f'INSERT INTO viehe (viehe) VALUES ("{viehe}")')
            viehe_id = cursor.lastrowid
            cursor.execute(f'INSERT INTO vapa (vapa) VALUES ("{vapa}")')
            vapa_id = cursor.lastrowid            
            
            cursor.execute(f"SELECT * FROM laji WHERE laji ='{laji}'")
            select_laji = cursor.fetchall()
            laji_id = select_laji[0][0]

            cursor.execute(f'INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ("{aika}", "{kalastaja_id}", "{viehe_id}", "{vapa_id}", "{paikka}")')
            tarppi_id = cursor.lastrowid
            cursor.execute(f'INSERT INTO kala (tarppi_id, pituus, paino, laji_id) VALUES ("{tarppi_id}", "{pituus}", "{paino}", "{laji_id}")')
            # tallettaa tapahtuneen tietokantaan
            mysql.connection.commit()        
            text = "Tiedot lisättiin onnistuneesti"
    return render_template('index.html', text=text, lajit=lajit)

@app.route('/muu', methods = ['POST', 'GET'])
def muu():
    if request.method == 'POST':
        id = 0
        cursor = mysql.connection.cursor()
        laji = request.form.get("lajiMuu")
        cursor.execute(f"SELECT * FROM laji WHERE laji ='{laji}'")
        laji_tarkistus = cursor.fetchall()
        if len(laji_tarkistus) == 0:
            cursor.execute(f"SELECT * FROM laji")
            laji_id = cursor.fetchall()
            id = len(laji_id) + 1
            cursor.execute(f'INSERT INTO laji (id, laji) VALUES ("{id}", "{laji}")')
            mysql.connection.commit()    
        else:
            return redirect(url_for("index"))
    return redirect(url_for("index"))

@app.route('/esitys', methods = ['POST', 'GET'])
def esitys():
    text = ""
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        # saa nopeuden arvon
        nopeus = request.form.get("nopeus")
        # laskee dian esityksen nopeuden
        s = int(nopeus) * 1000
        # tarkistaa ettei dian esityksen nopeus ole liian suuri tai liian pieni
        if s > 20000 or s < 1000:
            text = "Annoit joko liian suuren tai liian pienen luvun"
        else:        
            cursor.execute(f'INSERT INTO integraatiot (diaNopeus) VALUES ("{s}")')            
            # tallettaa tapahtuneen tietokantaan
            mysql.connection.commit()
            text = "Vaihtui onnistuneesti"
    return render_template('esitys.html', text=text)
if __name__=="__main__":
    app.run()