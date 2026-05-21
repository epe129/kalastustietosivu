# jatka paikkojen korjausta
"""
admin window moduuli joka on tehty thinker- ja customtkinter:illä,
on ikkuna jossa admin voi poistaa käyttajiä, vieheitä, vapoja ja lajeja.
"""
import pymysql, dbinfo
import customtkinter as ctk
from tkinter import StringVar, END
from CTkListbox import CTkListbox

# yhteys tietokantaan, ottaa yhteyden tiedot python tidostosta
connection = pymysql.connect(host=dbinfo.data["HOST"], port=dbinfo.data["PORT"],
    user=dbinfo.data["USER"], password=dbinfo.data["PASSWORD"], database=dbinfo.data["DBNIMI"])
cursor = connection.cursor()

 # näisssä funktioissa käsitellään eri arvojen poistot
def kayttaja_poista(kayttajat_input, hae_kayttaja, button_kayttaja, text_vapa,
    hae_vapa, vapa_input, button_vapa, vapa_list_box, kayttajat_list_box, kayttajat_list):
    # tarkistaa kummasta ottaa arvon input vai valikosta 
    kayttaja_poista_input = kayttajat_input.get().split()
    if kayttaja_poista_input == "" or "Poista" in kayttaja_poista_input:
        kayttaja_poista_input = hae_kayttaja.get().split()
        # laitetaan labelit, inputit tms takasin paikalleen
        paikat = [
            (kayttajat_input, {"x": 210, "y": 160}),
            (button_kayttaja, {"x": 210, "y": 190}),
            (text_vapa, {"x": 210, "y": 250}),
            (hae_vapa, {"x": 210, "y": 280}),
            (vapa_input, {"x": 210, "y": 310}),
            (button_vapa, {"x": 210, "y": 340})
            ]
        for c, i in paikat:
            c.place(x=i["x"], y=i["y"])
          
        vapa_list_box.place_forget()
        kayttajat_list_box.place_forget()
        kayttajat_input.set("Poista käyttäjä")
        hae_kayttaja.delete(0, END)
    # poistetaan käyttäjä ja siihen kuuluvat tiedot
    cursor.execute(f"SELECT id FROM kalastaja WHERE email='{kayttaja_poista_input[0]}'")
    kayttajat_id = cursor.fetchall()
    cursor.execute(f"SELECT id FROM tarppi WHERE kalastaja_id='{kayttajat_id[0][0]}'")
    tarppi_idt = cursor.fetchall()
    for c in tarppi_idt:
        cursor.execute(f"DELETE FROM kala WHERE tarppi_id='{c[0]}'")
    cursor.execute(f"DELETE FROM tarppi WHERE kalastaja_id='{kayttajat_id[0][0]}'")
    cursor.execute(f"DELETE FROM kalastaja WHERE email='{kayttaja_poista_input[0]}'")
    # tallettaa tapahtuneen tietokantaan
    connection.commit()
    # päivittää listat ja luettelot
    cursor.execute("SELECT email FROM kalastaja")
    kayttajat = cursor.fetchall()
    kayttajat_input.configure(values=[x[0] for x in kayttajat])
    kayttajat_input.set("Poista käyttäjä")
    kayttajat_list.clear()
    for x in kayttajat:
        kayttajat_list.append(x[0])

def laji_poista(laji_input, hae_laji, button_laji, text_viehe, 
    hae_viehe, viehe_input, button_viehe, viehe_list_box, laji_list_box, lajit_list):
    # tarkistaa kummasta ottaa arvon input vai valikosta 
    saa_laji_input = laji_input.get().split()
    if saa_laji_input == "" or "Poista" in saa_laji_input:
        saa_laji_input = hae_laji.get().split()
        # laitetaan labelit, inputit tms takasin paikalleen
        laji_input.place(x=590, y=160)
        button_laji.place(x=590, y=190)
        text_viehe.place(x=590, y=250)
        hae_viehe.place(x=590, y=280) 
        viehe_input.place(x=590, y=310)
        button_viehe.place(x=590, y=340)
        viehe_list_box.place_forget()
        laji_list_box.place_forget()
        laji_input.set("Poista laji")
        hae_laji.delete(0, END)
    # ignooraa forekey ja poistaa tiedot
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")        
    cursor.execute(f"SELECT id FROM laji WHERE laji='{saa_laji_input[0]}'")
    laji_id = cursor.fetchall()
    cursor.execute(f"UPDATE kala set laji_id = NULL WHERE laji_id ='{laji_id[0][0]}'")        
    cursor.execute(f"DELETE FROM laji WHERE laji='{saa_laji_input[0]}'")        
    # tallettaa tapahtuneen tietokantaan
    connection.commit()
    # päivittää listat ja luettelot
    cursor.execute("SELECT laji FROM laji")
    lajit = cursor.fetchall()
    laji_input.configure(values=[x[0] for x in lajit])
    laji_input.set("Poista käyttäjä")
    lajit_list.clear()
    for x in lajit:
        lajit_list.append(x[0])

