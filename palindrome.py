print("PALINDROME CHECKER")
print('\n')
def palindrome(s):
    clear=s.replace(" "," ").lower()
    rev=clear[::-1]
    return clear==rev
s=input("Enter the string:")
if palindrome(s):
    print("True")
else:
    print("False")