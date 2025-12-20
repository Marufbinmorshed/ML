# Employee yearly performance
performance = {
    "Rahim": [4.2, 4.5, 4.7],
    "Karim": [3.8, 4.0, 4.1],
    "Ayesha": [4.8, 4.9, 5.0]
}

for name, scores in performance.items():
    total = 0
    for s in scores:
        total += s
    print(name, "Avg Rating:", total/len(scores))
