# Hospital patient records
patients = {
    "P001": {"age": 30, "days": 5},
    "P002": {"age": 45, "days": 2},
    "P003": {"age": 60, "days": 10}
}

for pid, info in patients.items():
    bill = info["days"] * 1500
    print(pid, "Hospital Bill:", bill)
