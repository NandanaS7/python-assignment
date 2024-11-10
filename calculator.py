print("BASIC CALCULATOR")
print('\n')
 
def add(x, y): 
    
    return x + y

def sub(x, y):
   
    return x - y

def mul(x, y):
    
    return x * y

def div(x, y):
    
    if y == 0:
        return "Error: Division by zero"
    return x / y
print("Select the operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
def main():
    choice = input("Enter choice (1/2/3/4): ")
    if choice=='1':   
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice=='2':
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "-", num2, "=", sub(num1, num2))
    elif choice=='3':          
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "*", num2, "=", mul(num1, num2))
    elif choice=='4':         
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(num1, "%", num2, "=", div(num1, num2))
    else:
        print("Invalid Input")
while True:
    main()
    a=input("Do you want to perform another calculation? (yes/no): ")
    if(a=="yes"):
       continue
    else:
       print("Wrong option.")
       break
