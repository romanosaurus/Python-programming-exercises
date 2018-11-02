'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''

strfinal = input()

upper = 0
lower = 0

for i in strfinal:
    if i == i.upper() and i.isalpha():
        upper += 1
    elif i == i.lower() and i.isalpha():
        lower += 1

print('UPPER CASE ' + str(upper))
print('LOWER CASE ' + str(lower))
