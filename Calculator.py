# Simple CLI Calculator
# Handles arithmetic operations with error handling
while True:
    print("Welcome to Basic Calculator")

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the Second number: "))

        print("\nChoose an operator !")
        print(
            "Select this (/) if you want to Divide.\nSelect this (*) if you want to Multiply.\nSelect this (-) if you want to Subtraction.\nSelect this (+) if you want to Addition.\n"
        )

        oprator = input("Enter Operation !!").strip()

        match oprator:
            case "/":
                if b == 0:
                    print("Division of zero with any number is Undefined !!")
                else:
                    print(f"The result of {a} {oprator} {b} is: {a / b}")
            case "*":
                print(f"The result of {a} {oprator} {b} is: {a * b}")
            case "-":
                print(f"The result of {a} {oprator} {b} is: {a - b}")
            case "+":
                print(f"The result of {a} {oprator} {b} is: {a + b}")
            case _:
                print(
                    "Entered Operator is invalid ! Please choose from this ('/','*','-','+')!!"
                )

    except ValueError:
        print("Input Error !! Please enter the valid input !")
    except Exception as e:
        print(f"Unexpected Error: {e}")
 
    user_choice = input("Enter to calculate or type 'q' for quit: ").strip().lower()
    if user_choice == "q":
        print("Thanks for using the calculator. Goodbye !!")
        break
    
#---------------------------------Ending----------------------------------