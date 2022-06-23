"""
JSON - Javascript Object Notation

dictionary nek tudjuk megfeleltetni

"""

my_dict = {"kulcs": "érték"}

# object
my_dict = {
    'autosalon': {
        "kulcs": "érték"
    }
}

# array
my_dict = {
    "cars": ["BMW", {}, ()]
}

my_bool = True
my_bool = False

# true
# false


"""
pythonban nem számít hogy ' vagy " aposztróf
a JSON esetében csak a " lehet stringeknél nyitó és záró serparator karakter

pythonban null érték: None
json-ben: null

"""


######################################################################################################

# dump
# dumps
# load 
# loads
import os
import json

my_dict = {
    "cars": {
        "color": "white",
        "motor_type": "benzin"
    }
}

#['cars'][0]['motor_type']
my_dict = {
    "cars": [
        {
            "color": "white",
            "motor_type": "benzin"
        },
        {
            "color": "white",
            "motor_type": "benzin",
            "type": {
                "sedan": {
                    "price": {
                        "loan": 12345677,
                        "cash": 12346246
                    }
                },
                "combi": {
                    "func": True,
                    "func_name": "print"
                }
            }
        },
        {
            "color": "white",
            "motor_type": "benzin",
            "price": {
                "loan": 123450000,
                "cash": 123456756
            }
        },
        {
            "color": "white",
            "motor_type": "benzin",
            "manufacture_date": "1990"
        }
    ]
}
my_dict_temp = "['cars'][0]['motor_type']"
my_data = eval(f"my_dict{my_dict_temp}")

my_data = eval("print('Ricsi')")
# print(my_data)

# with open(os.path.join(os.path.dirname(__file__), "test2.json"), "w", encoding="utf-8") as f:
#     json.dump(my_dict, f, indent=4)


# dumps

"""
amikor python objectből JSON csinálok -> JSON-t serializálok
amikor egy JSON-t "beolvasok" pythonban -> JSON deserializálok

"""


my_json_str = json.dumps(my_dict, indent=4)

# print(my_json_str)

# loads
my_json = json.loads(my_json_str)

# print(type(my_json))
# print(my_json.values())

#load
with open(r"C:\WORK\2022_majus_prooktatas\8. alkalom\test.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
