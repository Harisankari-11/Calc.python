def unique_calculator():
    print("Welcome to the Unique Calculator!")
    print("Operations supported: +, -, *, /")

    while True:
        try:
            number1 = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ")
            number2 = float(input("Enter the second number: "))

            if operator == '+':
                result = number1 + number2
            elif operator == '-':
            
                result = number1 - number2
            elif operator == '*':
                result = number1 * number2
            elif operator == '/':
                result = number1 / number2
            else:
                print("Invalid operator! Please try again.")
                continue

            print("Result: ", result)

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except ZeroDivisionError:
            print("Error! Division by zero.")
        except Exception as e:
            print("An error occurred:", e)

        choice = input("Do you want to perform another calculation? (yes/no): ")
        if choice.lower() != 'yes':
            print("Thank you for using the Unique Calculator!")
            break

unique_calculator()
