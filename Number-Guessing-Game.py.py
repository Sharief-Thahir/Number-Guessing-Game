import random

number_to_guess = random.randint(1, 10)

while True:
    guess = input("Guess a number between 1 and 10: ")


    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    
    guess = int(guess)


    if guess == number_to_guess:
        print("Congratulations! You guessed it right!")
        break
    elif guess < number_to_guess:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
