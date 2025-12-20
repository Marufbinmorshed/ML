# Filter emails by domain
emails = ["a@gmail.com", "b@yahoo.com", "c@gmail.com"]
gmail_users = []

for mail in emails:
    if mail.endswith("@gmail.com"):
        gmail_users.append(mail)

print("Gmail users:", gmail_users)
