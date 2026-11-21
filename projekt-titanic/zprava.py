# Titanic – ZPRÁVA
#
# Tenhle soubor spouštíš (Run). Volá funkce z analyza.py a vypisuje
# výsledky. Patří sem všechno s print() a input().
#
# Začni krokem 1: cviceni/01_nacteni.md

import analyza

pasazeri = analyza.nacti_pasazery(analyza.SOUBOR)

print("Titanic")
print(f"Data jsou v souboru {analyza.SOUBOR.name}.")
print(f"Počet pasažérů je {len(pasazeri)}.")
sloupce = list(pasazeri[0])
print(sloupce)
print(f"První pasažér je {pasazeri[0]["Name"]}.")
