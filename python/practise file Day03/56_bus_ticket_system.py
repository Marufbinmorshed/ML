# Bus ticket booking simulation
seats = [0] * 10
bookings = [1, 3, 5, 3, 7]

for seat in bookings:
    if seats[seat] == 0:
        seats[seat] = 1
        print("Seat", seat, "booked")
    else:
        print("Seat", seat, "already booked")

print("Final seats:", seats)
