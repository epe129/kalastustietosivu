from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import dbinfo, createdb

createdb.db()
app = Flask(__name__)
# tietokannan yhdistämistiedot
app.config['MYSQL_HOST'] = dbinfo.data["HOST"]
app.config['MYSQL_USER'] = dbinfo.data["USER"]
app.config['MYSQL_PASSWORD'] = dbinfo.data["PASSWORD"]
app.config['MYSQL_DB'] = dbinfo.data["DBNIMI"]
mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    # luo yhteyden tietokannan taluihin
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        # saa inputtien arvot html formista
        nimi = request.form.get("nimi")
        pituus = request.form.get("pituus")
        paino = request.form.get("paino")
        laji = request.form.get("laji").lower()
        if laji == "muu": 
            laji = request.form.get("lajiMuu").lower()
        aika = request.form.get("aika")
        paikka = request.form.get("paikka")
        viehe = request.form.get("viehe")
        vapa = request.form.get("vapa")
        print(nimi, pituus, paino, laji, aika, paikka, viehe, vapa)
        # lähettää datan tietokantaan
        cursor.execute(f'INSERT INTO kalastaja (nimi) VALUES ("{nimi}")')        
        # saa aina edellisen taulun id:n
        kalastaja_id = cursor.lastrowid
        cursor.execute(f'INSERT INTO viehe (viehe) VALUES ("{viehe}")')
        viehe_id = cursor.lastrowid
        cursor.execute(f'INSERT INTO vapa (vapa) VALUES ("{vapa}")')
        vapa_id = cursor.lastrowid
        cursor.execute(f'INSERT INTO laji (laji) VALUES ("{laji}")')
        laji_id = cursor.lastrowid
        cursor.execute(f'INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ("{aika}", "{kalastaja_id}", "{viehe_id}", "{vapa_id}", "{paikka}")')
        tarppi_id = cursor.lastrowid
        cursor.execute(f'INSERT INTO kala (tarppi_id, pituus, paino, laji_id) VALUES ("{tarppi_id}", "{pituus}", "{paino}", "{laji_id}")')
        # tallettaa tapahtuneen tietokantaan
        mysql.connection.commit()
    return render_template('index.html')
@app.route('/esitys', methods = ['POST', 'GET'])
def esitys():
    error = ""
    cursor = mysql.connection.cursor()
    if request.method == 'POST':
        nopeus = request.form.get("nopeus")
        s = int(nopeus) * 1000
        if str(s) > "20000" or str(s) < "1":
            error = "Annoit joko liian suurenluvun tai nollan"
        else:        
            cursor.execute(f'INSERT INTO integraatiot (diaNopeus) VALUES ("{s}")')            
            # tallettaa tapahtuneen tietokantaan
            mysql.connection.commit()
    return render_template('esitys.html', error=error)
if __name__=="__main__":
    app.run()