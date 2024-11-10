print("FIBONACCI SEQUENCE")
print('\n')
n=int(input("Enter the number of terms:"))
x=0
y=1
i=3
print("Fibonacci series:\n")
print('\n')
print(x ,y ,end=" ")
while(i<=n):
    z=x+y
    print(z,end=" ")
    x=y
    y=z
    i=i+1