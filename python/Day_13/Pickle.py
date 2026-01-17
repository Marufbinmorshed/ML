import pickle

class User:
    def __init__(self, name):
        self.name = name

user = User("Maruf")

# Save object
with open("user.pkl", "wb") as f:
    pickle.dump(user, f)

# Load object (ONLY from trusted source)
with open("user.pkl", "rb") as f:
    loaded_user = pickle.load(f)

print(loaded_user.name)