def vapa_poista(vapa_input, hae_vapa, button_vapa, vapa_list_box, vavat_list):
    # tarkistaa kummasta ottaa arvon input vai valikosta 
    saa_vapa_input = vapa_input.get().split()
    if saa_vapa_input == "" or "Poista" in saa_vapa_input:
        saa_vapa_input = hae_vapa.get().split()
        vapa_input.place(x=210, y=310)
        button_vapa.place(x=210, y=340)
        vapa_list_box.place_forget()
        vapa_input.set("Poista viehe")
        hae_vapa.delete(0, END)
    # ignooraa  forekey ja poistaa tiedot
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")        
    cursor.execute(f"SELECT id FROM vapa WHERE vapa ='{saa_vapa_input[0]}'")
    vapa_id = cursor.fetchall()
    cursor.execute(f"UPDATE tarppi set vapa_id = NULL WHERE vapa_id ='{vapa_id[0][0]}'") 
    cursor.execute(f"DELETE FROM vapa WHERE vapa='{saa_vapa_input[0]}'")        
    # tallettaa tapahtuneen tietokantaan
    connection.commit()
    # päivittää listat ja luettelot
    cursor.execute("SELECT vapa FROM vapa")
    vavat = cursor.fetchall()
    vapa_input.configure(values=[x[0] for x in vavat])
    vapa_input.set("Poista vapa")
    vavat_list.clear()
    for x in vavat:
        vavat_list.append(x[0])

def viehe_poista(viehe_input, hae_viehe, button_viehe, viehe_list_box, viehet_list):
    # tarkistaa kummasta ottaa arvon input vai valikosta 
    saa_viehe_input = viehe_input.get().split()
    if saa_viehe_input == "" or "Poista" in saa_viehe_input:
        saa_viehe_input = hae_viehe.get().split()
        viehe_input.place(x=590, y=310)
        button_viehe.place(x=590, y=340)
        viehe_list_box.place_forget()
        viehe_input.set("Poista viehe")
        hae_viehe.delete(0, END)
    # ignooraa forekey ja poistaa tiedot
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")        
    cursor.execute(f"SELECT id FROM viehe WHERE viehe ='{saa_viehe_input[0]}'")
    viehe_id = cursor.fetchall()
    cursor.execute(f"UPDATE tarppi set viehe_id = NULL WHERE viehe_id ='{viehe_id[0][0]}'") 
    cursor.execute(f"DELETE FROM viehe WHERE viehe='{saa_viehe_input[0]}'")        
    # tallettaa tapahtuneen tietokantaan
    connection.commit()
    # päivittää listat ja luettelot
    cursor.execute("SELECT viehe FROM viehe")
    viehet = cursor.fetchall()
    viehe_input.configure(values=[x[0] for x in viehet])
    viehe_input.set("Poista viehe")
    viehet_list.clear()
    for x in viehet:
        viehet_list.append(x[0])

# päivitää listoja jotka näkyy kun hakee inputissa
def paivittaa_list(kayttajat_list, box):
    # poistaa kaiken inputista, näin jotta käy yksitellen jokaisen läpi niin ei tuu erroria
    for _ in range(box.size()):
        box.delete(0)
    # tarkistaa että list box koko on 0
    if box.size() == 0:
        # lisää arvot uudestaan listaa jotta päivittyy
        for index, item in enumerate(kayttajat_list):
            box.insert(index, item)

# laittaa clikatun valuen inputtiin
def tayttaa_input(hae, box):
    # poistaa kaiken inputista
    hae.delete(0, END)
    # tarkistaa että list box koko on suurempi kuin nolla
    if box.size() > 0:
        # lisää klikatun arvon inputtiin
        hae.insert(0, box.get())

def filter_haku(haku, tuotteet):
    data = []
    for item in tuotteet:
        if haku in str(item).lower():
            data.append(item)
    return data
    
