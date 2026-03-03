import random

target = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")

while True:
    guess = int(input("Enter your guess:"))
    if (guess < target):
            print("Too low! Try again.")
    elif (guess > target):
            print("Too high! Try again.")

    if (guess == target):
            print("Congratulations! You've guessed the number.")
            break
print("__GAME OVER__")