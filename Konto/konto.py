# ----------------------------------------------------------------------
#  Titel     : Konto
# ----------------------------------------------------------------------
#  Funktion  : Konstruktor & Methoden
# ----------------------------------------------------------------------
#  Sprache   : Python
#  Datum     : 04.05.26
#  Autor     : O. Linke
# ----------------------------------------------------------------------
# 
# ----------------------------------------------------------------------
class Konto:
    def __init__(self, kontonummer=-1, besitzer="unbekannt", kontostand=0.0):
        self.kontonummer = kontonummer
        self.besitzer = besitzer
        self.kontostand = kontostand

    def einzahlen(self, betrag):
        if not isinstance(betrag, (int, float)):
            print("Der Betrag muss eine Zahl sein!")
            return

        if betrag <= 0:
            print("Der Betrag muss größer als 0 sein")
            return
        
        self.kontostand += betrag

    def auszahlen(self, betrag):
        if not isinstance(betrag, (int, float)):
            print("Der Betrag muss eine Zahl sein!")
            return

        if betrag <= 0:
            print("Der Betrag muss größer als 0 sein")
            return

        if self.kontostand < betrag:
            print("Nicht ausreichend Geld auf dem Konto!")
            return

        self.kontostand -= betrag

    def zinsen_hinzufuegen(self, zinssatz):
        if not isinstance(zinssatz, (int, float)):
            print("Der Zinssatz muss eine Zahl sein!")
            return

        if zinssatz <= 0:
            print("Der Zinssatz muss größer als 0 sein")
            return

        zinsen = self.kontostand * zinssatz / 100
        self.kontostand += zinsen

    def anzeigen(self):
        print(f"Kontonummer: {self.kontonummer}")
        print(f"Besitzer: {self.besitzer}")
        print(f"Kontostand: {self.kontostand:.2f} Euro")