# ottaa input arvon ja päivittää listaa haun mukaan
# place_forget() poistaa kentä nykyiseltä paikalta
def tarkistaa_input_kayttaja(hae_kayttaja, kayttajat_list_box, button_kayttaja, 
    kayttajat_input, text_vapa, hae_vapa, vapa_input, button_vapa, vapa_list_box, kayttajat_list):
    # muokka kenttien ja nappin paikkoja sekä saa inputin
    hae_kayttaja_input = hae_kayttaja.get()
    kayttajat_list_box.place(x=210, y=165)
    button_kayttaja.place(x=423, y=130)
    kayttajat_input.place_forget()
    text_vapa.place_forget()
    hae_vapa.place_forget() 
    vapa_input.place_forget()
    button_vapa.place_forget()
    vapa_list_box.place_forget()
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if hae_kayttaja_input == '':
        data_kayttaja = kayttajat_list
        kayttajat_input.place(x=210, y=160)  
        button_kayttaja.place(x=210, y=190)
        text_vapa.place(x=210, y=250)
        hae_vapa.place(x=210, y=280) 
        vapa_input.place(x=210, y=310)
        button_vapa.place(x=210, y=340)
        vapa_list_box.place_forget()
        kayttajat_list_box.place_forget()
        kayttajat_input.set("Poista käyttäjä")
        hae_kayttaja.delete(0, END)
    else:
        # kun kirjoittaa inputtiin hakee tietoa ja
        # rajaa sillä jos sana/kirjain on jossain arvossa
        data_kayttaja = filter_haku(hae_kayttaja_input.lower(), kayttajat_list)
    # päivittää listaa joka näkyy kun hakee haun perusteella
    paivittaa_list(data_kayttaja, kayttajat_list_box)
     
    
def tarkistaa_input_laji(hae_laji, laji_list_box, button_laji, laji_input,
    text_viehe, hae_viehe, viehe_input, button_viehe, viehe_list_box, lajit_list):
    # muokka kenttien ja nappin paikkoja sekä saa inputin
    laji_kayttaja_input = hae_laji.get()
    laji_list_box.place(x=590, y=165)
    button_laji.place(x=803, y=130)
    laji_input.place_forget()
    text_viehe.place_forget()
    hae_viehe.place_forget() 
    viehe_input.place_forget()
    button_viehe.place_forget()
    viehe_list_box.place_forget()
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if laji_kayttaja_input == '':
        data_laji = lajit_list
        laji_input.place(x=590, y=160)
        button_laji.place(x=590, y=190)
        text_viehe.place(x=590, y=250)
        hae_viehe.place(x=590, y=280) 
        viehe_input.place(x=590, y=310)
        button_viehe.place(x=590, y=340)
        viehe_list_box.place_forget()
        laji_list_box.place_forget()
        laji_input.set("Poista laji")
        hae_laji.delete(0, END)
    else:
        # kun kirjoittaa inputtiin hakee tietoa ja rajaa sillä jos sana/kirjaimet on jossain arvossa
        data_laji = filter_haku(laji_kayttaja_input.lower(), lajit_list)
    # päivittää listaa joka näkyy kun hakee haun perusteella
    paivittaa_list(data_laji, laji_list_box)
    
def tarkistaa_input_viehe(hae_viehe, viehe_list_box, button_viehe, viehe_input, viehet_list):
    # muokka kenttien ja nappin paikkoja sekä saa inputin
    viehe_kayttaja_input = hae_viehe.get()
    viehe_list_box.place(x=590, y=310)
    button_viehe.place(x=803, y=280)
    viehe_input.place_forget()
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if viehe_kayttaja_input == '':
        data_viehe = viehet_list
        viehe_input.place(x=590, y=310)
        button_viehe.place(x=590, y=340)
        viehe_list_box.place_forget()
        viehe_input.set("Poista viehe")
        hae_viehe.delete(0, END)
    else:
        # kun kirjoittaa inputtiin hakee tietoa ja rajaa sillä jos sana/kirjaimet on jossain arvossa           
        data_viehe = filter_haku(viehe_kayttaja_input.lower(), viehet_list)
    # päivittää listaa joka näkyy kun hakee haun perusteella
    paivittaa_list(data_viehe, viehe_list_box)

def tarkistaa_input_vapa(hae_vapa, vapa_list_box, button_vapa, vapa_input, vavat_list):
    # muokka kenttien ja nappin paikkoja sekä saa inputin
    vapa_input_hae = hae_vapa.get()
    vapa_list_box.place(x=210, y=310)
    button_vapa.place(x=423, y=280)
    vapa_input.place_forget()
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if vapa_input_hae == '':
        data_vapa = vavat_list
        vapa_input.place(x=210, y=310)
        button_vapa.place(x=210, y=340)
        vapa_list_box.place_forget()
        vapa_input.set("Poista viehe")
        hae_vapa.delete(0, END)
    else:
        # kun kirjoittaa inputtiin hakee tietoa ja rajaa sillä jos sana/kirjaimet on jossain arvossa
        data_vapa = filter_haku(vapa_input_hae.lower(), vavat_list)
    # päivittää listaa joka näkyy kun hakee haun perusteella
    paivittaa_list(data_vapa, vapa_list_box)



