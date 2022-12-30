def how_many_numbers(numbers): 
    unique_numbers = set(numbers)
    return len(unique_numbers)

print(how_many_numbers \
([11, 12, 13, 11, 12, 13, 14, 11]))
# 4

print(how_many_numbers \
([5, 5, 3, 1, 5, 5, 7, 2]))
# 4

