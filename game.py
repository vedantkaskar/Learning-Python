import random

secret_number = random.randint(1, 20)

print("Hello! I'm thinking of a number between 1 and 20.")
print("Take a guess.")

while True:
    try:
        user_guess = int(input("Your guess: "))

        if user_guess == secret_number:
            print("Congratulations! You guessed my number!")
            break
        elif user_guess < secret_number:
            print("Your guess is too low. Try again!")
        else:
            print("Your guess is too high. Try again!")
    except ValueError:
        print("That's not a valid number. Please enter a whole number.")

print("Thanks for playing!")
