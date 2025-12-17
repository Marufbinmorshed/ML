# Hotel room booking system
rooms = [0] * 5
requests = [1, 2, 2, 4, 3]

for r in requests:
    if rooms[r-1] == 0:
        rooms[r-1] = 1
        print("Room", r, "Booked")
    else:
        print("Room", r, "Already booked")

print("Room status:", rooms)
