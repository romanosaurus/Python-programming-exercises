'''
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''

ipt = input()
digit = 0
letter = 0

for i in ipt:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        letter += 1

print('LETTERS ' + str(letter))
print('DIGITS ' + str(digit))