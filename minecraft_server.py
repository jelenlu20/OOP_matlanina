
class Hrac:
    """
    hráč minecraftu
    """

    def __init__(self, _nickname, _verze_hry):
        self.nick = _nickname,
        self.verzeH = _verze_hry



class Inventar:
    """
    hráčův inventář/data hráče
    """

    def __init__(self, _pocet_zivotu, _itemy, _brneni):
        self.zivoty = _pocet_zivotu,
        self.itemy = _itemy,
        self.brneni = _brneni



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

    def __init__(self, _nazev, _IP_adresa, _hraci_online, _max_hracu):
        self.nazev = _nazev,
        self.__IP = _IP_adresa,
        self.hraci_online = _hraci_online,
        self.max_hracu = _hmax_hracu

    @property
    def IP_servru(self):
        return self.__IP

    @IP_servru.getter
    def IP_servru(self):
        return self.__IP



class Svet:
    """
    svět na servru
    """

    def __init__(self, _nazev, _typ_hry, _verze_hry):
        self.nazev = _nazev,
        self.typ_hry = _typ_hry,
        self.verzeS = _verze_hry