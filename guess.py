import random

number = random.randint(1, 100)

guess = int(input("I'm thinking of a number between 1 and 100. Can you guess what it is? "))

while guess != number:
    if guess < number:
        print("Nope, try again. The number I'm thinking of is higher than that.")
    else:
        print("Nope, try again. The number I'm thinking of is lower than that.")
    guess = int(input("Guess again: "))

print("Congratulations, you guessed the number! It was", number)
