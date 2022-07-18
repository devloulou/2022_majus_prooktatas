# OOP - Object Oriented Programming
# a zárójelkben tudunk megadni bizonyos dolgot, ami opcionális

class ClassName:
    pass

# vagy valamilyen viselekedést akarsz lefejleszteni
# vagy kifejezetten valamilyen adattal kapcsolatos megközelítést

class Animal:
    # constructor
    def __init__():
        pass


def add_numbers(a, b):
    return a + b

temp = add_numbers(1, 2)



class Animal:
    # constructor
    def __init__(self, name):
        self.name = name
    
    def make_sound(self, param1):
        print(f'{self.name} - Csiripcsirip - {param1}')




# objektum példányosítás

my_list = []
my_list.append('alma')

tyuk = Animal('Frici')
tyuk2 = Animal('Frici2')

#tyuk.make_sound('Hangosan')

# abstraction  - elrejted az implementálás logikáját mindentől, ami az osztályon kívül van
class NetBank:
    def __init__(self):
        self.password = None
        self.iban = None
        self.money = 2400
        self.partners = []

        self.pay_bills()

    def send_money(self, money):
        if money > self.money:
            raise Exception(f'Nincs fedezeted! - {self.money}')

        self.money -= money

    def pay_bills(self):
        self.money -= 1200
        self.money -= 100
        self.money -= 400

    def create_partner_list(self, partner):
        self.partners.append(partner)

netbank = NetBank()

netbank.send_money(10)

#print(netbank.money)

netbank.create_partner_list('jocó')

#print(netbank.partners)


# inheritance  - öröklődés
# olyan mechanizmus, amellyel gyermek objektumot tudunk létrehozni úgy,
# hogy a gyermek örökölni fogja a szülő objektum minden viselkedését és attribútumát

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def run(self):
        print('running')


class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)

    def make_sound(self):
        print("vau vau")

    def run(self):
        print(f"{self.name} is running")

kutya = Dog('Floki', 'keverék')

print(kutya.name)
print(kutya.type)

kutya.run()

kutya.make_sound()

kutya.name = 'Ubul'

kutya.run()


# encapsulation - egységbe zárás
# az összes állapot, változó és metódus privátként tartásának a módja
# hacsak nem nyilvánosnak akarjuk használni azokat

# setter, getter, deleter

# public, private, protected

class NetBank:
    def __init__(self):
        self.__money = 100

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money += money


netbank = NetBank()

#netbank.set_money(10)

#print(netbank.get_money())

print(netbank._NetBank__money)

netbank._NetBank__money = 110

print(netbank.get_money())


netbank.owner = "Ricsi"

print(netbank.owner)


# polimorfizmus - többalakúság

# len()

print(len('alma'))

print(len(['asddfa', "saf"]))


class India:
    def capital(self):
        print("New Delhi")
    
    def language(self):
        print("Hindi")

    def type(self):
        print("Developing")

class USA:
    def capital(self):
        print("Washington")
    
    def language(self):
        print("English")

    def type(self):
        print("Developed")


india = India()
usa = USA()

for country in (india, usa):
    country.capital()
    country.language()
    country.type()