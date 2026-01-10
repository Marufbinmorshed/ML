USER = "admin"   # change to "guest" to test

def admin_required(func):
    def inner(*args, **kwargs):
        if USER != "admin":
            raise PermissionError("Admin access required")
        return func(*args, **kwargs)
    return inner

@admin_required
def delete_database():
    print("Database deleted!")

delete_database()
