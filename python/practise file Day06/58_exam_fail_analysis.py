# Exam fail analysis
marks = {
    "A": 35,
    "B": 55,
    "C": 30
}

for name, m in marks.items():
    if m < 40:
        print(name, "Failed")
