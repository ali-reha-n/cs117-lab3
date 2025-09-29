run_loop = True

def is_even_or_odd(num):
    if(num<0):
        print("Please enter a non-negative number.")
    elif num % 2 == 0:
        print("Even")
    else:
        print("Odd")

def calculate_percentage(part, whole):
        if whole == 0:
            print("Whole cannot be zero.")
        else:
            percentage = (part / whole) * 100
            print("The percentage is:", percentage)

def add(a, b):
    print("The sum is:", a + b)

def subtract(a, b):
    print("The difference is:", a - b)

def multiply(a, b):
    print("The product is:", a * b)

def divide(a, b):
    if b == 0:
        print("Cannot divide by zero.")
    else:
        print("The quotient is:", a / b)

while run_loop:
    print("Choose one of the following options (Input your choice using 1,2 or 3):")
    print("1. Check if the number is even or odd.")
    print("2. Calculate the percentage of a number.")
    print("3. Perform the operations of +,-,*,/ on two numbers.")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = int(input("Enter a number: "))
        is_even_or_odd(number)
    elif choice == 2:
        part = float(input("Enter the part value: "))
        whole = float(input("Enter the whole value: "))
        calculate_percentage(part, whole)
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        if operation == '+':
            add(num1, num2)
        elif operation == '-':
            subtract(num1, num2)
        elif operation == '*':
            multiply(num1, num2)
        elif operation == '/':
            divide(num1, num2)
        else:
            print("Invalid operation.")
    else:
        print("Invalid choice.")
    do_again = str(input("Do you want to perform another operation? (yes/no): "))
    if do_again == "no":
        run_loop = False
        print("Terminating..........")
    
    