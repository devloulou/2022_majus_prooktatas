# C#-ban
# String my_string = "valami"

my_string = 'ez egy string'
my_string2 = "ez egy másik string"

# dinamikus tipísusság

a = 10
print(a)
print(type(a))

a = "alma"
print(a)
print(type(a))

print("##########################################")

a = "Ricsi"
b = "Ricsi"
c = "Ricsi"
print(id(a))
print(id(b))
print(id(c))


print("##########################################")
print()
print()
print()
print()
# Stringek
# characterek sorozata
# iterálható objektum - adattípus

my_string = "ez az első stringem"

# slice-ing - szeletelés
# első eleme a stringnek
print(my_string[0])
print(my_string[3])

# az utolsó elem
print(my_string[-1])

# 
# kezdő érték bele tartozik, a végérték viszont nem
# 

print(my_string[6:10])

print(my_string[11:19])

print("##########################################")
print()
print()
print()
print()

my_string = "ez az első stringem"

print(my_string[0:19:4])
print(my_string[::4])

print(my_string[6::2])

print(my_string[11:19:2])

print(my_string[::-1])

print(my_string[-4:-2])


print("##########################################")
print()
print()
print()
print()

my_string = "ez az első stringem"

# ilyet nem lehet
#my_string[0] = "péter"

my_string = "ez az új érték"

# string concatenáció
my_string = my_string + " Ricsi vagyok"

print(my_string)


#mutable - immutable : megváltoztatható és a megváltoztathatatlan
#string immutable adattípus
print("##########################################")
print()
print()
print()

my_num = 1990
my_string = "my_birthday: "

my_str = my_num*my_string

# típus konverzió - type casting
my_str2 = my_string + str(my_num) 

print(my_str2)

birth_date = "1990"

birth_date = int(birth_date)

print(int(birth_date))

print(len(str(birth_date)))


# string formázás
# 4 típusát

# listákat