# 1. feladat:
# adjatok egy tetszőleges kulcs-érték párt a megadott dictionaryhez.

my_dict = {
    "auto": "BWM"
}

my_dict['kulcs'] = "érték"
my_dict.update({"new_key": "new_value"})

#print(my_dict)
#################################################################################
# 2. feladat:
# a megadott dictionaryben lévő autokhoz 
# adjatok hozzá egy price kulcsot és egy tetszőleges értéket állítsatok be hozzá

my_dict = {
    "auto": [
        {
            "brand": "BMW",
            "color": "white",
            "type": "diesel"
        },
        {
            "brand": "Volvo",
            "color": "yellow",
            "type": "benzin"
        },
        {
            "brand": "Tesla",
            "color": "black",
            "type": "electric"
        }
    ]
}

my_dict['auto'][0].update({"price": 15000})
my_dict['auto'][1].update({"price": 15000})
my_dict['auto'][2].update({"price": 15000})

my_dict['auto'][0]["price"] = 15000
my_dict['auto'][1]["price"] = 15000
my_dict['auto'][2]["price"] = 15000


#print(my_dict)
############################################################################
# 3. feladat
# a megadott litából hozzatok létre egy tuple-t úgy,
# hogy az első elemtől minden 2. elemet tartalmazza

my_list = ["alma", "körte", "banán", "narancs", "dinnye", "barack"]

my_tuple = tuple(my_list[0::2])

#print(my_tuple)

##############################################################
##############################################################

# 4. Nem szeretjük a francia autót, töröljök a renault az autók közül. A többi érték ne változzon.

my_dict = {
            "auto": [{"type": "Volvo",
                     "color": "gold"
                    },
                    {"type": "Audi",
                     "color": "red"
                    },
                    {"type": "Reanult",
                     "color": "White"
                    } ],
            "driver": ["Heikki Kovalainen", "Bruno Senna", "Sebastien Buemi"],
            "licence": False,
            "age": 18
        }

#my_dict['auto'].pop(2)
#del my_dict['auto'][2]

my_dict['auto'] = my_dict['auto'][0:2]

# my_dict['auto'][2].popitem()
# my_dict['auto'][2].popitem()

print(my_dict)

###################################################