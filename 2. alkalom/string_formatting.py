# string formázás

my_string = "Ricsi"
my_age = 32

# Ricsi vagyok és 32 éves
# string concatenáció

answer = my_string + " vagyok " + str(my_age) + " éves"

#print(answer)

# string formázás

# 1. "régi" string formázás: %

my_num = 5123152436212

# hexadecimális értékét kiíratni
#függvényhivással
#print(hex(my_num))

my_hex_val = "my_num hex value: %x" % my_num 

#print(my_hex_val)

# Ricsi vagyok és 32 éves
my_string = "Ricsi"
my_age = 32

answer = " %s vagyok és %x éves" % (my_string, my_age)

answer = " %(name)s vagyok és %(age)i éves" % {'name': my_string, 'age': my_age}

#print(answer)

# 2. "New Style" string fromatting: str.format()
my_string = "Ricsi"
my_age = 32

answer = "{name} vagyok és {age} éves".format(name=my_string, age=my_age)

# print(answer)

# 3. String interpoláció - f-string

my_string = "Ricsi"
my_age = 32

answer = f"{my_string} vagyok és {my_age} éves"

#print(answer)

from string import Template

my_template = Template('$name vagyok és $age éves')

#print(my_template.substitute(name=my_string, age=my_age))

######################################################################