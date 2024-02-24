print("\n--------------- Calculator ---------------\n")

number = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))

print("")

print("Operations")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Division")

print("")

select_operation = int(input("Enter an operation: "))

print("")

if select_operation == 1:
    print(f"{number} + {number_2} = {number+number_2}")
elif select_operation == 2:
    print(f"{number} - {number_2} = {number-number_2}")
elif select_operation == 3:
    print(f"{number} * {number_2} = {number*number_2}")
elif select_operation == 4:
    if number_2 != 0:
        print(f"{number} / {number_2} = {number/number_2}")
    else:
        print("Cannot divide by 0")
else:
    print("Not a valid operation")
