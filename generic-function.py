def first_and_last(sequence):
    return sequence[:1] + sequence[-1:]

print(first_and_last("wxyz"))
# "wz"
print(first_and_last(('a', 'b', 'c', 'd')))
# ('a', 'd')