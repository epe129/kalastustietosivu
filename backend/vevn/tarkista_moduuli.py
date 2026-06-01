"""
Moduuli tiedosto functiolle joka ottaa input arvon ja päivittää CTkListbox haun mukaan.
"""
from tkinter import END
import admin_window

def filter_haku(haku,
                tuotteet):
    """
    kun kirjoittaa inputtiin hakee tietoa ja rajaa sillä jos sana/kirjain on jossain arvossa.
    saa parametreista arvot.
    """
    data = []
    for item in tuotteet:
        if haku in str(item).lower():
            data.append(item)
    return data

def tarkistaa_input(
                    hae,
                    list_,
                    input_,
                    list_box,
                    paikat_1,
                    paikat_2,
                    paikat_3,
                    paikat_4
                    ):
    """
    Tehdään käyttäjien haku kun käyttää inputtia, ja päivittää CTkListbox haun mukaan.
    """
    # muokkaa kenttien ja nappin paikkoja sekä saa inputin
    hae_input = hae.get()
    admin_window.paikat(paikat_1)
    admin_window.paikat_unohtaa(paikat_2)
    # jos haku kenttä on tyhjä laittaa buttonit ja muut inputit/tekstit takaisin paikoilleen 
    if hae_input == '':
        data = list_
        admin_window.paikat(paikat_3)
        admin_window.paikat_unohtaa(paikat_4)
        input_.set("Poista käyttäjä")
        hae.delete(0, END)
    else:
        data = filter_haku(hae_input.lower(), list_)
    # päivittää listaa joka näkyy kun hakee inputilla
    admin_window.paivittaa_list_haku(data, list_box)
