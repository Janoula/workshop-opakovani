# Cvičení 1 – Dvě kostky
# Doplň kód pod zadání a soubor spusť (Run).

# Hoď dvěma kostkami (každá má čísla 1 až 6) a vypiš obě čísla
#    i jejich součet. Použij randrange z modulu random.
#    Ukázka výstupu:
#
#    Padlo 3 a 5, dohromady 8.

from random import randrange

hod1 = randrange(1, 7)
hod2 = randrange(1, 7)
print(f"Padlo {hod1} a {hod2}, celkem {hod1 + hod2}.")
