class User:
    def login(self):
        print("User logged in")

class Admin(User):
    def delete_db(self):
        print("Database deleted")

a = Admin()
a.login()
a.delete_db()
