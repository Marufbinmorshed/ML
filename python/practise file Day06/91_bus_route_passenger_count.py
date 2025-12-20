# Bus route passenger count
routes = {
    "RouteA": [30, 35, 40],
    "RouteB": [25, 20, 30]
}

for route, counts in routes.items():
    total = 0
    for c in counts:
        total += c
    print(route, "Total Passengers:", total)
