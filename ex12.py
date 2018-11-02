'''
Write a program, which will find all such numbers between 1000 and 3000
(both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence
on a single line.
'''

begin = 1000
end = 3000
finalstr = ''

for nb in range(begin, end + 1):
    s = str(nb)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        finalstr += str(nb) + ','
finalstr = finalstr[:-1]
print(finalstr)