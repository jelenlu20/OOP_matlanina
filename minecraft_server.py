
class Hrac:
    """
    hráč minecraftu - udaje o hráči
    """

    def __init__(self, _nickname, _verze_hry):
        self.nick = _nickname,
        self.verzeH = _verze_hry

    @property
    def vypis_nick (self):
        return self.nick

    @vypis_nick.getter
    def vypis_nick (self):
        return self.nick
    # -------------------------
    @property
    def vypis_verze(self):
        return self.verzeH

    @vypis_verze.getter
    def vypis_verze(self):
        return self.verzeH



class Inventar:
    """
    hráčův inventář/data hráče
    """

    def __init__(self, _pocet_zivotu):
        self.zivoty = _pocet_zivotu,
        self.itemy = [],
        self.brneni = []

    @property
    def pridat_item (self):
        return itemy

    @pridat_item.setter
    def pridat_item (self, novy_item):
        pass
    # -------------------------
    @property
    def odebrat_item(self):
        return itemy

    @odebrat_item.setter
    def odebrat_item(self, zahozeny_item):
        pass


class Item:
    """
    itemy
    """

    def __init__(self, _nazev, _typ, _durabilita):
        self.nazev = _nazev,
        self.typ = _typ,
        self.durabilita = _durabilita



class Server:
    """
    minecraft server
    """

    def __init__(self):
        self.nazev = "ZdendaCraft",
        self.__IP = "play.zdenda-craft.cz",
        self.hraci_online = [],
        self.max_hracu = 10

    @property
    def IP_servru(self):
        return self.__IP

    @IP_servru.getter
    def IP_servru(self):
        return self.__IP
    # -------------------------
    @property
    def pripojit_hrace(self):
        return nickname

    @pripojit_hrace.setter
    def pripojit_hrace(self, nickname, max_hracu):
        if len(hraci_online) < self.max_hracu:
            hraci_online.insert(len(hraci_online), nickname)



class Svet:
    """
    svět na servru
    """

    def __init__(self, _nazev, _typ_hry, _verze_sveta):
        self.nazev = _nazev,
        self.typ_hry = _typ_hry,
        self.verzeS = _verze_sveta

# --------------------------------------------------

h1 = Hrac("Zdenda", "1.18")

h2 = Hrac("Ludek123", "1.18")

h3 = Hrac("Plechac73", "1.15")


s = Server()
s.pripojit_hrace(h1.vypis_nick)
print(s.pripojit_hrace)