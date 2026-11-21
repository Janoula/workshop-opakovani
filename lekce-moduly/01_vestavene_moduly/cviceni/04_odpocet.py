# Cvičení 4 – Odpočet
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se, od kolika se má odpočítávat. Pak vypisuj čísla
#    dolů až k jedničce, mezi každými dvěma počkej sekundu,
#    a nakonec vypiš „Šťastný nový rok!“.
#    Na čekání použij sleep z modulu time.

import time

start = int(input("Od kolika se má počítat? "))
for i in range(0, start):
    print(start)
    time.sleep(1)
    start = start - 1
    if start == -1:
        break
print("Šťastný nový rok!")
