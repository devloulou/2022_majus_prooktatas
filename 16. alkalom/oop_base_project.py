# ősosztály
class Vehicle:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.color = None

    def set_color(self):
        self.color = "red"
    

class Car(Vehicle):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = 'car'

class MotorBike(Vehicle):
    def __init__(self, name, price):
        super().__init__(name, price)
        self.type = 'motorbike'


class Catalogue:
    def __init__(self):
        self.cars = {}
        self.motorbikes = {}

    def upload_catalogue(self, item):
        if item.type == 'car':
            self.cars[item.name] = item
        else:
            self.motorbikes[item.name] = item

    def delete_from_catalogue(self, item):
        if item.type == 'car':
            self.cars.pop(item.name)
        else:
            self.motorbikes.pop(item.name)    

    # __str__ az példányosított objektum string reprezentációja
    def __str__(self):
        desc = {
            "cars": {},
            "motorbikes": {}
            }
        for k, v in self.cars.items():
            desc['cars'][k] = {'price': v.price}

        for k, v in self.motorbikes.items():
            desc['motorbikes'][k] = {'price': v.price}

        return str(desc)

    def __del__(self):
        print("törölve lett")
        del self

# dependency injection: 
class Salon:
    def __init__(self, catalogue: Catalogue):
        self.money = 30_000_000
        self.catalogue = catalogue

    def transaction_handling(self, price):
        self.money += price


if __name__ == '__main__':
    volvo = Car(name='Volvo S40', price=1_300_000)
    simson = MotorBike(name='Simson', price=50_000)


    catalogue = Catalogue()
    salon = Salon(catalogue)

    salon.catalogue.upload_catalogue(volvo)
    salon.catalogue.upload_catalogue(simson)

    salon.catalogue.delete_from_catalogue(simson)
    salon.transaction_handling(simson.price)

    mercedes = Car(name='SLK Merci', price=10_300_000)

    salon.catalogue.upload_catalogue(mercedes)
    salon.transaction_handling(mercedes.price*-1)

    print(salon.catalogue)
    print(salon.money)


    # cat = Catalogue()

    # a = 10
    # cat.upload_catalogue(volvo)
    # cat.upload_catalogue(simson)

    # print(cat.cars)
    # print(cat.motorbikes)

    # cat.delete_from_catalogue(volvo)

    # print(cat)

    # __func__ típusú függvényeket: double undescore vagy dunderscore metódusoknak nevezünk
    # "magic metódusok"