def admin_window(root):
    """
    luodaan admin ikkuna ja siihen buttonit, labelit, luettelot ja tekstit.
    lambda sallii lähettää parametreja kun esim buttoni kutsuu functiota.
    """
    # luodaan listat
    kayttajat_list = []
    lajit_list = []
    vavat_list = []
    viehet_list = []

    # lisää listoihin arvot tietokannasta jotka näkyy jos käyttäjä käyttää syöttö kenttää
    cursor.execute("SELECT email FROM kalastaja")
    kayttajat = cursor.fetchall()
    for x in kayttajat:
        kayttajat_list.append(x[0])

    cursor.execute("SELECT laji FROM laji")
    lajit = cursor.fetchall()
    for l in lajit:
        lajit_list.append(l[0])

    cursor.execute("SELECT vapa FROM vapa")
    vavat = cursor.fetchall()
    for va in vavat:
        vavat_list.append(va[0])

    cursor.execute("SELECT viehe FROM viehe")
    viehet = cursor.fetchall()
    for vi in viehet:
        viehet_list.append(vi[0])

    # luodaan ikkuna
    window = ctk.CTkToplevel(root)
    window.geometry("1000x600")
    window.resizable(width=False, height=False)
    window.title("Admin")

    #  luodaan frame, jotta kaikki admin_window buttonit,
    #  label tms täbin sisällä pysyvät aina samassa paikassa
    container = ctk.CTkFrame(window, width=1000, height=600)
    container.place(x=0, y=0)
                   
    # luodaan inpu teille tyyppit
    hae_string_var = StringVar()
    laji_hae_string_var = StringVar()
    vapa_hae_string_var = StringVar()
    viehe_hae_string_var = StringVar()

    # koko ikkunan otsikko
    ctk.CTkLabel(container, text="Admin", font=('calibre',40)).place(x=450, y=25)

    # otsikko
    ctk.CTkLabel(container, text="Poista käyttäjä:", font=('calibre',20)).place(x=210, y=100)

    # luodaan luettelo jossa näkyy arvot jos käyttää haku kenttää
    kayttajat_list_box = CTkListbox(container, width=200)

    # hakukenttä
    hae_kayttaja = ctk.CTkEntry(container, textvariable=hae_string_var,
                                font=('calibre',12,'normal'), width=200)
    hae_kayttaja.place(x=210, y=130)        

    # luettelo boxsi
    kayttajat_input = ctk.CTkComboBox(container, values=[x[0] for x in kayttajat],
                                        font=('calibre',15))
    kayttajat_input.set("Poista käyttäjä")
    kayttajat_input.place(x=210, y=160)

    # button
    button_kayttaja = ctk.CTkButton(master=container ,text="Poista käyttäjä", command=lambda: kayttaja_poista(
        kayttajat_input,
        hae_kayttaja,
        button_kayttaja,
        text_vapa,
        hae_vapa,
        vapa_input,
        button_vapa,
        vapa_list_box,
        kayttajat_list_box,
        kayttajat_list
    ))
    button_kayttaja.place(x=210, y=190)

    # kuuntelee jos kayttajat_list_box arvo klikattu
    kayttajat_list_box.bind("<Button-1>", lambda e: tayttaa_input(hae_kayttaja, kayttajat_list_box))
    # päivittää kayttajat_list_box
    paivittaa_list(kayttajat_list, kayttajat_list_box)    
    # kuuntelee jos inputtiin kirjoitetaan
    hae_kayttaja.bind('<KeyRelease>', lambda e: tarkistaa_input_kayttaja(
        hae_kayttaja,
        kayttajat_list_box,
        button_kayttaja,
        kayttajat_input,
        text_vapa,
        hae_vapa,
        vapa_input,
        button_vapa,
        vapa_list_box,
        kayttajat_list
    ))

    # otsikko
    ctk.CTkLabel(container, text="Poista laji:", font=('calibre',20)).place(x=590, y=100)
    
    # luodaan luettelo jossa näkyy arvot jos käyttää haku kenttää
    laji_list_box = CTkListbox(container, width=200)

    # hakukenttä
    hae_laji = ctk.CTkEntry(container, textvariable=laji_hae_string_var,
                            font=('calibre',12,'normal'), width=200)
    hae_laji.place(x=590, y=130) 

    # luettelo boxsi
    laji_input = ctk.CTkComboBox(container, values=[x[0] for x in lajit], font=('calibre',15))
    laji_input.set("Poista laji")
    laji_input.place(x=590, y=160)

    # button
    button_laji = ctk.CTkButton(master=container ,text="Poista laji", command=lambda: laji_poista(
        laji_input,
        hae_laji,
        button_laji,
        text_viehe,
        hae_viehe,
        viehe_input,
        button_viehe,
        viehe_list_box,
        laji_list_box,
        lajit_list
    ))
    button_laji.place(x=590, y=190)

    # kuuntelee jos laji_list_box arvo klikattu
    laji_list_box.bind("<Button-1>", lambda e: tayttaa_input(hae_laji, laji_list_box))
    # päivittää laji_list_box
    paivittaa_list(lajit_list, laji_list_box)    
    # kuuntelee jos inputtiin kirjoitetaan
    hae_laji.bind('<KeyRelease>', lambda e: tarkistaa_input_laji(
        hae_laji,
        laji_list_box,
        button_laji,
        laji_input,
        text_viehe,
        hae_viehe,
        viehe_input,
        button_viehe,
        viehe_list_box,
        lajit_list
    ))

    # otsikko
    text_vapa = ctk.CTkLabel(container, text="Poista vapa:", font=('calibre',20))
    text_vapa.place(x=210, y=250)

    # luodaan luettelo jossa näkyy arvot jos käyttää haku kenttää
    vapa_list_box = CTkListbox(container, width=200)

    # hakukenttä
    hae_vapa = ctk.CTkEntry(container, textvariable=vapa_hae_string_var,
                            font=('calibre',12,'normal'), width=200)
    hae_vapa.place(x=210, y=280) 

    # luettelo boxsi
    vapa_input = ctk.CTkComboBox(container, values=[x[0] for x in vavat], font=('calibre',15))
    vapa_input.set("Poista vapa")
    vapa_input.place(x=210, y=310)
    
    # button
    button_vapa = ctk.CTkButton(master=container ,text="Poista vapa", command=lambda: vapa_poista(
        vapa_input,
        hae_vapa,
        button_vapa,
        vapa_list_box,
        vavat_list
    ))
    button_vapa.place(x=210, y=340)

    # kuuntelee jos vapa_list_box arvo klikattu
    vapa_list_box.bind("<Button-1>", lambda e: tayttaa_input(hae_vapa, vapa_list_box))
    # päivittää vapa_list_box
    paivittaa_list(vavat_list, vapa_list_box)    
    # kuuntelee jos inputtiin kirjoitetaan
    hae_vapa.bind('<KeyRelease>', lambda e: tarkistaa_input_vapa(
        hae_vapa,
        vapa_list_box,
        button_vapa,
        vapa_input,
        vavat_list
    ))

    # otsikko
    text_viehe = ctk.CTkLabel(container, text="Poista viehe:", font=('calibre',20))
    text_viehe.place(x=590, y=250)

    # luodaan luettelo jossa näkyy arvot jos käyttää haku kenttää
    viehe_list_box = CTkListbox(container, width=200)
    
    # hakukenttä
    hae_viehe = ctk.CTkEntry(container, textvariable=viehe_hae_string_var, 
                            font=('calibre',12,'normal'), width=200)
    hae_viehe.place(x=590, y=280) 

    # luettelo boxsi
    viehe_input = ctk.CTkComboBox(container, values=[x[0] for x in viehet], font=('calibre',15))
    viehe_input.set("Poista viehe")
    viehe_input.place(x=590, y=310)
    
    # button
    button_viehe = ctk.CTkButton(master=container ,text="Poista viehe", command=lambda: viehe_poista(
        viehe_input,
        hae_viehe,
        button_viehe,
        viehe_list_box,
        viehet_list
    ))
    button_viehe.place(x=590, y=340)
  
    # kuuntelee jos viehe_list_box arvo klikattu
    viehe_list_box.bind("<Button-1>", lambda e: tayttaa_input(hae_viehe, viehe_list_box))
    # päivittää viehe_list_box
    paivittaa_list(viehet_list, viehe_list_box)
    # kuuntelee jos inputtiin kirjoitetaan
    hae_viehe.bind('<KeyRelease>', lambda e: tarkistaa_input_viehe(
        hae_viehe,
        viehe_list_box,
        button_viehe,
        viehe_input,
        viehet_list
    ))

    # jos painaa x:sää sulkee ikkunan
    def close():
        root.destroy()
    window.protocol("WM_DELETE_WINDOW", close)
