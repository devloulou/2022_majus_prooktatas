# Össze tett adattípusok
my_str = ""
my_str = str()

# 1. List - lista
# A lista az egy mutable adattípus - megváltoztatható
# lista műveletek:

# elemet hozzáadni
# elemet törölni
# elemet módosítani
# össze lehet vonni listákat
# elérni az elemet

my_list = []
my_list = list()

my_list = [1, "Ricsi", print, "Ricsi", [1, 2, 3], None]

my_list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(my_list2[0::2])
# print(my_list2[-1])
# print(my_list2[::-1])

my_list2[0] = my_list2[0] * 5
my_list2[-1] = "Jocó"

my_list2[0:4] = 10, 11, 12, 'Ági', 'Ricsi'
#my_list2[0:4] = [10, 11, 12, 'Ági', 'Ricsi']

#print(my_list2)

########################################################

my_list = []

# append: 1 érték hozzáadása a listához

my_list.append("Juci")

# extend: több érték hozzáadása a listához

my_list.extend(["Karcsi", "Pista", 'Jolán'])

# insert: egy adott index elé betenni adatot
my_list.insert(-1, 30)

#print(my_list)

my_list = [1, 8, 3, 5, 8, 11, 19]

# érték alapján törölni
my_list.remove(8)



# index alapján törölni

my_list.pop(1)

# del

del my_list[0]


#print(my_list)


# lista mint referencia

# referencia hivatkozás
######################################################


a = 10
b = a

a = 20
b = 15

# print(a)
# print(b)

# referencia hivatkozás listák esetében

my_list = [1, 2, 3, 4]
my_list2 = my_list

my_list[0] = "Ricsi"
my_list2[-1] = 100

my_list.append(50)
my_list2.append(302)

#print(my_list)

#######################################

my_list = [1, 2, 3, 4, [5, 6, ["Ricsi", "Joci"]]]

my_list[4][2].append(10)
#print(my_list)

########################################

my_list = [1, 2, 3, [4, 5]]

my_list2 = my_list

my_list[2] = "10"

my_list[-1][0] = "Ricsi"

#print(my_list2)

#########################################

# listák összevonása

my_list = [10, 20, 30]
my_list2 = [30, 40, 50, 60]

my_list3 = my_list + my_list2

my_list2[-1] = "Ricsi"

# print(id(my_list))
# print(id(my_list2))
# print(id(my_list3))

# print(my_list3)

############################

my_list = [10, 20, 30]
my_list2 = [30, 40, 50, 60]

my_list3 = []

my_list3.extend(my_list)
my_list3.extend(my_list2)

#print(my_list3)


#####################################

my_list = [10, 20, 30]
my_list2 = [30, 40, 50, 60]

# unpacking 
my_list3 = [*my_list, *my_list2]

#print(my_list3)

#####################################

# tuple - 
# immutable - megváltoztathatatlan

# mikor jó a tuple: ha nem akarok az adaton változtatni
# adatbázis műveletek

my_tuple = (10, 20, 30, 40)
my_tuple = tuple((10, 20, 30, 40))

my_list = list(my_tuple)

my_list[-1] = 50

my_tuple = tuple(my_list)

#print(my_tuple[::-1])

#########################################################

my_list = [1, 2, 3, ["Ricsi", "Karcsi"]]

my_list2 = []

my_list2.extend(my_list)

#print(id(my_list))

# print(id(my_list[0]))
# print(id(my_list[1]))

# print(id(my_list2[0]))
# print(id(my_list2[1]))

my_list[0] = "Laci"
my_list[3][0] = "Peti"
#print(id(my_list2))

# print(my_list)
# print(my_list2)
##############################################################################################

# dictionary: kulcs - érték párok
# mutable object - megváltoztatható

# kulcs az egyedi értéknek kell hogy legyen

my_dict = {}
my_dict = dict()


my_dict = {"kulcs": "érték"}

my_dict = {
    "name": "Ricsi",
    "age": 32,
    "profession": "developer"
    }


my_dict = {
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}


my_dict = {
    "name": "Ricsi",
    "age": 32,
    "profession": "developer"
    }

# 

print(my_dict["name"])
#print(my_dict["age"])
#print(my_dict["profession"])

my_dict["name"] = "Elon"

my_dict['new_key'] = "new_value"

my_dict.update({"eyecolor": "brown"})

#print(my_dict)


#################################################

my_dict = {
    "name": "Ricsi",
    "age": 32,
    "profession": "developer"
    }

# my_dict.pop('age')
# my_dict.popitem()



del my_dict['name']

#print(my_dict)

##########################################################

my_dict = {
	"id": "0001",
	"type": "donut",
	"name": "Cake",
	"ppu": 0.55,
	"batters":
		{
			"batter":
				[
					{ "id": "1001", "type": "Regular" },
					{ "id": "1002", "type": "Chocolate" },
					{ "id": "1003", "type": "Blueberry" },
					{ "id": "1004", "type": "Devil's Food" }
				]
		},
	"topping":
		[
			{ "id": "5001", "type": "None" },
			{ "id": "5002", "type": "Glazed" },
			{ "id": "5005", "type": "Sugar" },
			{ "id": "5007", "type": "Powdered Sugar" },
			{ "id": "5006", "type": "Chocolate with Sprinkles" },
			{ "id": "5003", "type": "Chocolate" },
			{ "id": "5004", "type": "Maple" }
		]
}
my_dict['batters']['batter'][0]['type'] = 'banana'
print(my_dict['batters']['batter'][0])

print(my_dict.keys())

print(my_dict['batters']['batter'][0].keys())

##########################################################################

#set - duplikáció mentes

my_set = {10, 20, 30}

my_set = set({10, 20, 30})


my_set.add(100)

my_list = [1,1,1,1,1,1,2,2,2,3,3,3]

print(set(my_list))

#################################################################

# if else
# ciklusok

# comprehension műveletek

# függvények

my_list = []


print(help(my_list))