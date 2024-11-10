print("PRIME NUMBERS")
print('\n')
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=int(input("Enter the starting range"))
b=int(input("Enter the ending range"))
for n in range(a,b+1):
    if is_prime(n):
        print(n, end=" ")