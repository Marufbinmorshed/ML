# Employee training completion
training = {
    "Rahim": [True, True, False],
    "Karim": [True, False],
    "Ayesha": [True, True, True]
}

for emp, status in training.items():
    completed = 0
    for s in status:
        if s:
            completed += 1
    print(emp, "Completed Trainings:", completed)
