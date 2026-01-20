import tkinter as tk
import pymysql

connection = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="kalastustietosivu")
cursor = connection.cursor()

root = tk.Tk()
root.geometry("600x600")
root.title("Admin")

def get_input():
    nimi = nimi_input.get()
    pituus = pituus_input.get()
    paino = paino_input.get()
    laji = laji_input.get()
    aika = aika_input.get()
    paikka = paikka_input.get()
    viehe = viehe_input.get()
    vapa = vapa_input.get()

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
    connection.commit()
    # sulkee yhteyden tietokannan tauluihin
    cursor.close()

l = tk.Label(text = "Kalastustiedot")



string=tk.StringVar()

nimi = tk.Label(root, text="Nimi:", font=('calibre',10))
nimi_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

pituus = tk.Label(root, text="Pituus:", font=('calibre',10))
pituus_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

paino = tk.Label(root, text="Paino:", font=('calibre',10))
paino_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

laji = tk.Label(root, text="Laji:", font=('calibre',10))
laji_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

aika = tk.Label(root, text="Aika:", font=('calibre',10))
aika_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

paikka = tk.Label(root, text="Paikka:", font=('calibre',10))
paikka_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

viehe = tk.Label(root, text="Viehe:", font=('calibre',10))
viehe_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

vapa = tk.Label(root, text="Vapa:", font=('calibre',10))
vapa_input = tk.Entry(root, textvariable=string, font=('calibre',10,'normal'))

button = tk.Button(root, text="Lähetä", command=get_input)

l.grid(row=0,column=1)

nimi.grid(row=1,column=0)
nimi_input.grid(row=1,column=1)

pituus.grid(row=2,column=0)
pituus_input.grid(row=2,column=1)

paino.grid(row=3,column=0)
paino_input.grid(row=3,column=1)

laji.grid(row=4,column=0)
laji_input.grid(row=4,column=1)

aika.grid(row=5,column=0)
aika_input.grid(row=5,column=1)

paikka.grid(row=6,column=0)
paikka_input.grid(row=6,column=1)

viehe.grid(row=7,column=0)
viehe_input.grid(row=7,column=1)

vapa.grid(row=8,column=0)
vapa_input.grid(row=8,column=1)

button.grid(row=9,column=1)

root.mainloop()