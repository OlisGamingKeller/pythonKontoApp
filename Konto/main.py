# ----------------------------------------------------------------------
#  Titel     : main.py
# ----------------------------------------------------------------------
#  Funktion  : Hauptprogramm (Konsolenmenü)
# ----------------------------------------------------------------------
#  Sprache   : Python
#  Datum     : 04.05.26
#  Autor     : O. Linke
# ----------------------------------------------------------------------
# 
# ----------------------------------------------------------------------
import os
import subprocess
from konto import Konto

konten = []

# Hilfsfunktionen
def konsole_leeren():
    if os.name == 'nt':
        subprocess.run(['cls'], shell=True)
    else:
        subprocess.run(['clear'])

def konto_anlegen():
    name = input("Name: ")
    while True:
        try:
            kontonummer = int(input("Kontonummer: "))
            break
        except ValueError:
            print("Bitte eine gültige Kontonummer eingeben.")
        
    while True:
        try:
            eingabe = input("Kontostand: ").replace(",",".")
            kontostand = float(eingabe)
            break
        except ValueError:
            print("Bitte einen gültigen Betrag eingeben.")
        
    konto = Konto(kontonummer, name, kontostand)

    konsole_leeren()

    print("Bitte Eingabe prüfen:")
    konto.anzeigen()
    
    bestaetigung = input("Konto speichern? (j/n): ")
    if bestaetigung.lower() == "j":
        return konto
    else:
        return None

def konto_suchen(konten):
    if len(konten) == 0:
        print("Keine Konten vorhanden.")
        return None
    
    suchbegriff = input("Geben Sie Kontonummer oder Name ein: ")

    try:
        gesuchte_kontonummer = int(suchbegriff)

        for konto in konten:
            if konto.kontonummer == gesuchte_kontonummer:
                return konto

        print("Kein Konto mit dieser Kontonummer gefunden.")
        return None

    except ValueError:
        gefundene_konten = []

        for konto in konten:
            if konto.besitzer.lower() == suchbegriff.lower():
                gefundene_konten.append(konto)

        if len(gefundene_konten) == 0:
            print("Kein Konto mit diesem Namen gefunden.")
            return None

        if len(gefundene_konten) == 1:
            return gefundene_konten[0]

        print("Mehrere Konten gefunden:")
        for index, konto in enumerate(gefundene_konten):
            print(f"{index + 1}) {konto.kontonummer} - {konto.besitzer} - {konto.kontostand:.2f} Euro")

        try:
            auswahl = int(input("Welches Konto auswählen? "))
        except ValueError:
            print("Ungültige Auswahl.")
            return None

        if auswahl < 1 or auswahl > len(gefundene_konten):
            print("Ungültige Auswahl.")
            return None

        return gefundene_konten[auswahl - 1]

def konto_untermenue(konto):
    while True:
        konsole_leeren()
        print(f"---Konto: {konto.kontonummer}---")

        print("1) Kontodaten anzeigen")
        print("2) Geld einzahlen")
        print("3) Geld auszahlen")
        print("4) Zinsen berechnen")
        print("5) Zurück")

        try:
            unterauswahl = int(input("Auswahl: "))
        except ValueError:
            print("Bitte eine Zahl (Menüpunkt) eingeben.")
            input("Weiter mit Enter...")
            continue

        konsole_leeren()

        if unterauswahl == 1:
            konto.anzeigen()
            input("Weiter mit Enter...")
        elif unterauswahl == 2:
            print(f"Kontostand: {konto.kontostand:.2f} Euro")
            betrag = zahl_einlesen("Welchen Betrag möchten Sie einzahlen?: ")
            konto.einzahlen(betrag)
            print(f"Neuer Kontostand: {konto.kontostand:.2f} Euro")
            input("Weiter mit Enter...")

        elif unterauswahl == 3:
            print(f"Kontostand: {konto.kontostand:.2f} Euro")
            betrag = zahl_einlesen("Welchen Betrag möchten Sie auszahlen?: ")
            konto.auszahlen(betrag)
            print(f"Neuer Kontostand: {konto.kontostand:.2f} Euro")
            input("Weiter mit Enter...")
            
        elif unterauswahl == 4:
            print(f"Kontostand: {konto.kontostand:.2f} Euro")
            zinssatz = zahl_einlesen("Wie hoch ist der Zinssatz in Prozent?: ")
            konto.zinsen_hinzufuegen(zinssatz)
            print(f"Neuer Kontostand: {konto.kontostand:.2f} Euro")
            input("Weiter mit Enter...")

        elif unterauswahl == 5:
            break
        
        else:
            print("Ungültige Auswahl.")
            input("Weiter mit Enter...")

def zahl_einlesen(text):
    while True:
        try:
            zahl = float(input(text).replace(",","."))
        except ValueError:
            print("Bitte einen gültigen Betrag eingeben.")
            continue
        return zahl

# Hauptprogramm
while True:
    konsole_leeren()
    print("1) Konto anlegen")
    print("2) Konto anzeigen")
    print("3) Beenden")
    
    try:
        hauptauswahl = int(input("Auswahl: "))
    except ValueError:
        print("Bitte eine Zahl (Menüpunkt) eingeben.")
        input("Weiter mit Enter...")
        continue
    
    konsole_leeren()

    if hauptauswahl == 1:
        print("---Konto Anlegen---")
        konto = konto_anlegen()
        if konto is not None:
            konten.append(konto)
            print("Konto wurde gespeichert.")
        else:
            print("Konto wurde verworfen.")
        input("Weiter mit Enter...")

    elif hauptauswahl == 2:
        konto = konto_suchen(konten)
        if konto is not None:
            konto_untermenue(konto)
        else:
            input("Weiter mit Enter...")

    elif hauptauswahl == 3:
        break

    else:
        print("Ungültige Auswahl.")
        input("Weiter mit Enter...")
        continue