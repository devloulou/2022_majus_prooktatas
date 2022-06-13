# minden pythonban írt kódfile egyben modul is
# ezeket tetszés szerint be lehet hivatkozni egy másik file-ban
# mert a "modulban" lefejelsztett megoldást tudjuk használni más helyen is
# emiatt teljesül részben a DRY elv - Don't repeat yourself
# a modulok fejlesztését moduláris fejlesztésnek nevezzük

# Előnyei:
# el tudjuk kerülni a redundanciát - kód duplikációnak
# könyebben struktúrálható, olvasható kódot tudunk így írni ( :D )
# ha valamit tömegesen kell változtatni, akkor könyebben végig tudjuk vezetni a változást

# Hátránya
# a végletekig túl lehet gondolni a struktúrálást -> nagyon szét lehet bontani a kódót
# over engineering
a = 10

def my_func():
    print(f"hello: {__name__}")

print(__file__)
print(__name__)


if __name__ == '__main__':
    print("most futok, mert engem hívnak")
else:
    print(f"most_futok, mert más hív: {__name__}")