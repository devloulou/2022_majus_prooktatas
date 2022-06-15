# namespace
# scope - láthatóság

import test_modul


# global scope

a = 10

def my_func():
    b = 10

    def other():
        # b = 15
        nonlocal b
        if b >= 10:
            b = 15
        print(b)

    def other2():
        return b**2

    other()
    val = other2()
    print(val)   

my_func()


# file műveletek
# csv
# json
# contextusmanager

# adatbázis dolgait:
# alap adatmodellezés
# SQL alapjai: -> adatot töltsünk be adatbázisba,
# feldolgozzuk és lekérdezzük
# módosíani és törölni tudjuk

# OOP - Object Oriented Programming
