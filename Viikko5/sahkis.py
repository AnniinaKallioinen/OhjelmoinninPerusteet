# Copyright (c) 2025 Anniina Kallioinen
# License: MIT

from datetime import datetime, date, time

def muunna_tiedot(kulutus_tuotanto_2: list) -> list:
    """Muuttaa tietorivien tietotyypit oikeiksi"""
    muutettu_tietorivi = []
    muutettu_tietorivi.append(datetime.fromisoformat(kulutus_tuotanto_2[0]))
    muutettu_tietorivi.append(int(kulutus_tuotanto_2[1]))
    muutettu_tietorivi.append(int(kulutus_tuotanto_2[2]))
    muutettu_tietorivi.append(int(kulutus_tuotanto_2[3]))
    muutettu_tietorivi.append(int(kulutus_tuotanto_2[4]))
    muutettu_tietorivi.append(int(kulutus_tuotanto_2[5]))
    muutettu_tietorivi.append(int(kulutus_tuotanto_2[6]))
    return muutettu_tietorivi

def lue_data(tiedoston_nimi: str) -> list:
    """Lukee tiedoston "viikko42.csv" ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä."""
    kulutus_tuotanto_tiedot = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for kulutus_tuotanto in f:
            kulutus_tuotanto = kulutus_tuotanto.strip()
            kulutus_tuotanto_sarake = kulutus_tuotanto.split(';')
            kulutus_tuotanto_tiedot.append(muunna_tiedot(kulutus_tuotanto_sarake))

    return kulutus_tuotanto_tiedot

def paivantiedot(paiva: str, lukemat: list) -> int:
    pv = int(paiva.split('.')[0])
    kk = int(paiva.split('.')[1])
    vuosi = int(paiva.split('.')[2])
    lasketut_tiedot = []
    kulutus1vaihe = 0
    kulutus2vaihe = 0
    kulutus3vaihe = 0
    tuotanto1vaihe = 0
    tuotanto2vaihe = 0
    tuotanto3vaihe = 0
    for lukema in lukemat:
        if lukema[0].date() == date(vuosi, kk, pv):
            kulutus1vaihe += lukema[1]
            kulutus2vaihe += lukema[2]
            kulutus3vaihe += lukema[3]
            tuotanto1vaihe += lukema[4]
            tuotanto2vaihe += lukema[5]
            tuotanto3vaihe += lukema[6]
    
    lasketut_tiedot.append(kulutus1vaihe/1000)
    lasketut_tiedot.append(kulutus2vaihe/1000)
    lasketut_tiedot.append(kulutus3vaihe/1000)
    lasketut_tiedot.append(tuotanto1vaihe/1000)
    lasketut_tiedot.append(tuotanto2vaihe/1000)
    lasketut_tiedot.append(tuotanto3vaihe/1000)
    return lasketut_tiedot


def main():
    """Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""
    lukemat = lue_data("viikko42.csv")
    print("Viikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)", end="\n\n")
    print("Päivä         Pvm         Kulutus [kWh]                 Tuotanto [kWh]")
    print("             (pv.kk.vvvv)  v1      v2      v3            v1     v2     v3")
    print("---------------------------------------------------------------------------")
    maanantainlukemat = paivantiedot("13.10.2025", lukemat)
    print(f"Maanantai     13.10.2025   ", f"{maanantainlukemat[0]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[1]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[2]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[3]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[4]:.2f}".replace('.', ','), end= "\t")
    print(f"{maanantainlukemat[5]:.2f}".replace('.', ','))



if __name__ == "__main__":
    main()