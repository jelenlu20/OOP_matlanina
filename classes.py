
# !!!  1. pravidlo třídy s VELKÝM PÍSMENEM  !!!

class Person:
    # musí tu být tahle poznámka
    """
    class that represents a person
    """

    def __init__(self, _name, _birth, _email_address):
        self.name = _name
        self.birth = _birth
        self.email_address = _email_address
        self.__address = None

    def getAge(self):
        return 2022 - self.birth

    def purchase_parking_pass(self):
        pass

    def get_address(self):
        return self._address = 
        pass


    def __str__(self):
        return


class Profesor(Person):
    """
    třída profesora
    """
    def __init__(self, _salary, _trida profesora, _name, _birth, _email_address):
        super().__init__(_name, _birth, _email_address)
        self.salary = _salary
        self.trida profesora =  _trida profesora


class Student(Person):
    """
    třída studenta
    """
    def __init__(self):
        pass


class Address:
    """
    sdhdjgmsrz
    """
    def __init__(self):



p1 = Person(
    _name="Peter",
    _birth=2000,
    _email_address="peter@parker.com"
)

print(p1.getAge())





# dekorátor ---------------

class PersonA:

    def __init__(self):
        self.__money = 0
        self.birth = 2006

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, amount):
        if not self.__money + amount < 0:
            self.__money += amount
        else:
            print("Nemáš dostatek peněz")

    # - ???

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(str(new_name)) >=1
            self.__name = new_name

    @name.getter
    def name(self):
        pass