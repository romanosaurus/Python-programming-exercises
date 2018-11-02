'''
With a given integral number n, write a program to generate a dictionary that
contains (i, i*i) such that is an integral number
between 1 and n (both included). and then the program should print the dictionary.
'''

x = 8
res = {}
for y in range(1, x + 1):
    res[y] = y * y

print(res)