import pymysql
import createdb
import dbinfo
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkcalendar import DateEntry
import os
# tarkistaa aina että tietokanta on olemassa
createdb.db()
# yhteys tietokantaan

USER = dbinfo.data["USER"]
PASSWORD = dbinfo.data["PASSWORD"]
DBNIMI = dbinfo.data["DBNIMI"]
PORT = dbinfo.data["PORT"]
HOST = dbinfo.data["HOST"]

connection = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DBNIMI)
cursor = connection.cursor()
# luodaan ikkuna
root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("1000x600")
root.title("Admin")
valikko = Menu(root)
# saadaan inputit
def get_input():
    nimi = nimi_input.get()
    pituus = pituus_input.get()
    paino = paino_input.get()
    laji = laji_input.get()
    if laji == "muu":
        laji = laji_input_muu.get()
    saatu_aika = aika.get_date()
    paikka = paikka_input.get()
    viehe = viehe_input.get()
    vapa = vapa_input.get()
    # print(nimi, pituus, paino, laji, saatu_aika, paikka, viehe, vapa)
    cursor.execute(f'INSERT INTO kalastaja (nimi) VALUES ("{nimi}")')        
    # saa aina edellisen taulun id:n
    kalastaja_id = cursor.lastrowid
    cursor.execute(f'INSERT INTO viehe (viehe) VALUES ("{viehe}")')
    viehe_id = cursor.lastrowid
    cursor.execute(f'INSERT INTO vapa (vapa) VALUES ("{vapa}")')
    vapa_id = cursor.lastrowid
    cursor.execute(f'INSERT INTO laji (laji) VALUES ("{laji}")')
    laji_id = cursor.lastrowid
    cursor.execute(f'INSERT INTO tarppi (aika, kalastaja_id, viehe_id, vapa_id, paikka) VALUES ("{saatu_aika}", "{kalastaja_id}", "{viehe_id}", "{vapa_id}", "{paikka}")')
    tarppi_id = cursor.lastrowid
    cursor.execute(f'INSERT INTO kala (tarppi_id, pituus, paino, laji_id) VALUES ("{tarppi_id}", "{pituus}", "{paino}", "{laji_id}")')
    # tallettaa tapahtuneen tietokantaan
    connection.commit()
    # sulkee yhteyden tietokannan tauluihin

# saa näytön leveyden
window_width = root.winfo_width()

# lasketaan x(leveys suunta) coordinaatiot keskelle sivua
x = (window_width + 400)
z = (window_width + 400)
nimi_paikka = (window_width + 350)
pituus_paikka = (window_width + 295)
paino_paikka = (window_width + 305)
laji_paikka = (window_width + 265)
aika_paikka = (window_width + 350)
paikka_paikka = (window_width + 330)
viehe_paikka = (window_width + 340)
vapa_paikka = (window_width + 340)
button_paikka = (window_width + 505)
laji_muu_paikka = (window_width + 315)

# otsikko
l = tk.Label(root, text = "Kalastustiedot", font=('calibre',20,'bold'))
l.place(x=x, y=25)

# luodaan inpu teille tyyppi
nimi_var=tk.StringVar()
pituus_var=tk.IntVar()
paino_var=tk.IntVar()
laji_var=tk.StringVar()
laji_var_muu=tk.StringVar()
aika_var=tk.StringVar()
paikka_var=tk.StringVar()
viehe_var=tk.StringVar()
vapa_var=tk.StringVar()

# luodaan inputit ja labelit
nimi = tk.Label(root, text="Nimi:", font=('calibre',15))
nimi_input = tk.Entry(root, textvariable=nimi_var, font=('calibre',15,'normal'))
nimi.place(x=nimi_paikka, y=70)
nimi_input.place(x=x, y=70)
    
pituus = tk.Label(root, text="Pituus(cm):", font=('calibre',15))
pituus_input = tk.Entry(root, textvariable=pituus_var, font=('calibre',15,'normal'))
pituus.place(x=pituus_paikka, y=110)
pituus_input.place(x=x, y=110)
    
paino = tk.Label(root, text="Paino(kg):", font=('calibre',15))
paino_input = tk.Entry(root, textvariable=paino_var, font=('calibre',15,'normal'))
paino.place(x=paino_paikka, y=150)
paino_input.place(x=x, y=150)
    

