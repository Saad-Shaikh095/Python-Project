import random 

subjects = [
    "ShahRukh Khan",
    "M.S. Dhoni",
    "Prime Minister Narendra Modi",
    "The Mumbai Don",
    "Chai Wala",
    "Lazy Cat",
    "King Lucky",
    "Birthday Boy"
]

Verbs = [
    "eats",
    "sleeps",
    "ran",
    "appears",
    "walks",
    "wins",
    "goes to",
    "enters"
]

objects = [
    "India",
    "as King of Bollywood",
    "GOAT",
    "inside the room",
    "India Gate",
    "IPL 2021",
    "Taj Mahal",
    "Dubai"
]

while True:
    subject = random.choice(subjects)
    verb = random.choice(Verbs)
    object = random.choice(objects)

    headline = f"BREAKING NEWS: {subject} {verb} {object}"
    print("\n" + headline)

    user = input("Do you want to gnerate another news/ headling...?? (yes/no)").strip().lower()
    if user == "no":
        break

print("\n Thanks for using this Fake News Generator. Have a nice day...!!!    ~Saad Shaikh")