import pymysql
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkcalendar import DateEntry
# yhteys tietokantaan
connection = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="", database="kalastustietosivu")
cursor = connection.cursor()
# luodaan ikkuna
root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("1000x600")
root.title("Admin")
# saadaan inputit
def get_input():
    nimi = nimi_input.get()
    pituus = pituus_input.get()
    paino = paino_input.get()
    laji = laji_input.get()
    saatu_aika = aika.get_date()
    paikka = paikka_input.get()
    viehe = viehe_input.get()
    vapa = vapa_input.get()
    print(laji)
    # cursor.execute(f'INSERT INTO kalastaja (nimi) VALUES ("{nimi}")')        
    # saa aina edellisen taulun id:n
    # kalastaja_id = cursor.lastrowid
    # cursor.execute(f'INSERT INTO viehe (viehe) VALUES ("{viehe}")')
    # viehe_id = cursor.lastrowid
    # cursor.execute(f'INSERT INTO vapa (vapa) VALUES ("{vapa}")')
    # vapa_id = cursor.lastrowid
    # cursor.execute(f'INSERT INTO laji (laji) VALUES ("{laji}")')
    # laji_id = cursor.lastrowid
    # cursor.execute(f'INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ("{saatu_aika}", "{kalastaja_id}", "{viehe_id}", "{vapa_id}", "{paikka}")')
    # tarppi_id = cursor.lastrowid
    # cursor.execute(f'INSERT INTO kala (tarppi_id, pituus, paino, laji_id) VALUES ("{tarppi_id}", "{pituus}", "{paino}", "{laji_id}")')
    # # tallettaa tapahtuneen tietokantaan
    # connection.commit()
    # # sulkee yhteyden tietokannan tauluihin
    # cursor.close()
# otsikko
l = tk.Label(root, text = "Kalastustiedot", font=('calibre',20,'bold'))
l.pack()

# luodaan inpu teille tyyppi
nimi_var=tk.StringVar()
pituus_var=tk.IntVar()
paino_var=tk.IntVar()
laji_var=tk.StringVar()
aika_var=tk.StringVar()
paikka_var=tk.StringVar()
viehe_var=tk.StringVar()
vapa_var=tk.StringVar()

# luodaan inputit ja labelit
nimi = tk.Label(root, text="Nimi:", font=('calibre',15))
nimi_input = tk.Entry(root, textvariable=nimi_var, font=('calibre',15,'normal'))
nimi.pack()
nimi_input.pack()

pituus = tk.Label(root, text="Pituus(cm):", font=('calibre',15))
pituus_input = tk.Entry(root, textvariable=pituus_var, font=('calibre',15,'normal'))
pituus.pack()
pituus_input.pack()

paino = tk.Label(root, text="Paino(kg):", font=('calibre',15))
paino_input = tk.Entry(root, textvariable=paino_var, font=('calibre',15,'normal'))
paino.pack()
paino_input.pack()

laji = tk.Label(root, text="Valiset kalalaji:", font=('calibre',15))
laji.pack()

luettelo_lajit = ["ahven", "hauki", "kuha", "siika", "taimen", "made", "lohi", "muu"]

laji_input = ttk.Combobox(root, values=luettelo_lajit, font=('calibre',15), textvariable=laji_var)
laji_input.set("Valiset kalalaji")
laji_input.pack()

def get_index(*args):
    # saa arvon joka valittu
    if str(laji_var.get()) == "muu":
        laji_input = tk.Entry(root, textvariable=laji_var, font=('calibre',15,'normal'))
        laji_input.pack()

# katsoo mikä arvo on valittu
laji_var.trace('w', get_index)
print(str(laji_var.get()))

aika_text = tk.Label(root, text="Aika:", font=('calibre',15))
aika = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2, font=('calibre',15,'normal'))
aika_input = tk.Entry(root, textvariable=aika_var, font=('calibre',15,'normal'))
aika_text.pack()
aika.pack()

paikka = tk.Label(root, text="Paikka:", font=('calibre',15))
paikka_input = tk.Entry(root, textvariable=paikka_var, font=('calibre',15,'normal'))
paikka.pack()
paikka_input.pack()

viehe = tk.Label(root, text="Viehe:", font=('calibre',15))
viehe_input = tk.Entry(root, textvariable=viehe_var, font=('calibre',15,'normal'))
viehe.pack()
viehe_input.pack()

vapa = tk.Label(root, text="Vapa:", font=('calibre',15))
vapa_input = tk.Entry(root, textvariable=vapa_var, font=('calibre',15,'normal'))
vapa.pack()
vapa_input.pack()

border = LabelFrame(root, borderwidth=2, background="black")
border.pack(pady = 10)
            
button = tk.Button(border, text="Lähetä", command=get_input, font=('calibre',15,'normal'), cursor="hand2")
button.pack()

if __name__=="__main__":
    root.mainloop()