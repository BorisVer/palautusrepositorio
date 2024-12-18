from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly:
    def pelaa(self):
        tuomari = Tuomari()
        tekoaly = TekoalyParannettu(10)

        while True:
            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")

            if not (self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto)):
                break

            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)
            tekoaly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"