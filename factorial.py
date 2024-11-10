print("FACTORIAL OF A NUMBER")
print('\n')

def recursive(n):
    if n == 0:
        return 1
    else:
        return n * recursive(n - 1)

def iterative(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter a non-negative integer: "))

print("\nFactorial of the number using recursive method:")
a = recursive(n)
print("Factorial is:", a)

print("\nFactorial of the number using iterative method:")
b = iterative(n)
print("Factorial is:", b)