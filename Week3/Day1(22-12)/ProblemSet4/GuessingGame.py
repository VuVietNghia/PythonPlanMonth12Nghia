import random

def guessing_game():
    while True:
        try:
            level: int = int(input("Level: "))
            if level < 1:
                continue
            break
        except ValueError:
            pass
    
    random_number = random.randint(1, level)
    
    while True:
        try:
            guess_number = int(input("Guess: "))
            if guess_number < 1:
                continue
            
            if guess_number > random_number:
                print("Too large!")
            elif guess_number < random_number:
                print("Too small!")
            else:
                print("Just right!")
                break
                
        except ValueError:
            pass

guessing_game()
