# Student exam attempt limit
attempts = {
    "Rahim": 2,
    "Karim": 4,
    "Ayesha": 1
}

for name, a in attempts.items():
    if a > 3:
        print(name, "Exceeded attempt limit")
