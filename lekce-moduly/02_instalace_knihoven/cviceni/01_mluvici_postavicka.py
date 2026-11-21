# Cvičení 1 – Mluvící postavička
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se uživatelky, co má postavička říct a která to má být
#    (třeba cow, tux nebo dragon). Pak ji nech promluvit.
#
#    cowsay.draw(text, cowsay.CHARS[jmeno]) nechá mluvit postavičku
#    podle jména. Seznam jmen je v cowsay.char_names. Když jméno
#    v seznamu není, vypiš, ze kterých jde vybírat.

import cowsay

jmeno = input("Kdo to má říct? ")
text = input("Co má říct? ")
if jmeno in cowsay.char_names:
    cowsay.draw(text, cowsay.CHARS[jmeno])
else:
    print(f"Lze vybírat jen z {cowsay.char_names}")



