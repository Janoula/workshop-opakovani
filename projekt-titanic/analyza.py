# Titanic – ANALÝZA
#
# Sem piš funkce, které něco spočítají a výsledek vrátí (return).
# Nepatří sem žádný input() ani print(), ty piš do zprava.py.
# Díky tomu půjdou funkce z tohohle datau testovat.
#
# Začni krokem 1: cviceni/01_nacteni.md

import csv
from pathlib import Path

# Složka, ve které leží tenhle soubor, a cesta k datům v ní.
# Díky tomu program data najde, ať ho spouštíš odkudkoliv.

SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"

def nacti_pasazery(data):
    with open(data, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def pocet_pasazeru(data):
    pasazeri = analyza.nacti_pasazery(data)
    return len(pasazeri)

def kazdy_pasazer_ma_dvanact_sloupcu(data):
    pasazeri = analyza.nacti_pasazery(data)
    return len(pasazeri[0])

def jmeno_prvniho_pasazera(data):
    pasazeri = analyza.nacti_pasazery(data)
    return pasazeri[0]["Name"]

def cislo_nebo_nic(text):
    if text == "":
        text = None
        return None
    else:
        text = float(text)
        return text
    

def uprav_pasazera(radek):
    pasazer = radek.copy()
    pasazer["Survived"] = round(int(radek["Survived"]))
    pasazer["Pclass"] = round(int(radek["Pclass"]))
    pasazer["SibSp"] = round(int(radek["SibSp"]))
    pasazer["Parch"] = round(int(radek["Parch"]))
    pasazer["Fare"] = float(radek["Fare"])
    pasazer["Age"] = cislo_nebo_nic(radek["Age"])
    return pasazer

def uprav_pasazery(pasazeri):
    upraveni_pasazeri = []
    for pasazer in pasazeri:
        novy = uprav_pasazera(pasazer)
        upraveni_pasazeri.append(novy)
    return upraveni_pasazeri

def seznam_bez_veku(cisty_seznam):
    seznam_bez_veku = []
    for p in uprav_pasazery(cisty_seznam):
        if p["Age"] == None:
            seznam_bez_veku.append(p)


