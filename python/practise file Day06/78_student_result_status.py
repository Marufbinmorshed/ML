# Student result status
marks = {
    "Rahim": 45,
    "Karim": 35,
    "Ayesha": 80
}

for name, m in marks.items():
    status = "Pass" if m >= 40 else "Fail"
    print(name, status)
