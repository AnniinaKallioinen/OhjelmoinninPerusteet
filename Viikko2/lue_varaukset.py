"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    from datetime import datetime
    paiva = datetime.strptime(varaus[2], "%Y-%m-%d").date()
    suomalainenPaiva = paiva.strftime("%d.%m.%Y")
    aika = datetime.strptime(varaus[3], "%H:%M").time()
    suomalainenAika = aika.strftime("%H.%M")

    print(varaus.split('|'))
    varausnumero = int(varaus[0])
    varaaja = str(varaus[1])
    päivämäärä = datetime.date(varaus[2])
    aloitusaika = datetime.time(varaus[3])
    tuntimäärä = int(varaus[4])
    tuntihinta = float(varaus[5])
    maksettu = bool(varaus[6])
    varauskohde = str(varaus[7])
    puhelin = int(varaus[8])
    sähköposti = str(varaus[9])


if __name__ == "__main__":
    main()