
print("** DIVISION **")
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if num2 == 0:
    print("Can't divide by zero. Please enter a non-zero number.")

    for i in range(2):
        num2 = int(input("Enter 2nd number again: "))
        if num2 != 0:
            break

    if num2 == 0:
        print("Chance is over!")
    else:
        div = num1 / num2
        print(f"Answer of {num1} and {num2} is {div}")

else:
    div = num1 / num2
    print(f"Answer of {num1} and {num2} is {div}")


