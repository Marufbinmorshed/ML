class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return Wallet(self.balance + other.balance)

w1 = Wallet(100)
w2 = Wallet(200)

w3 = w1 + w2
print(w3.balance)  
