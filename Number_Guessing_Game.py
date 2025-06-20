import random 

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game..!! Made by @Saad Shaikh")
print("I have picked a number between 1 to 100.Can you guess it correctly...??")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too Low..!! Try Again.")
    elif guess > number:
        print("Too High..!! Try Again.")
    else:
        print(f"Congratulations..!! You guessed the number {number} correctly in {attempts} attempts.")
        break