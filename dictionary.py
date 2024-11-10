print("DICTIONARY SORTER")
print('\n')

def sort_dictionary(dictionary):
    sorted_keys = sorted(dictionary.keys())
    sorted_dict = {}
    for key in sorted_keys:
        sorted_dict[key] = dictionary[key]
    return sorted_dict   


user_input = input("Enter a dictionary (e.g., {'a': 1, 'c': 3, 'b': 2}): ")
user_dict = eval(user_input)  
sorted_dict = sort_dictionary(user_dict)  
print(sorted_dict)