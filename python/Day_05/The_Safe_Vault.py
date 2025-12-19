user = {"id": 1}
email = user.get("email")        
email_default = user.get("email", "Not provided")
print(email)
print(email_default)
