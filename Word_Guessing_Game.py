import random 

def word_guessing_game():
    word_list = ["python", "laptop", "stream", "window", "bottle", "rocket", "planet", "school"]
    secret_word = random.choice(word_list)
    guessed_letters = []
    tries = 7

    print("Welcome to the word  huessing game...!!!")
    print("_ " * len(secret_word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter...!!!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word.lower():
            print("You guessed a letter correctly...!!!")

        else:
            tries -= 1
            print(f"Wrong guess..!! Try again. Tries left: {tries}")

            displayed_word = ""
            for letter in secret_word:
                if letter.lower() in guessed_letters:
                    displayed_word += letter + " "

                else:
                    displayed_word += "_ "

            print("\n" + displayed_word)

            if "_" not in displayed_word:
                print("Congratulations!! You guessed the word correctly...!!!")
                break
    else:
        print(f"Game Over...!! The word.. The word was: {secret_word}")

word_guessing_game()

