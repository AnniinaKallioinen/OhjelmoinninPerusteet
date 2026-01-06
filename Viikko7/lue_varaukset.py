# Copyright (c) 2025 Ville Heikkiniemi
#
# This code is licensed under the MIT License.
# You are free to use, modify, and distribute this code,
# provided that the original copyright notice is retained.
#
# See LICENSE file in the project root for full license information.


from datetime import datetime
from typing import List, Dict

def muunna_varaustiedot(varaus_lista: List[str]) -> Dict[str, object]:
    paiva_str = varaus_lista[4].strip()
    aika_str = varaus_lista[5].strip().replace(".", ":")

    paiva = datetime.strptime(paiva_str, "%Y-%m-%d").date()
    aika = datetime.strptime(aika_str, "%H:%M").time()

    vahvistus_str = varaus_lista[8].strip().lower()
    vahvistus = vahvistus_str in {"1", "true", "t", "kyllä", "kylla", "k", "yes", "y"}

    return {
        "id": int(varaus_lista[0]),
        "nimi": varaus_lista[1],
        "mail": varaus_lista[2],
        "tel": varaus_lista[3],  # puhelin merkkijonona
        "paiva": paiva,          # date
        "aika": aika,            # time
        "kesto": float(varaus_lista[6].replace(",", ".")),
        "hinta": float(varaus_lista[7].replace(",", ".")),
        "vahvistus": vahvistus,
        "tila": varaus_lista[9],
        "luotu": datetime.strptime(varaus_lista[10].strip(), "%Y-%m-%d").date()
    }

def hae_varaukset(varaustiedosto: str) -> List[Dict[str, object]]:
    varaukset: List[Dict[str, object]] = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for rivi in f:
            rivi = rivi.strip()
            if not rivi:
                continue
            varaustiedot = rivi.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset: List[Dict[str, object]]) -> None:
    for varaus in varaukset:
        if varaus["vahvistus"]:
            print(
                f"- {varaus['id']}, {varaus['tila']}, "
                f"{varaus['paiva'].strftime('%d.%m.%Y')} klo {varaus['aika'].strftime('%H.%M')}"
            )
    print()

def pitkat_varaukset(varaukset: List[Dict[str, object]]) -> None:
    for varaus in varaukset:
        if float(varaus["kesto"]) >= 3:
            print(
                f"- {varaus['nimi']}, {varaus['paiva'].strftime('%d.%m.%Y')} "
                f"klo {varaus['aika'].strftime('%H.%M')}, kesto {varaus['kesto']} h, {varaus['tila']}"
            )
    print()

def varausten_vahvistusstatus(varaukset: List[Dict[str, object]]) -> None:
    for varaus in varaukset:
        status = "Vahvistettu" if varaus["vahvistus"] else "EI vahvistettu"
        print(f"{varaus['nimi']} → {status}")
    print()

def varausten_lkm(varaukset: List[Dict[str, object]]) -> None:
    vahvistetut = sum(1 for v in varaukset if v["vahvistus"])
    ei_vahvistetut = len(varaukset) - vahvistetut
    print(f"- Vahvistettuja varauksia: {vahvistetut} kpl")
    print(f"- Ei-vahvistettuja varauksia: {ei_vahvistetut} kpl")
    print()

def varausten_kokonaistulot(varaukset: List[Dict[str, object]]) -> None:
    tulot = 0.0
    for v in varaukset:
        if v["vahvistus"]:
            tulot += float(v["kesto"]) * float(v["hinta"])
    print("Vahvistettujen varausten kokonaistulot:", f"{tulot:.2f}".replace('.', ','), "€")
    print()

def main():
    varaukset = hae_varaukset("varaukset.txt")
    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()
