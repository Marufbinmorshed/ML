# Employee promotion system
employees = {
    "Rahim": {"years": 5, "rating": 4.5},
    "Karim": {"years": 2, "rating": 3.8},
    "Ayesha": {"years": 6, "rating": 4.9}
}

for name, info in employees.items():
    if info["years"] >= 5 and info["rating"] >= 4:
        print(name, "Eligible for Promotion")
    else:
        print(name, "Not Eligible")
