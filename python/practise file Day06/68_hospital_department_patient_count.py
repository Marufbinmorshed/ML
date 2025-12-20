# Hospital department patient count
departments = {
    "Cardiology": ["P1", "P2"],
    "Orthopedic": ["P3"],
    "Neurology": ["P4", "P5", "P6"]
}

for dept, patients in departments.items():
    print(dept, "Patients:", len(patients))
