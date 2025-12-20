# Phone book dictionary
phone_book = {"Rahim": "017xxxx", "Karim": "018xxxx"}

phone_book["Ayesha"] = "019xxxx"

for name, number in phone_book.items():
    print(name, "=>", number)
