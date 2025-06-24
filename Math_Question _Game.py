import random 

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1,100)
    operator = random.choice(["+", "-", "*"])

    question = f"{num1} {operator} {num2}"
    answer = eval(question)
    return question, answer

def math_challenge():
    score = 0
    print("\n<----- Welcome to Saad's Maths Question and Answer game.----->")
    print("\n Answer the 5 math questions correctly..!!\n")

    for i in range(1, 6):
        question, answer = generate_question()
        print(f"Q{i}.  What is {question}..??")
        try:
            user_input = int(input("Enter your answer: "))
            if user_input == answer:
                print("Correct..!!\n")
                score += 1
            else:
                print(f"Wrong answer..The answer was {answer}\n")
        except:
            print("Invalid input..Skipped..!!")

    print(f"Gave over..Thank you for playing..Your final score: {score}/5\n")
    if score == 5:
        print("You are Genius..!!")
    elif score >= 3:
        print("Well played..")
    else:
        print("Nice try..Keep practicing..")

math_challenge()
    