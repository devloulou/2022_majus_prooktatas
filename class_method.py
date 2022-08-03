class Human:
    sex = 'man'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        print(f"Hi {self.name}, your age is: {self.age} and your sexual identity: {self.sex}")


David = Human('Dávid', 40)

Petra = Human('Petra', 24)

#Petra.sex = 'woman'

Human.sex = 'natural'
Human.sexualizalas = "azta"

print(David.sex)
print(Petra.sex)


Anna = Human('Dávid', 40)

Anna.sexecske = "azta"

print(Anna.sex)
print(Anna.sexecske)
print(Human.sexualizalas)