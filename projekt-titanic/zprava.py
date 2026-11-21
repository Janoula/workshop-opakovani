# Titanic – ZPRÁVA
#
# Tenhle soubor spouštíš (Run). Volá funkce z analyza.py a vypisuje
# výsledky. Patří sem všechno s print() a input().
#
# Začni krokem 1: cviceni/01_nacteni.md

import csv
import analyza
from pathlib import Path

SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"

radky = analyza.nacti_pasazery(SOUBOR)
print(radky)

pasazeri = analyza.nacti_pasazery(SOUBOR)

print("Titanic")
print(f"Data jsou v souboru {analyza.SOUBOR.name}.")
print(f"Počet pasažérů je {len(pasazeri)}.")
sloupce = list(pasazeri[0])
print(sloupce)
print(f"První pasažér je {pasazeri[0]["Name"]}.")
cisty_seznam = analyza.uprav_pasazery(pasazeri)
pocet_bez_veku = 0

for p in cisty_seznam:
    if p["Age"] == None:
        pocet_bez_veku = pocet_bez_veku + 1
print(f"Pasažérů, kde nemám uveden věk je {pocet_bez_veku}.")