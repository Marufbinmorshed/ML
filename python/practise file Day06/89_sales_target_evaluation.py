# Sales target evaluation
targets = {
    "Rahim": 120000,
    "Karim": 90000,
    "Ayesha": 150000
}

target_limit = 100000
for name, sale in targets.items():
    status = "Achieved" if sale >= target_limit else "Not Achieved"
    print(name, status)
