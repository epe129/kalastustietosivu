import pymysql, createdb, dbinfo, datetime 
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkcalendar import DateEntry

# tarkistaa aina että tietokanta on olemassa
createdb.db()

# otetaan db tiedot python tiedostosta
USER = dbinfo.data["USER"]
PASSWORD = dbinfo.data["PASSWORD"]
DBNIMI = dbinfo.data["DBNIMI"]
PORT = dbinfo.data["PORT"]
HOST = dbinfo.data["HOST"]

# yhteys tietokantaan
connection = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD, database=DBNIMI)
cursor = connection.cursor()

# luodaan ikkuna
root = tk.Tk()
root.resizable(width=False, height=False)
root.geometry("1000x600")
root.title("Admin")

def get_input():
    try:
        # saadaan inputit
        nimi = nimi_input.get()
        laji = laji_input.get()
        saatu_aika = aika.get_date()
        paikka = paikka_input.get()
        viehe = viehe_input.get()
        vapa = vapa_input.get()
        x = datetime.datetime.now()
        nyky_aika = x.strftime("%Y-%m-%d")
        # tarkistaa pituus ja paino ovat lukuja
        try:
            pituus = float(pituus_input.get())
            paino = float(paino_input.get())
        except:
            # asettaa tekstin 
            text.place(x=window_width + 350, y=425)
            my_string_var.set("Pituus ja paino kohtiin pitää laittaa luku")
            return
        # jos on muu laji ottaa muu laji inputin
        if laji == "muu":
            laji = laji_input_muu.get()
            # tuhoaa inputin
            laji_input_muu.delete(0, END)
        # tarkistaa ettei päivämäärä ole nyky aikaa suurempi
        if str(saatu_aika) > str(nyky_aika):
            text.place(x=window_width + 325, y=425)
            my_string_var.set("Et voi laitta nykyaikaa suurempaa aikaa")
            return
        # tarkistaa ettei arvot ole tyhjiä tai jos on arvoja jotka ei kelpaa
        if nimi == "" or pituus == "" or paino == "" or paino == "0" or pituus == "0" or laji == "Valiset kalalaji" or laji == "" or paikka == "" or viehe == "" or vapa == "":
            text.place(x=window_width + 335, y=425)
            my_string_var.set("Et täyttänyt kaikkia kohtia tai valinnut lajia")
            return   
        print(len(nimi))
        if len(nimi) > 24 or len(laji) > 24 or len(viehe) > 24 or len(paikka) > 24 or len(vapa) > 24:
            text.place(x=window_width + 370, y=425)
            my_string_var.set("Maksimi merkkien määrä on 24")
            return
        if len(str(pituus)) > 6 or len(str(paino)) > 6:
            text.place(x=window_width + 300, y=425)
            my_string_var.set("Painon ja pituuden maksimi merkkien määrä on 6")
            return
        # lähettää tiedot tietokantaan  
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
        # asettaa tekstin 
        text.place(x=window_width + 400, y=425)
        my_string_var.set("Tiedot lisättiin onnistuneesti")
    except:
        text.place(x=window_width + 425, y=425)
        my_string_var.set("Jokin meni vikaan")
    tyhjenna_inputit()

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
button_paikka = (window_width + 565)
laji_muu_paikka = (window_width + 315)

# luodaan teksti kenttä jossa teksti voi muuttua
my_string_var = StringVar()
my_string_var.set("")
text = tk.Label(root, textvariable=my_string_var, font=('calibre',15))
text.place(x=window_width + 350, y=425)

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
nimi_input = tk.Entry(root, textvariable=nimi_var, font=('calibre',15,'normal'), width=25)
nimi.place(x=nimi_paikka, y=70)
nimi_input.place(x=x, y=70)
    
pituus = tk.Label(root, text="Pituus(cm):", font=('calibre',15))
pituus_input = tk.Entry(root, textvariable=pituus_var, font=('calibre',15,'normal'), width=25)
pituus.place(x=pituus_paikka, y=110)
pituus_input.place(x=x, y=110)
    
paino = tk.Label(root, text="Paino(kg):", font=('calibre',15))
paino_input = tk.Entry(root, textvariable=paino_var, font=('calibre',15,'normal'), width=25)
paino.place(x=paino_paikka, y=150)
paino_input.place(x=x, y=150)

laji = tk.Label(root, text="Valiset kalalaji:", font=('calibre',15))
laji.place(x=laji_paikka, y=190)
    
luettelo_lajit = ["ahven", "hauki", "kuha", "siika", "taimen", "made", "lohi", "muu"]

laji_input = ttk.Combobox(root, values=luettelo_lajit, font=('calibre',15), textvariable=laji_var, state="readonly")
laji_input.set("Valiset kalalaji")
laji_input.place(x=x, y=190)
    
def saa_arvon(*args):
    # jos arvo on muu laittaa input johon käyttäjä voi itse kirjoittaa lajin
    if str(laji_var.get()) == "muu":
        global laji_input_muu
        global laji_muu
        laji_muu = tk.Label(root, text="Mikä laji:", font=('calibre',15))
        laji_input_muu = tk.Entry(root, textvariable=laji_var_muu, font=('calibre',15,'normal'), width=25)
        laji_input_muu.place(x=x, y=230)
        laji_muu.place(x=laji_muu_paikka, y=230)
   

