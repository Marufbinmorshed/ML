# Electricity bill calculation
units_list = [120, 250, 90, 310]

for units in units_list:
    bill = 0
    for u in range(1, units + 1):
        if u <= 100:
            bill += 2
        elif u <= 200:
            bill += 3
        else:
            bill += 5
    print("Units:", units, "Bill:", bill)
