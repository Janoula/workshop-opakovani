import csv
import analyza
from pathlib import Path

SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"

radky = analyza.nacti_pasazery(SOUBOR)
print(radky)