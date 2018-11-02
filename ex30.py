'''
Define a function that can accept two strings as input and print the string with maximum length in console. 
If two strings have the same length, then the function should print al l strings line by line.
'''


def compare():
    arr = []
    for i in range(0, 2):
        arr.append(input())
    print('-----------')
    if (len(arr[0]) > len(arr[1])):
        print(arr[0])
    elif (len(arr[0]) < len(arr[1])):
        print(arr[1])
    else:
        print(arr[0])
        print(arr[1])


compare()
