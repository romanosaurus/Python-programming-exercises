'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
'''

x = 8
res = 1
for y in range(1, x + 1):
    res *= y
print(res)