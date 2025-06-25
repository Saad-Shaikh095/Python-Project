# import random

# def play_game():
#     options = ["rock", "paper", "scissors"]
#     print("🎮 Welcome to Rock, Paper, Scissors Game!")

#     user_score = 0
#     comp_score = 0

#     while True:
#         user = input("\nChoose rock, paper or scissors (or 'q' to quit): ").lower()
#         if user == 'q':
#             print("\nGame Over!")
#             break
#         if user not in options:
#             print("⚠️ Invalid choice. Try again.")
#             continue

#         comp = random.choice(options)
#         print(f"Computer chose: {comp}")

#         if user == comp:
#             print("🤝 It's a Draw!")
#         elif (user == "rock" and comp == "scissors") or \
#              (user == "paper" and comp == "rock") or \
#              (user == "scissors" and comp == "paper"):
#             print("✅ You Win!")
#             user_score += 1
#         else:
#             print("❌ You Lose!")
#             comp_score += 1

#         print(f"🏆 Score: You {user_score} | Computer {comp_score}")

# play_game()


import random 

def play_game():
    options = ["rock", "paper", "scissors"]
    print("\n<----- Welcome to Rocl, Paper, Scissor's Game..!! ----->")

    user_score = 0
    comp_score = 0

    while True:
        user = input("\n Choose rock, paper, scissor or q (q for quit): ").lower()
        if user == "q":
            print("\n Game Over")
            break
        if user not in options:
            print("\. Invalid Choice.. Try again....")
            continue

        comp = random.choice(options)
        print(f"Computer chooses: {comp}")

        if user == comp:
            print("\n It's a Draw...")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print ("You Win...!!!")
            user_score += 1
        else:
            print("You loose...")
            comp_score += 1

        print(f" \n SCORE-----> You: {user_score}  | Computer: {comp_score}")

play_game()