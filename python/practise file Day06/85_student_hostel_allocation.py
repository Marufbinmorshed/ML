# Student hostel allocation
hostel = {
    "Room1": ["Rahim", "Karim"],
    "Room2": ["Ayesha"],
    "Room3": []
}

for room, students in hostel.items():
    print(room, "Occupied by", len(students), "students")
