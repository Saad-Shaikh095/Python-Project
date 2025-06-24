import random 

name = input("Enter your name: ")

def roll_dice():
    return random.randint(1, 6)  # Keep dice realistic (1-6)

def dice_game():
    print(f"\nWelcome to {name} vs Computer Dice Rolling Game")                                                                                                                                                   
    user_score = 0
    comp_score = 0

    while user_score < 50 and comp_score < 50:
        input("\nPress Enter to roll the dice... ")

        user_roll = roll_dice()
        comp_roll = roll_dice()

        print(f"You Rolled: {user_roll}")
        print(f"Computer Rolled: {comp_roll}")

        user_score += user_roll
        comp_score += comp_roll

        print(f"Current Scores ---> {name}: {user_score}   | Computer: {comp_score}")

    print("\nGame Over....!!!")
    if user_score >= 50 and comp_score >= 50:
        print("Ohh It's a tie!")
    elif user_score >= 50:
        print(f"You won {name}. Congratulations...!!!")
    else:
        print("You lose.. Please try again.")

dice_game()