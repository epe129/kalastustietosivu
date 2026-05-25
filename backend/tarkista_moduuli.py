"""
Moduuli tiedosto functioille jotka ottaa input arvon ja päivittää listaa haun mukaan.
"""
import admin_window
from tkinter import END

def tarkistaa_input_kayttaja(hae_kayttaja, kayttajat_list_box, button_kayttaja, kayttajat_input, text_vapa, hae_vapa, vapa_input, button_vapa, vapa_list_box, kayttajat_list):
    # muokkaa kenttien ja nappin paikkoja sekä saa inputin
    hae_kayttaja_input = hae_kayttaja.get()
    admin_window.paikat([(kayttajat_list_box, {"x": 210, "y": 165}), (button_kayttaja, {"x": 423, "y": 130})])
    admin_window.paikat_unohtaa([kayttajat_input,text_vapa,hae_vapa, vapa_input,button_vapa,vapa_list_box])
    
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if hae_kayttaja_input == '':
        data_kayttaja = kayttajat_list
        admin_window.paikat([(kayttajat_input, {"x": 210, "y": 160}), (button_kayttaja, {"x": 210, "y": 190}), (text_vapa, {"x": 210, "y": 250}), (hae_vapa, {"x": 210, "y": 280}), (vapa_input, {"x": 210, "y": 310}), (button_vapa, {"x": 210, "y": 340})])
        admin_window.paikat_unohtaa([vapa_list_box,kayttajat_list_box])
        kayttajat_input.set("Poista käyttäjä")
        hae_kayttaja.delete(0, END)
    else:
        data_kayttaja = admin_window.filter_haku(hae_kayttaja_input.lower(), kayttajat_list)
    
    # päivittää listaa joka näkyy kun hakee haun perusteella
    admin_window.paivittaa_list_haku(data_kayttaja, kayttajat_list_box)
         
def tarkistaa_input_laji(hae_laji, laji_list_box, button_laji, laji_input, text_viehe, hae_viehe, viehe_input, button_viehe, viehe_list_box, lajit_list):    
    # muokkaa kenttien ja nappin paikkoja sekä saa inputin
    laji_kayttaja_input = hae_laji.get()
    admin_window.paikat([(laji_list_box, {"x": 590, "y": 165}), (button_laji, {"x": 803, "y": 130})])
    admin_window.paikat_unohtaa([laji_input,text_viehe,hae_viehe, viehe_input,button_viehe,viehe_list_box])
    
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if laji_kayttaja_input == '':
        data_laji = lajit_list
        admin_window.paikat([(laji_input, {"x": 590, "y": 160}), (button_laji, {"x": 590, "y": 190}), (text_viehe, {"x": 590, "y": 250}), (hae_viehe, {"x": 590, "y": 280}), (viehe_input, {"x": 590, "y": 310}), (button_viehe, {"x": 590, "y": 340})])
        admin_window.paikat_unohtaa([viehe_list_box,laji_list_box])
        laji_input.set("Poista laji")
        hae_laji.delete(0, END)
    else:
        data_laji = admin_window.filter_haku(laji_kayttaja_input.lower(), lajit_list)
    
    # päivittää listaa joka näkyy kun hakee haun perusteella
    admin_window.paivittaa_list_haku(data_laji, laji_list_box)
    
def tarkistaa_input_viehe(hae_viehe, viehe_list_box, button_viehe, viehe_input, viehet_list):
    # muokkaa kenttien ja nappin paikkoja sekä saa inputin
    viehe_kayttaja_input = hae_viehe.get()
    admin_window.paikat([(viehe_list_box, {"x": 590, "y": 310}), (button_viehe, {"x": 803, "y": 280})])
    admin_window.paikat_unohtaa([viehe_input])
    
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if viehe_kayttaja_input == '':
        data_viehe = viehet_list
        admin_window.paikat([(viehe_input, {"x": 590, "y": 310}), (button_viehe, {"x": 590, "y": 340})])
        admin_window.paikat_unohtaa([viehe_list_box])
        viehe_input.set("Poista viehe")
        hae_viehe.delete(0, END)
    else:
        data_viehe = admin_window.filter_haku(viehe_kayttaja_input.lower(), viehet_list)
    
    # päivittää listaa joka näkyy kun hakee haun perusteella
    admin_window.paivittaa_list_haku(data_viehe, viehe_list_box)

def tarkistaa_input_vapa(hae_vapa, vapa_list_box, button_vapa, vapa_input, vavat_list):    
    # muokkaa kenttien ja nappin paikkoja sekä saa inputin
    vapa_input_hae = hae_vapa.get()
    admin_window.paikat([(vapa_list_box, {"x": 210, "y": 310}), (button_vapa, {"x": 423, "y": 280})])
    admin_window.paikat_unohtaa([vapa_input])
    
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if vapa_input_hae == '':
        data_vapa = vavat_list
        admin_window.paikat([(vapa_input, {"x": 210, "y": 310}), (button_vapa, {"x": 210, "y": 340})])
        admin_window.paikat_unohtaa([vapa_list_box])
        vapa_input.set("Poista viehe")
        hae_vapa.delete(0, END)
    else:
        data_vapa = admin_window.filter_haku(vapa_input_hae.lower(), vavat_list)
    
    # päivittää listaa joka näkyy kun hakee haun perusteella
    admin_window.paivittaa_list_haku(data_vapa, vapa_list_box)
