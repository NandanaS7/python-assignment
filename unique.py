print("UNIQUE CHARACTERS IN A STRING")
print('\n')

def unique(s):
    char_set = set()
    for char in s.lower():
        if char in char_set:
            return False
        char_set.add(char)
    return True

s = input("Enter the string:")
if unique(s):
    print("True")
else:
    print("False")