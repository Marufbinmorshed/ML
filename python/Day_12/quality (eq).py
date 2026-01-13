class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __eq__(self, other):
        return self.user_id == other.user_id

u1 = User(1)
u2 = User(1)

print(u1 == u2)  
