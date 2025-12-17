# Password strength check
passwords = ["abc", "Admin123", "pass@123"]

for pwd in passwords:
    has_digit = False
    has_special = False
    for ch in pwd:
        if ch.isdigit():
            has_digit = True
        if not ch.isalnum():
            has_special = True

    if len(pwd) >= 6 and has_digit and has_special:
        print(pwd, "Strong")
    else:
        print(pwd, "Weak")
