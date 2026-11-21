# Cvičení 3 – Kruh
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na poloměr kruhu a vypiš jeho obvod (2 · pí · r)
#    a obsah (pí · r · r), oba zaokrouhlené na dvě desetinná místa.
#    Tentokrát použij zápis import math a pí z modulu math.

import math

polomer = int(input("Zadej poloměr kruhu: "))
print(f"Obvod je {round(2 * math.pi * polomer, 2)} a obsah {round(math.pi * polomer ** 2, 2)}")
