my_list = [1, 'apple', 3, 'banana', 5, 'cherry']

check_type = lambda x: isinstance(x, int) or isinstance(x, str)

result = all(map(check_type, my_list))

if result:
    print("All elements in the list are either integers or strings.")
else:
    print("Not all elements in the list are either integers or strings.")