# katsoo mikä arvo on valittu luettelosta
laji_var.trace('w', saa_arvon)

aika_text = tk.Label(root, text="Aika:", font=('calibre',15))
aika = DateEntry(root, width=12, background="darkblue", foreground="white", borderwidth=2, font=('calibre',15,'normal'), date_pattern="dd.mm.yyyy")
aika_input = tk.Entry(root, textvariable=aika_var, font=('calibre',15,'normal'))
aika_text.place(x=aika_paikka, y=270)
aika.place(x=x, y=270)

paikka = tk.Label(root, text="Paikka:", font=('calibre',15))
paikka_input = tk.Entry(root, textvariable=paikka_var, font=('calibre',15,'normal'), width=25)
paikka.place(x=paikka_paikka, y=310)
paikka_input.place(x=x, y=310)
    
viehe = tk.Label(root, text="Viehe:", font=('calibre',15))
viehe_input = tk.Entry(root, textvariable=viehe_var, font=('calibre',15,'normal'), width=25)
viehe.place(x=viehe_paikka, y=350)
viehe_input.place(x=x, y=350)

vapa = tk.Label(root, text="Vapa:", font=('calibre',15))
vapa_input = tk.Entry(root, textvariable=vapa_var, font=('calibre',15,'normal'), width=25)
vapa.place(x=vapa_paikka, y=390)
vapa_input.place(x=x, y=390)

def tyhjenna_inputit():
   # tyhjen tää inputit kun arvot lähetetty
   nimi_input.delete(0, END)
   pituus_input.delete(0, END)
   paino_input.delete(0, END)
   laji_input.set("Valiset kalalaji")
   paikka_input.delete(0, END)
   viehe_input.delete(0, END)
   vapa_input.delete(0, END)
   # jos on käytetty muu inputtia tuhoaa sen muuten jos ei ole käytetty jättää huomioimatta siitä saadun errorin    
   try:
    laji_input_muu.destroy()
    laji_muu.destroy()
   except:
       pass
   
# luodaan tyylit buttoniin ja luodaan buttoni
style = ttk.Style()
style.configure('TButton', font = ('calibri', 15, 'bold'), borderwidth = '4')
button = ttk.Button(text="Lähetä", command=get_input, style='TButton', cursor="hand2")
button.place(x=button_paikka, y=475)

# voit vaihtaa kuinka nopeaa dia esitys menee sivulla
def intecraatio():
    # luodaa uusi ikkuna
    uusi_ikkuna = Toplevel(root)  
    uusi_ikkuna.title("Diaesityksen nopeus")
    uusi_ikkuna.geometry("450x250")  
    uusi_ikkuna.resizable(width=False, height=False)
    window_width = uusi_ikkuna.winfo_width()
    # asetetaan elementtien sijainnit leveys suunnassa
    x = (window_width)
    nopeus_x = (x + 5)
    nopeus_input_x = (x + 90)
    button_x = (x + 135)
    def get_input():
        s = 0
        nopeus = nopeus_input.get()
        # tarkistaa ettei ole tyhjä
        if nopeus == "": 
            # asettaa tekstin
            text_var.set("Annoit tyhjän arvon")
            text.place(x=x+110, y=100)
            return
        # tarkistaa että nopeus on int
        if isinstance(nopeus, str):
            text.place(x=x+10, y=100)
            # asettaa tekstin
            text_var.set("Annoit kirjaimia, pitää olla numero väliltä 1-20")
        # laskee millisekunteiksi
        s = int(nopeus) * 1000
        # tarkistaa että nopeus on oikealla arvo alueeella
        if s > 20000 or s < 1000:
            # asettaa tekstin
            text.place(x=x+10, y=100)
            text_var.set("Annoit joko liian suuren tai liian pienen luvun")
            return
        cursor.execute(f'INSERT INTO integraatiot (diaNopeus) VALUES ("{s}")')            
        # tallettaa tapahtuneen tietokantaan
        connection.commit()
        text_var.set("Vaihtui onnistuneesti")
        text.place(x=x+110, y=100)
    text_var = StringVar()
    text_var.set("")
    # luodaan inputit ja labelit
    text = tk.Label(uusi_ikkuna, textvariable = text_var, font=('calibre',15))
    text.place(x=x+10, y=100)
    nopeus_var = tk.IntVar()
    nopeus = tk.Label(uusi_ikkuna, text="Anna diaesityksen nopeus sekunteina(1-20):", font=('calibre',15))
    nopeus_input = tk.Entry(uusi_ikkuna, textvariable=nopeus_var, font=('calibre',15,'normal'))
    nopeus.place(x=nopeus_x, y=30) 
    nopeus_input.place(x=nopeus_input_x, y=70)
    button = ttk.Button(uusi_ikkuna, text="Lähetä", command=get_input, style='TButton', cursor="hand2")
    button.place(x=button_x, y=140)
# luodaan buttoniin tyyli ja buttoni
style.configure('W.TButton', font = ('calibri', 17, 'bold'), borderwidth = '4')
button = ttk.Button(text="Vaihda diaesityksen nopeutta", command=intecraatio, style='W.TButton', cursor="hand2")
button.place(x=5, y=5)

if __name__=="__main__":
    root.mainloop()