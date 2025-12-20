# Bus schedule simulation
routes = {
    "Route A": ["8:00", "10:00", "12:00"],
    "Route B": ["9:00", "11:00", "13:00"]
}

for route, times in routes.items():
    print(route)
    for t in times:
        print("  Bus at", t)
