from validators import email

get_email = input("What's your email address? ").strip()

try:
    if email(get_email):
        print("Valid")
    else:
        print("Invalid")
except ValueError:
    print("Invalid")
    