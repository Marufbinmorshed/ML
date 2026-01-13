class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, level):
        super().__init__(name)
        self.level = level

a = Admin("Maruf", "Super")
print(a.name, a.level)
