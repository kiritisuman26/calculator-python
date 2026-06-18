def add(num1,num2):
    return num1 + num2
def sub(num1 , num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1,num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1/num2
def mod(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero"
    else:
        return num1 % num2
def power(num1, num2):
    return num1 ** num2
print("WELCOME TO THE CALCULATOR APP")
while True:
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. MULTIPLICATION")
    print("4. DIVISION")
    print("5. MODULUS")
    print("6. POWER")
    print("7.EXIT")
    ch = int(input("Choose an operation to perform(1-7) : "))
    if ch not in [1,2,3,4,5,6,7]:
        print("Invalid choice. Please choose a valid operation(1-7) : ")
        continue
    if ch == 7:
        print("Thank you for using the Calculator App")
        break
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number : "))
    if ch == 1:
        result = add(num1,num2)
        print(f"Addition of {num1} and {num2} is {result}")
    elif ch == 2:
        result = sub(num1, num2)
        print(f"Subtraction of {num1} and {num2} is {result}")
    elif ch == 3:
        result = multiply(num1, num2)
        print(f"Multiplication of {num1} and  {num2} is { result}")
    elif ch == 4:
        result = divide(num1, num2)
        print(f"Division of {num1} and {num2} is {result}")
    elif ch == 5:
        result = mod(num1, num2)
        print(f"Modulus of {num1} and {num2} is {result}")
    elif ch == 6 :
        result = power(num1, num2)
        print(f"Power of {num1} and {num2} is {result:.2f}")
    ans = input("Do you want to perform another operation? (yes/no) :")
    if ans.lower() == 'no':
        print("Thank you for using the Calculator App")
        break
    else:
        continue
    
