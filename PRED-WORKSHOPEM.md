# Před workshopem

Na workshopu chceme hned programovat, ne instalovat. Projdi si proto tenhle
návod doma, nejlépe pár dní předem. Zabere asi dvacet minut. Když se
někde zasekneš, nevadí: napiš nám na Discord, nebo přijď na workshop
o čtvrt hodiny dřív a vyřešíme to spolu.

Budeš potřebovat totéž co na lekcích: VS Code, Python, Git a účet na
GitHubu.

## 1. Fork

Materiály workshopu leží v repozitáři
[pyladiesprague/workshop-opakovani](https://github.com/pyladiesprague/workshop-opakovani).
Uděláš si z něj vlastní kopii stejně jako na první lekci s `materialy`.

1. Přihlas se na GitHub a otevři odkaz výše.
2. Vpravo nahoře klikni na **Fork**.
3. Nic neměň a klikni na **Create fork**. Volba **Copy the main branch
   only** má zůstat zaškrtnutá.

Na GitHubu teď máš repozitář `tvoje-jmeno/workshop-opakovani`. Do něj
budeš během dne ukládat svou práci.

## 2. Clone

Stejně jako u `materialy` klonuješ ve VS Code:

1. Na stránce svého forku klikni na zelené tlačítko **Code** a zkopíruj
   adresu končící na `.git`. Musí v ní být tvoje uživatelské jméno, ne
   `pyladiesprague`.
2. Ve VS Code otevři v levém pruhu panel **Source Control** a klikni na
   **Clone Repository**. Když tam tlačítko není (máš otevřenou jinou
   složku), stiskni **Ctrl+Shift+P** (na macOS **Cmd+Shift+P**), napiš
   `Git: Clone` a potvrď Enterem.
3. Vlož adresu forku a potvrď Enterem.
4. Vyber **Dokumenty** a klikni na **Select as Repository Destination**.
5. Až se VS Code zeptá, jestli repozitář otevřít, klikni na **Open**.

Ve VS Code otevři vždycky celou složku `workshop-opakovani`, ne jen jeden
projekt nebo soubor. Jen tak najde VS Code testy a nastavení.

Když clone nejde, stáhni si materiály jako ZIP: na stránce repozitáře
zelené tlačítko **Code → Download ZIP**, archiv rozbal a složku otevři ve
VS Code. Programovat se dá i tak, jen svou práci nebudeš ukládat na GitHub.
Na workshopu ti s clonem pomůžeme.

## 3. Instalace knihoven

Na workshopu se hodí tři knihovny: pytest na testy, cowsay a pyfiglet na
lekci o modulech. Ve VS Code otevři terminál (**Terminal → New Terminal**)
a napiš:

```text
pip install pytest cowsay pyfiglet
```

Na konci výpisu má být `Successfully installed …`. Když už některou
knihovnu máš, napíše `Requirement already satisfied`, a to je taky
v pořádku.

### Když instalace nejde

| Co se stalo | Co zkusit |
|---|---|
| `pip` není rozpoznaný příkaz (Windows) | `py -m pip install pytest cowsay pyfiglet` |
| `command not found: pip` (macOS) | `python3 -m pip install pytest cowsay pyfiglet` |
| `error: externally-managed-environment` | Nic dalšího nezkoušej a napiš nám. Tvůj Python spravuje jiný program a je potřeba to vyřešit jinak. |
| instalace proběhla, ale program hlásí `ModuleNotFoundError` | VS Code používá jiný Python než terminál. Dole na stavové liště klikni na verzi Pythonu, vyber jinou a instalaci zopakuj. |

Když nepomůže nic z tabulky, zkopíruj si celou chybovou hlášku a pošli nám
ji na Discord.

## 4. Kontrola

1. Ve VS Code otevři panel **Testing** (ikona baňky vlevo).
2. Spusť všechny testy (dvojitá šipka nahoře v panelu).
3. Všechny mají být zelené.

Pak otevři soubor `lekce-moduly/02_instalace_knihoven/01_pip.py` a spusť ho
tlačítkem **Run**. V terminálu má promluvit kráva.

## 5. Ráno v den workshopu

Materiály do poslední chvíle dolaďujeme. Ráno si proto fork aktualizuj
stejně jako u `materialy`:

1. Na GitHubu otevři svůj fork a klikni na **Sync fork → Update branch**.
2. Ve VS Code v panelu **Source Control** klikni u nadpisu *Changes* na
   tři tečky **…** a zvol **Pull**.

## Hotovo, když

- [ ] máš na GitHubu vlastní fork `workshop-opakovani`
- [ ] máš ho naklonovaný a celou složku otevřenou ve VS Code
- [ ] testy v panelu **Testing** jsou zelené
- [ ] kráva promluvila

Víc dělat nemusíš. Lekce i projekty si projdeme spolu na workshopu.
