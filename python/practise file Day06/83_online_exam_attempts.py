# Online exam attempts
attempts = {
    "Rahim": 3,
    "Karim": 2,
    "Ayesha": 1
}

for name, cnt in attempts.items():
    if cnt > 2:
        print(name, "Multiple attempts")
    else:
        print(name, "Within limit")
