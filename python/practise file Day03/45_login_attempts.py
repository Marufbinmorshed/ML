# Login attempt simulation
correct_password = "admin123"
attempts = ["1234", "admin", "admin123"]
count = 0

for pwd in attempts:
    count += 1
    if pwd == correct_password:
        print("Login successful at attempt", count)
        break
    else:
        print("Wrong password")

if count == len(attempts):
    print("Account locked")
