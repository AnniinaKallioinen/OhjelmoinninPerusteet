# Copyright (c) 2025 Anniina Kallioinen
# License: MIT

from datetime import datetime, date, time


def muunna_tiedot(tietue: list) -> list:

    """ Muuttaa jokaisen tietorivin tietotyypit oikeaan muotoon
         -> palauttaa listan muutetuilla tietotyypeillä """

    return [
        datetime.fromisoformat(tietue[0]),
        float(tietue[1].replace(",", ".")),
        float(tietue[2].replace(",", ".")),
        float(tietue[3].replace(",", ".")),
    ]

def lue_data(tiedoston_nimi: str) -> list:

    """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa"""

    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta

def printtaa_raportti(raportti: str):

    """ Generoi raportin pyydettyjen tietojen perusteella """
    
    with open("rapsa.txt", "w", encoding="utf-8") as f:
        f.write(raportti)

def raportti_aikavali(alkupaiva: str, loppupaiva: str, tietokanta: list) ->list:

    """ Luo raportin halutulta aikaväliltä """

    alkupv = int(alkupaiva.split(".")[0])
    alkukk = int(alkupaiva.split(".")[1])
    alkuvv = int(alkupaiva.split(".")[2])
    alku = date(alkuvv, alkukk, alkupv)
    loppupv = int(loppupaiva.split(".")[0])
    loppukk = int(loppupaiva.split(".")[1])
    loppuvv = int(loppupaiva.split(".")[2])
    loppu = date(loppuvv, loppukk, loppupv)
    
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0

    for tietue in tietokanta:
        if alku <= tietue[0].date() <= loppu:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1

    raportti = "---------------------------------------------------------\n"
    raportti += f"Raportti aikaväliltä {alkupaiva}-{loppupaiva}\n"
    raportti += f"- kokonaiskulutus: {kulutus:.2f} kWh\n".replace(".", ",")
    raportti += f"- kokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".", ",")
    raportti += f"- keskilämpötila: {lampotila/tietue_lkm:.2f} °C\n".replace(".", ",")
    raportti += "---------------------------------------------------------\n"
    return raportti

def raportti_kk(kuukausi: str, tietokanta: list) -> str:

    """ Luo raportin halutulta kuukaudelta """

    kuukaudet = [
        "Tammikuu",
        "Helmikuu",
        "Maaliskuu",
        "Huhtikuu",
        "Toukokuu",
        "Kesäkuu",
        "Heinäkuu",
        "Elokuu",
        "Syyskuu",
        "Lokakuu",
        "Marraskuu",
        "Joulukuu",
    ]

    kk = int(kuukausi)
    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        if tietue[0].date().month == kk:
            kulutus += tietue[1]
            tuotanto += tietue[2]
            lampotila += tietue[3]
            tietue_lkm += 1

    raportti = "---------------------------------------------------------\n"
    raportti += f"~ Raportti kuukaudelta: {kuukaudet[kk-1]} ~\n"
    raportti += f"- kokonaiskulutus: {kulutus:.2f} kWh\n".replace(".", ",")
    raportti += f"- kokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".", ",")
    raportti += f"- keskilämpötila: {lampotila/tietue_lkm:.2f} °C\n".replace(".", ",")
    raportti += "---------------------------------------------------------\n"
    return raportti

def raportti_v(tietokanta: list) -> str:

    """ Luo yhteenvetoraportin koko vuodelta """

    kulutus = 0
    tuotanto = 0
    lampotila = 0
    tietue_lkm = 0
    for tietue in tietokanta:
        kulutus += tietue[1]
        tuotanto += tietue[2]
        lampotila += tietue[3]
        tietue_lkm += 1

    raportti = "---------------------------------------------------------\n"
    raportti += f"~ Yhteenvetoraportti vuodelta 2025 ~\n"
    raportti += f"- kokonaiskulutus: {kulutus:.2f} kWh\n".replace(".", ",")
    raportti += f"- kokonaistuotanto: {tuotanto:.2f} kWh\n".replace(".", ",")
    raportti += f"- keskilämpötila: {lampotila/tietue_lkm:.2f} °C\n".replace(".", ",")
    raportti += "---------------------------------------------------------\n"
    return raportti

def main():

    """Ohjelman pääfunktio: lukee datan, näyttää valikot ja ohjaa raporttien luomista"""
    
    kulut_tuot_25 = lue_data("2025.csv")

    while True:
        print("Valitse raporttityyppi:")
        print("1) Päiväkohtainen yhteenveto aikaväliltä")
        print("2) Kuukausikohtainen yhteenveto yhdeltä kuukaudelta")
        print("3) Vuoden 2025 kokonaisyhteenveto")
        print("4) Ohjelman lopetus")
        ensimmainen_valinta = int(input("Anna valinta (numero 1-4): "))
        if ensimmainen_valinta == 1:
            alkupaiva = input("Anna alkupäivä (pv.kk.vvvv): ")
            loppupaiva = input("Anna loppupäivä (pv.kk.vvvv): ")
            raportti = raportti_aikavali(alkupaiva, loppupaiva, kulut_tuot_25)
            print(raportti)
        elif ensimmainen_valinta == 2:
            kuukausi = input("Anna kuukauden numero (1–12): ")
            raportti = raportti_kk(kuukausi, kulut_tuot_25)
            print(raportti)
        elif ensimmainen_valinta == 3:
            raportti = raportti_v(kulut_tuot_25)
            print(raportti)
        elif ensimmainen_valinta == 4:
            print("Lopetetaan ohjelma.")
            break
        else:
            continue

        print("Mitä haluat tehdä seuraavaksi?")
        print("1) Kirjoita raportti tiedostoon rapsa.txt")
        print("2) Luo uusi raportti")
        print("3) Lopeta")
        toinen_valinta = int(input("Anna valinta (numero 1-3): "))
        if toinen_valinta == 1:
            printtaa_raportti(raportti)
            print("Raportti printattu tiedostoon.")
        elif toinen_valinta == 2:
            continue
        elif toinen_valinta == 3:
            print("Lopetetaan ohjelma.")
            break
        else:
            continue

        print("---------------------------------------------------------")

if __name__ == "__main__":
    main()