# Employee leave tracker
leaves = {
    "Rahim": ["CL", "SL"],
    "Karim": ["CL"],
    "Ayesha": ["CL", "SL", "EL"]
}

for emp, leave_list in leaves.items():
    print(emp, "Total Leaves Taken:", len(leave_list))
