import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Let's see if you can guess it! Be careful, you only have 8 attempts.")

secret_number = random.randint(1, 100)
guess = None
attempts = 0
max_attempts = 8

while guess != secret_number and attempts < max_attempts:
    guess = int(input("Take a guess: "))
    attempts += 1
    if guess > secret_number:
        print("Too High!⬇️")
    elif guess < secret_number:
        print("Too Low!⬆️")
    else:
        print("🎯 BINGO! You got it! Someone's good at this 👀!")
        print(f"You got it in {attempts} attempts!")

if guess != secret_number: #and attempts >= max_attempts:
    print("Game over!")
    print(f"The number was {secret_number}.")
