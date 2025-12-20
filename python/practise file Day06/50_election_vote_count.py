# Election vote counting
votes = {
    "A": 120,
    "B": 150,
    "C": 90
}

winner = None
max_votes = -1
for candidate, v in votes.items():
    if v > max_votes:
        max_votes = v
        winner = candidate

print("Winner:", winner)
