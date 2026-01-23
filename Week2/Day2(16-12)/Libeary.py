import random

low = 1
hight = 100
guesses = 0

options = ("rock", "paper", "scissors")
card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# num = random.randint(low, hight)
num = random.random()
random.shuffle(card)

print(num)
print(card)

option = random.choice(options)

print(options)
