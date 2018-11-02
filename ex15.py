'''
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''

nbr = int(input())
res = 0
for digit in range(1, 4 + 1):
    tmp = ''
    for i in range(1, digit + 1):
        tmp += str(nbr)
    res += int(tmp)

print(res)