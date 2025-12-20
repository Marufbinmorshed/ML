# Employee training cost
training_cost = {
    "Rahim": [5000, 3000],
    "Karim": [4000],
    "Ayesha": [6000, 2000]
}

for name, costs in training_cost.items():
    print(name, "Training Cost:", sum(costs))
