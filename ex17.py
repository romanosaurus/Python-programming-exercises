'''
Question:
Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''

res = 0
while True:
    inpt = input()
    if inpt:
        lineparsed = inpt.split(' ')
        if lineparsed[0] == 'D':
            res += int(lineparsed[1])
        else:
            res -= int(lineparsed[1])
    else:
        break

print(res)