laji = tk.Label(root, text="Valiset kalalaji:", font=('calibre',15))
laji.place(x=laji_paikka, y=190)
    
luettelo_lajit = ["ahven", "hauki", "kuha", "siika", "taimen", "made", "lohi", "muu"]

laji_input = ttk.Combobox(root, values=luettelo_lajit, font=('calibre',15), textvariable=laji_var)
laji_input.set("Valiset kalalaji")
laji_input.place(x=x, y=190)
    
def get_index(*args):
    # saa arvon joka valittu
    if str(laji_var.get()) == "muu":
        global laji_input_muu 
        laji_muu = tk.Label(root, text="Mikä laji:", font=('calibre',15))
        laji_input_muu = tk.Entry(root, textvariable=laji_var_muu, font=('calibre',15,'normal'))
        laji_input_muu.place(x=x, y=230)
        laji_muu.place(x=laji_muu_paikka, y=230)

# katsoo mikä arvo on valittu
laji_var.trace('w', get_index)
# print(str(laji_var.get()))

aika_text = tk.Label(root, text="Aika:", font=('calibre',15))
aika = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2, font=('calibre',15,'normal'), date_pattern="dd.mm.yyyy")
aika_input = tk.Entry(root, textvariable=aika_var, font=('calibre',15,'normal'))
aika_text.place(x=aika_paikka, y=270)
aika.place(x=x, y=270)
    
paikka = tk.Label(root, text="Paikka:", font=('calibre',15))
paikka_input = tk.Entry(root, textvariable=paikka_var, font=('calibre',15,'normal'))
paikka.place(x=paikka_paikka, y=310)
paikka_input.place(x=x, y=310)
    
viehe = tk.Label(root, text="Viehe:", font=('calibre',15))
viehe_input = tk.Entry(root, textvariable=viehe_var, font=('calibre',15,'normal'))
viehe.place(x=viehe_paikka, y=350)
viehe_input.place(x=x, y=350)

vapa = tk.Label(root, text="Vapa:", font=('calibre',15))
vapa_input = tk.Entry(root, textvariable=vapa_var, font=('calibre',15,'normal'))
vapa.place(x=vapa_paikka, y=390)
vapa_input.place(x=x, y=390)
style = ttk.Style()
style.configure('TButton', font = ('calibri', 15, 'bold'), borderwidth = '4')
button = ttk.Button(text="Lähetä", command=get_input, style='TButton', cursor="hand2")
button.place(x=button_paikka, y=425)

# voit vaihtaa kuinka nopeaa dia esityse menee sivulla
def intecraatio():
    uusi_ikkuna = Toplevel(root)  
    uusi_ikkuna.title("Diaesityksen nopeus")
    uusi_ikkuna.geometry("400x250")  
    uusi_ikkuna.resizable(width=False, height=False)
    window_width = uusi_ikkuna.winfo_width()
    x = (window_width)
    nopeus_x = (x + 10)
    nopeus_input_x = (x + 90)
    button_x = (x + 135)
    error_x = (x + 90)

    def get_input():
        nopeus = nopeus_input.get()
        if len(nopeus) < 4 :
            error = tk.Label(uusi_ikkuna, text="Et antanut millisekuntteina", font=('calibre',15))
            error.place(x=error_x, y=100)
        else:
            cursor.execute(f'INSERT INTO integraatiot (diaNopeus) VALUES ("{nopeus}")')            
            # tallettaa tapahtuneen tietokantaan
            connection.commit()
    nopeus_var = tk.IntVar()
    nopeus = tk.Label(uusi_ikkuna, text="Anna diaesityksen nopeus(millisekuntteina):", font=('calibre',15))
    nopeus_input = tk.Entry(uusi_ikkuna, textvariable=nopeus_var, font=('calibre',15,'normal'))
    nopeus.place(x=nopeus_x, y=30) 
    nopeus_input.place(x=nopeus_input_x, y=70)
    button = ttk.Button(uusi_ikkuna, text="Lähetä", command=get_input, style='TButton', cursor="hand2")
    button.place(x=button_x, y=140)
valikko.add_command(label ='Vaihda dia esityksen nopeutta', command = intecraatio)
if __name__=="__main__":
    root.config(menu = valikko)
    root.mainloop()