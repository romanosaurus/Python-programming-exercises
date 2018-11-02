'''
A robot moves in a plane starting from the original point (0,0).
The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
¡­
The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
import math


dif_position = {"UP": 0, "DOWN": 0, "LEFT": 0, "RIGHT": 0}
xori = 0
yori = 0

while True:
    res = input()
    if res:
        res = res.split(' ')
        if res[0] in dif_position:
            dif_position[res[0]] += int(res[1])
    else:
        break
x = dif_position["UP"] - dif_position["DOWN"]
y = dif_position["LEFT"] - dif_position["RIGHT"]

res = int(math.sqrt(math.pow((xori - x), 2) + math.pow((yori - y), 2)))

print(res)
