from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        peli = None
        if vastaus.endswith("a"):
            peli = KPSPelaajaVsPelaaja()
        elif vastaus.endswith("b"):
            peli = KPSTekoaly()
        elif vastaus.endswith("c"):
            peli = KPSParempiTekoaly()

        if peli:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()