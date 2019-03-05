# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it
# print(f'term: {term}/number: {number}')

num = 0
add = 1

for i in range(51):
    print(f'term: {i} / number: {num}')
    new = num + add
    num = add
    add = new

#     new = 0 + 1
#     num = 1
#     add = 1

#     new = 1 + 1
#     num = 1
#     add = 2

#     new = 1 + 2
#     num = 2
#     add = 3

#     new = 2 + 3
#     num = 3
#     add = 5

#     new = 3 + 5
#     num = 5
#     add = 8