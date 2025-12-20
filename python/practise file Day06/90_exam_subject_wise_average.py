# Subject-wise average marks
marks = {
    "Math": [80, 85, 90],
    "Physics": [70, 75, 78],
    "Chemistry": [88, 92, 85]
}

for subject, scores in marks.items():
    total = 0
    for s in scores:
        total += s
    print(subject, "Average:", total/len(scores))
