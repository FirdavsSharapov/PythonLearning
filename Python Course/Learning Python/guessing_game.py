import random

def guessing_game():
    guessed_number = random.randint(0,100)
    
    while True:
        input_number = int(input("What is your guess? "))
        if guessed_number < input_number:
            print(f'Your guess of {input_number} is too high!')
        elif input_number > guessed_number:
            print(f'Your guess of {input_number} is too low!')
        else:
            print("You got it!")
            break

guessing_game()