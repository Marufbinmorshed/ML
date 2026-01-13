class Person:
    species = "Human"   # Class variable

    def __init__(self, name):
        self.name = name  # Instance variable

p1 = Person("A")
p2 = Person("B")

Person.species = "Alien"

print(p1.species)  
print(p2.species)  
