import string
import secrets

def generate_password(min_length = 14, max_length = 64):
    chars = string.ascii_letters + string.digits + string.punctuation

    length = secrets.choice(range(min_length, max_length))
    print(length)

    password_list = []

    for _ in range(length):
        password_list.append(secrets.choice(chars))
    
    return ''.join(password_list)

print(generate_password(14, 15))