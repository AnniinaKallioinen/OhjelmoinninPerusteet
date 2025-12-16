# Copyright (c) 2025 Anniina Kallioinen
# License: MIT

from datetime import datetime, date, time


def muunna_tiedot(tietue: list) -> list:

    """ Muuttaa jokaisen tietorivin tietotyypit oikeiksi. """

    return [
        datetime.fromisoformat(tietue[0]),
        int(tietue[1]),
        int(tietue[2]),
        int(tietue[3]),
        int(tietue[4]),
        int(tietue[5]),
        int(tietue[6]),
    ]

def lue_data(tiedoston_nimi: str) -> list:

    """ Lukee csv-tiedoston datan ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä. """

    tietokanta = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for tietue in f:
            tietue = tietue.split(";")
            tietokanta.append(muunna_tiedot(tietue))

    return tietokanta

def paivan_tiedot(paiva: date, tietokanta: list) -> list:

    """ Laskee kulutus- ja tuotantotiedot vaiheittain ja palauttaa listan.
        Laskettavat tiedot muutetaan Wh -> kWh """

    kulutus = [0, 0, 0]
    tuotanto = [0, 0, 0]
    for tietue in tietokanta:
        if tietue[0].date() == paiva:
            kulutus[0] += tietue[1] / 1000
            kulutus[1] += tietue[2] / 1000
            kulutus[2] += tietue[3] / 1000
            tuotanto[0] += tietue[4] / 1000
            tuotanto[1] += tietue[5] / 1000
            tuotanto[2] += tietue[6] / 1000

    return [
        f"{paiva.day}.{paiva.month}.{paiva.year}",
        f"{kulutus[0]:.2f}".replace(".", ","),
        f"{kulutus[1]:.2f}".replace(".", ","),
        f"{kulutus[2]:.2f}".replace(".", ","),
        f"{tuotanto[0]:.2f}".replace(".", ","),
        f"{tuotanto[1]:.2f}".replace(".", ","),
        f"{tuotanto[2]:.2f}".replace(".", ","),
    ]

def main():

    """ Ohjelman pääfunktio: lukee datan, laskee yhteenvedot ja tulostaa raportin."""

    kulutus_tuotanto_vko41 = lue_data("viikko41.csv")
    kulutus_tuotanto_vko42 = lue_data("viikko42.csv")
    kulutus_tuotanto_vko43 = lue_data("viikko43.csv")

    """ Viikko 41 """
    viikko41 = "\nViikon 41 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko41 += "Päivä\t\tPvm\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko41 += "\t\t\t(pv.kk.vvvv) v1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko41 += "----------------------------------------------------------------------------\n"
    viikko41 += "maanantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 6), kulutus_tuotanto_vko41)) +"\n"
    viikko41 += "tiistai\t\t" + "\t".join(paivan_tiedot(date(2025, 10, 7), kulutus_tuotanto_vko41)) +"\n"
    viikko41 += "keskiviikko\t" + "\t".join(paivan_tiedot(date(2025, 10, 8), kulutus_tuotanto_vko41)) +"\n"
    viikko41 += "torstai\t\t" + "\t".join(paivan_tiedot(date(2025, 10, 9), kulutus_tuotanto_vko41)) +"\n"
    viikko41 += "perjantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 10), kulutus_tuotanto_vko41)) +"\n"
    viikko41 += "lauantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 11), kulutus_tuotanto_vko41)) +"\n"
    viikko41 += "sunnuntai\t" + "\t".join(paivan_tiedot(date(2025, 10, 12), kulutus_tuotanto_vko41)) +"\n"
    viikko41 += "----------------------------------------------------------------------------\n"

    """ Viikko 42 """
    viikko42 = "\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko42 += "Päivä\t\tPvm\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko42 += "\t\t\t(pv.kk.vvvv) v1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko42 += "----------------------------------------------------------------------------\n"
    viikko42 += "maanantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 13), kulutus_tuotanto_vko42)) +"\n"
    viikko42 += "tiistai\t\t" + "\t".join(paivan_tiedot(date(2025, 10, 14), kulutus_tuotanto_vko42)) +"\n"
    viikko42 += "keskiviikko\t" + "\t".join(paivan_tiedot(date(2025, 10, 15), kulutus_tuotanto_vko42)) +"\n"
    viikko42 += "torstai\t\t" + "\t".join(paivan_tiedot(date(2025, 10, 16), kulutus_tuotanto_vko42)) +"\n"
    viikko42 += "perjantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 17), kulutus_tuotanto_vko42)) +"\n"
    viikko42 += "lauantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 18), kulutus_tuotanto_vko42)) +"\n"
    viikko42 += "sunnuntai\t" + "\t".join(paivan_tiedot(date(2025, 10, 19), kulutus_tuotanto_vko42)) +"\n"
    viikko42 += "----------------------------------------------------------------------------\n"

    """ Viikko 43 """
    viikko43 = "\nViikon 43 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko43 += "Päivä\t\tPvm\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko43 += "\t\t\t(pv.kk.vvvv) v1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko43 += "----------------------------------------------------------------------------\n"
    viikko43 += "maanantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 20), kulutus_tuotanto_vko43)) +"\n"
    viikko43 += "tiistai\t\t" + "\t".join(paivan_tiedot(date(2025, 10, 21), kulutus_tuotanto_vko43)) +"\n"
    viikko43 += "keskiviikko\t" + "\t".join(paivan_tiedot(date(2025, 10, 22), kulutus_tuotanto_vko43)) +"\n"
    viikko43 += "torstai\t\t" + "\t".join(paivan_tiedot(date(2025, 10, 23), kulutus_tuotanto_vko43)) +"\n"
    viikko43 += "perjantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 24), kulutus_tuotanto_vko43)) +"\n"
    viikko43 += "lauantai\t" + "\t".join(paivan_tiedot(date(2025, 10, 25), kulutus_tuotanto_vko43)) +"\n"
    viikko43 += "sunnuntai\t" + "\t".join(paivan_tiedot(date(2025, 10, 26), kulutus_tuotanto_vko43)) +"\n"
    viikko43 += "----------------------------------------------------------------------------\n"

    """ Raportointi yhteenvedosta tiedostoon raportti.txt """

    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(viikko41)
        f.write(viikko42)
        f.write(viikko43)
    
    print("Yhteenveto luotu, katso raportti.txt")

if __name__ == "__main__":
    main()