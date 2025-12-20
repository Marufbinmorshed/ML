# Library fine calculation
days_late = [0, 2, 5, 10]
fines = []

for d in days_late:
    fine = 0
    for day in range(1, d+1):
        fine += 2
    fines.append(fine)

print("Fines:", fines)
