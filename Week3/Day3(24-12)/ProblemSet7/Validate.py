import re

email = input("Enter your email: ").strip()

if re.search(r"^\S+@\S+\.\S+$", email):
    print("Valid")
else:
    print("Invalid")