# TurtleDrawLite - Part 3
# By: Anahi Guerrero 
#
# All rights reserved.

import turtle
import math


turtle.setup(450, 450)  # Set window size


TEXTFILENAME = 'turtle-draw.txt'

# Todo: Ask user for the file name. 

print('TurtleDrawLite - Part 3')

anahiturtleDraw = turtle.Turtle()
anahiturtleDraw.speed(10)
# anahiturtleDraw.penup()
print('Reading a text file line by line.')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()
total_distance = 0.0


#calculate distance function
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

#distance groups
groups=[]
current_group=[]

while line:
    # print(line, end='')
    parts = line.split(' ')

    if line.strip()=='stop':
        if current_group:
            groups.append(current_group)
            current_group=[]
    elif line:
        x,y=map (int,line.split()[1:])
        current_group.append((x,y))
        # print(x,y)
            
    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])
        # total_distance += abs(x)+abs(y)
    
        
        anahiturtleDraw.color(color)
        anahiturtleDraw.goto(x,y)
        # Todo: Calculate the distance and add it to the total distance.
        anahiturtleDraw.pendown()
    
    if (len(parts) == 1): # Assumes that a single word on a line is "stop"
        anahiturtleDraw.penup()
    
    line = turtleDrawTextfile.readline()
    
    
if current_group:
    groups.append(current_group)


#calculate grand total distance
grand_total=0 
for i,group in enumerate(groups):
    total_distance=0
    for j in range(1,len(group)):
        total_distance+=distance (group[j-1],group[j])
    grand_total+=total_distance
print(f"Grand Total: {grand_total:.2f}")

anahiturtleDraw.penup()
anahiturtleDraw.goto(-1, -150)
anahiturtleDraw.pendown()
anahiturtleDraw.color('blue')
anahiturtleDraw.write(f'Total Distance Marked: {grand_total:.2f}', align='left', font=('Arial', 10, 'normal'))
anahiturtleDraw.penup()


# print('\nTotal distance traveled:', total_distance)

turtle.done()
turtleDrawTextfile.close()



print('\nEnd')

    
