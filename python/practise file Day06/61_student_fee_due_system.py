# Student fee due system
students = {
    "Rahim": {"paid": 8000, "total": 10000},
    "Karim": {"paid": 6000, "total": 10000},
    "Ayesha": {"paid": 10000, "total": 10000}
}

for name, info in students.items():
    due = info["total"] - info["paid"]
    if due > 0:
        print(name, "Due Amount:", due)
    else:
        print(name, "No Due")
