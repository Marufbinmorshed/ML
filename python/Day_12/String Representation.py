class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name='{self.name}')"

u = User("Maruf")
print(u)        # User: Maruf
print(repr(u))  # User(name='Maruf')
