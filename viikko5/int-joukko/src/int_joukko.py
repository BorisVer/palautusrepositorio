class IntJoukko:
    OLETUSKAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, alkukapasiteetti=None, kasvatuskoko=None):

        self._kapasiteetti = alkukapasiteetti or self.OLETUSKAPASITEETTI
        self._kasvatuskoko = kasvatuskoko or self.OLETUSKASVATUS
        
        if not isinstance(self._kapasiteetti, int) or self._kapasiteetti < 0:
            raise ValueError("Kapasiteetin täytyy olla positiivinen") # :D
        
        if not isinstance(self._kasvatuskoko, int) or self._kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon täytyy olla positiivinen") # :D
 
        self._luvut = [0] * self._kapasiteetti
        self._alkioiden_lkm = 0
    
    def kuuluu(self, alkio):
        for i in range(self._alkioiden_lkm):
            if self._luvut[i] == alkio:
                return True
        return False

    def lisaa(self, alkio):
        if self.kuuluu(alkio):
            return False
        if self._alkioiden_lkm == len(self._luvut):
            self._kasvata()
        self._luvut[self._alkioiden_lkm] = alkio
        self._alkioiden_lkm += 1
        return True

    def poista(self, alkio):
        for i in range(self._alkioiden_lkm):
            if self._luvut[i] == alkio:
                self._siirra_alkioita(i)
                return True
        return False

    def _siirra_alkioita(self, poisto_indeksi):
        for i in range(poisto_indeksi, self._alkioiden_lkm - 1):
            self._luvut[i] = self._luvut[i + 1]
        
        self._alkioiden_lkm -= 1
        self._luvut[self._alkioiden_lkm] = 0

    def _kasvata(self):
        uusi_kapasiteetti = len(self._luvut) + self._kasvatuskoko
        uudet_luvut = [0] * uusi_kapasiteetti

        for i in range(self._alkioiden_lkm):
            uudet_luvut[i] = self._luvut[i]
        
        self._luvut = uudet_luvut

    def mahtavuus(self): # :D
        return self._alkioiden_lkm

    def to_int_list(self):
        return self._luvut[:self._alkioiden_lkm]

    def yhdiste(joukko_a, joukko_b):
        yhdiste_joukko = IntJoukko()
        for alkio in joukko_a.to_int_list():
            yhdiste_joukko.lisaa(alkio)
        for alkio in joukko_b.to_int_list():
            yhdiste_joukko.lisaa(alkio)
        return yhdiste_joukko

    def leikkaus(joukko_a, joukko_b):
        leikkaus_joukko = IntJoukko()
        for alkio in joukko_a.to_int_list():
            if joukko_b.kuuluu(alkio):
                leikkaus_joukko.lisaa(alkio)
        return leikkaus_joukko

    def erotus(joukko_a, joukko_b):
        erotus_joukko = IntJoukko()
        for alkio in joukko_a.to_int_list():
            if not joukko_b.kuuluu(alkio):
                erotus_joukko.lisaa(alkio)
        return erotus_joukko

    def __str__(self):
        if self._alkioiden_lkm == 0:
            return "{}"
        elif self._alkioiden_lkm == 1:
            return "{" + str(self._luvut[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self._alkioiden_lkm - 1):
                tuotos = tuotos + str(self._luvut[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self._luvut[self._alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos