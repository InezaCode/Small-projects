print("Welcome to my calculator!")
number1 = float(input("Enter your first number: "))
number2 = float(input("Enter your second number: "))

print("Choose an operation:")
print("1 = Addition")
print("2 = Subtraction")
print("3 = Multiplication")
print("4 = Division")
choice = input("Enter 1, 2, 3, or 4: ")

if choice == "1":
    result = number1 + number2
    print("Result:", result)
elif choice == "2":
    result = number1 - number2
    print("Result:", result)
elif choice == "3":
    result = number1 * number2
    print("Result:", result)
elif choice == "4":
    if number2 == 0:
        print("You cannot divide by zero.")
    else:
        result = number1 / number2
        print("Result:", result)
else:
    print("That is not a valid choice.")
