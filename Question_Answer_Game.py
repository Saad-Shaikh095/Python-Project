questions = [
    {"question": "What is the National Animal of India..??", "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Leopard"], "answer": "B"},
    {"question": "What is the Capital of India..??", "options": ["A. Mumbai", "B. Kolkata", "C. Delhi", "D. Chennai"], "answer": "C"},
    {"question": "What is the National Sport of India..??", "options": ["A. Cricket", "B. Football", "C. Hockey", "D. None"], "answer": "D"},
    {"question": "What is the Economic Capital of India..??", "options": ["A. Mumbai", "B. Kolkata", "C. Delhi", "D. Chennai"], "answer": "A"},
    {"question": "When did India get its Independence..??", "options": ["A. 1949", "B. 2000", "C. 1950", "D. 1947"], "answer": "D"}
]

def start_quiz():
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for opt in q["options"]:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ").upper()

        if user_ans == q["answer"]:
            print("Correct...!!!")
            score += 1
        else:
            print(f"Wrong..! Correct answer is: {q['answer']}")

    print("\nQuiz Completed..!!")
    print(f"Your Final Score: {score}/5")

    if score == 5:
        print("You are a Genius..!!")
    elif score >= 3:
        print("Well Played.")
    else:
        print("Keep Practicing.....")

start_quiz()
