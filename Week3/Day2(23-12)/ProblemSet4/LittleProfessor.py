import random


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Level must be 1, 2, or 3")
        except ValueError:
            print("Invalid input. Please enter a number.")


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def professor():
    level = get_level()
    score = 0
    total_questions = 10

    for question_num in range(total_questions):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        attempts = 0
        max_attempts = 3

        while attempts < max_attempts:
            try:
                user_answer = int(input(f"{x} + {y} = "))

                if user_answer == correct_answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1

                    if attempts == max_attempts:
                        print(f"{x} + {y} = {correct_answer}")

            except ValueError:
                print("EEE")
                attempts += 1

                if attempts == max_attempts:
                    print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {score}")


if __name__ == "__main__":
    professor()
