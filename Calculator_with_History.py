History_File = "history.txt"

def show_history():
    file = open(History_File, "r")
    lines = file.readlines()
    if len(lines) == 0:
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
        file.close()

def clear_history():
    file = open(History_File, "w")
    file.close()
    print("History cleared.")

def save_to_history(equation, result):
    file = open(History_File, "a")
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculator(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid Input. Use format: number operator number (eg. 2 + 2)") 
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2 
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    elif op == "%":
        result = num1 % num2
    elif op == "**":
        result = num1 ** num2
    else:
        print("Invalid Operater. Use only + - * / %  ** ")
        return

    if int(result) == result:
        result = int(result)
    print("Result:", result)
    save_to_history(user_input, result)

def main():
    print("-----Simple Calculator (type history, clear, or exit)-----")
    while True:
        user_input = input("Enter calcualtion (+ - * / % **) or command history, clear or exit")     
        if user_input == "exit":
            print("Goodbye!")
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculator(user_input)
main()