from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'kalastustietosivu'
app.config['MYSQL_PASSWORD'] = '2007'
app.config['MYSQL_DB'] = 'kalastustietosivu'
 
mysql = MySQL(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        # saa inputtien arvon html fomista
        nimi = request.form.get("nimi")
        pituus = request.form.get("pituus")
        paino = request.form.get("paino")
        laji = request.form.get("laji")
        aika = request.form.get("aika")
        paikka = request.form.get("paikka")
        viehe = request.form.get("viehe")
        vapa = request.form.get("vapa")
        print(nimi)
        print(pituus)
        print(paino)
        print(laji)
        print(aika)
        print(paikka)
        print(viehe)
        print(vapa)

        cursor.execute(f'INSERT INTO kalastaja (nimi) VALUES ("{nimi}")')

        # kalastaja_id = cursor.lastrowid

        # cursor.execute(f'INSERT INTO viehe (viehe) VALUES ({viehe})')

        # viehe_id = cursor.lastrowid

        # cursor.execute(f'INSERT INTO vapa (vapa) VALUES ({vapa})')

        # vapa_id = cursor.lastrowid
            
        # cursor.execute(f'INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ({aika}, {kalastaja_id}, {viehe_id}, {vapa_id}, {paikka})')

        # tarppi_id = cursor.lastrowid

        # cursor.execute(f'INSERT INTO kala (tarppi_id, pituus, paino, laji) VALUES ({tarppi_id}, {pituus}, {paino}, {laji})')

        mysql.connection.commit()
        
        cursor.close()

    return render_template('index.html')

if __name__=="__main__":
    app.run()