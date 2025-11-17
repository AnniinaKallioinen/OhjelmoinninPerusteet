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
    varaukset = "varaukset.txt"

    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    from datetime import datetime

    varausnro = int(varaus.split('|')[0])
    print("Varausnumero:", varausnro)

    varaajannimi = str(varaus.split('|')[1])
    print("Varaaja:", varaajannimi)

    paivam = datetime.strptime(varaus.split('|')[2], "%Y-%m-%d").date()
    print("Päivämäärä:", paivam.strftime("%d.%m.%Y"))

    aloitusaika = datetime.strptime(varaus.split('|')[3], "%H:%M").time()
    print("Aloitusaika:", aloitusaika.strftime("%H.%M"))

    tuntimaara = int(varaus.split('|')[4])
    print("Tuntimäärä:", tuntimaara)

    tuntihinta = float(varaus.split('|')[5])
    print("Tuntihinta:", tuntihinta, "€")

    kokonaishinta = tuntihinta*tuntimaara
    print("Kokonaishinta:", kokonaishinta, "€")

    maksettu = varaus.split('|')[6]
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")

    varauskohde = str(varaus.split('|')[7])
    print("Kohde:", varauskohde)

    puhelinnumero = str(varaus.split('|')[8])
    print("Puhelin:", puhelinnumero)

    sahkoposti = str(varaus.split('|')[9])
    print("Sähköposti:", sahkoposti)

if __name__ == "__main__":
    main()