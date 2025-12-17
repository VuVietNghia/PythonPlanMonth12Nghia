import random

def random_guessing_number():
    low = int(input("Nhap vao so thap: "))
    high = int(input("Nhap vao so cao: "))
    guess = random.randint(low, high)
    guesses = 0

    while True:
        num = int(input("Nhap vao so can doan: "))
        if num > guess:
            print("So doan qua cao")
            guesses += 1
        elif num < guess:
            print("So doan qua nho")
            guesses += 1
        else:
            print("Doan dung")
            guesses += 1
            break

    print(f"So lan doan: {guesses}")

random_guessing_number()
