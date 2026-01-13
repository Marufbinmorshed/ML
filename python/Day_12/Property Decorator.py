class User:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    @property
    def age(self):
        return 2026 - self.birth_year

u = User(2000)
print(u.age) 
