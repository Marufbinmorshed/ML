# Student ranking
students = {
    "A": 85,
    "B": 92,
    "C": 78,
    "D": 88
}

sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

rank = 1
for name, score in sorted_students:
    print("Rank", rank, ":", name, score)
    rank += 1
