# Password attempt limit
password = "python"
attempts = ["java", "c++", "python"]

count = 0
for a in attempts:
    count += 1
    if a == password:
        print("Login successful")
        break
    else:
        print("Wrong password")

if count == len(attempts):
    print("Access denied")
