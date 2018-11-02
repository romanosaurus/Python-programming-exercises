'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

# Use modulo to know if a number is divible and multiple by the operator


begin = 2000
end = 3200
final_answer = ''
for nbr in range(begin + 1, end + 1):
    if nbr % 7 == 0 and nbr % 5 == 0:
        final_answer += str(nbr) + ','
final_answer = final_answer[:-1]
print(final_answer)