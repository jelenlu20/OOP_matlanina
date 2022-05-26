import random



class Karta:
    """
    popis karta
    """
    def __init__(self, _barva, _hodnota):
        self.barva = _barva
        self.hodnota = _hodnota

    def vypis_kartu(self):
        print(f"{self.barva}{self.hodnota}")

    def vrat_kartu(self):
        return [self.barva]

    def vydat_kartu(self):
        return self.__karty  # --- ???



class Balicek:
    def __init__(self):
        self.__karty = []
        self.barvy = ["S", "K", "Z", "P"]
        self.barvy = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

        for barva in barvy:
            for hodnota in hodnoty:
                self.__karty.append(karta(barva, hodnota))
        self.zamichat()

    def zamichat(self):
        random.shuffle(self.__karty)

    def vypis_balicek(self):
        for karta in self.__karty:
            karta.vypis_kartu()

    def vydat_kartu(self):
        return self.__karty.pop()



class Hrac:
    def __init__(self, _jmeno, _penize):
        self.jmeno = _jmeno
        self.penize = 1000
        self.__ruka = []

    def vezmi_kartu(self, karta):
        self.__ruka.append(karta)

    def vypis_karty(self):
        for karta in self.__ruka:
            karta.vypis_kartu()

class Krupier:
    def __init__(self):
        self.__ruka = []

    def lizni(self, pocet, balicek):
        for i in range(pocet):
            self.__ruka.append(balicek.vydat_kartu())

    def rozdej(self, pocet_karet_pro_1_hrace, hrac, balicek):
        for i in range(pocet_karet_pro_1_hrace):
            hrac.vezmi_kartu(balicek.vydat_kartu())

    def vypis_karty(self):
        for karta in self.__ruka:
            print(karta.barva, karta.hodnota, sep="", end=" ")




b1 = Balicek()
#b1.vypis_balicek()
h1 = Hrac("Lukas")
k1 = Krupier()
k1.lizni(2, b1)
k1.rozdej(2, h1, b1)
print("Deeler:", end=" ")
k1.vypis_karty()

print("Hrac:", end=" ")
h1.vypis_karty()