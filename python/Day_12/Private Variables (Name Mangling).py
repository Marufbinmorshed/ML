class User:
    def __init__(self, password):
        self.__password = password

u = User("secret123")
# print(u.__password)  
print(u._User__password)  
