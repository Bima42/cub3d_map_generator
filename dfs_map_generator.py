import random

sizex = 10
sizey = 10

maze = []
skip = 0

def getcase(x, y):
	if (x < 0 or y < 0 or x >= sizex or y >= sizey):
		return ("-1")
	return (maze[y][x])

for i in range(sizey):
	line = []
	for j in range(sizex):
		line.append("1")

	maze.append(line)

stack = []

# Pick a random pos in maze, borders exclude
# Stock those coords in stack
stack.append({"x": random.randint(1, sizex - 2), "y": random.randint(1, sizey - 2)})

# Put a 0 char on coords generated before
maze[stack[0]["y"]] [stack[0]["x"]] = "0"


# infinite loop to create way on maze
while (len(stack) > 0):
	lst = [0,1,2,3] # 4 differents ways to move
	ok = 0
	me = stack[-1]
	futur = {} # dictionary

	while (ok == 0 and len(lst) > 0):
		choice = random.randint(0, len(lst) - 1)

		if (lst[choice] == 0 and getcase(me["x"], me["y"] - 1) == "1"): # choice : 0 = move up

			if (getcase(me["x"] - 1, me["y"] - 1) == "1" and getcase(me["x"], me["y"] - 2) == "1"):
				ok = 1
				futur = {"x": me["x"], "y": me["y"] - 1}


		if (lst[choice] == 1 and getcase(me["x"] - 1, me["y"]) == "1"): # choice : 1 = move left

			if (getcase(me["x"] - 1, me["y"] + 1) == "1" and getcase(me["x"] - 2, me["y"]) == "1"):
				ok = 1
				futur = {"x": me["x"] - 1, "y": me["y"]}


		if (lst[choice] == 2 and getcase(me["x"], me["y"] + 1) == "1"): # choice : 2 = move down

			if (getcase(me["x"] + 1, me["y"] + 1) == "1" and getcase(me["x"], me["y"] + 2) == "1"):
				ok = 1
				futur = {"x": me["x"], "y": me["y"] + 1}


		if (lst[choice] == 3 and getcase(me["x"] + 1, me["y"]) == "1"): # choice : 3 = move right

			if (getcase(me["x"] + 1, me["y"] + 1) == "1" and getcase(me["x"] + 2, me["y"]) == "1"):
				ok = 1
				futur = {"x": me["x"] + 1, "y": me["y"]}

		lst.pop(choice)

# Append new coords in stack
	if (ok == 1):
		maze[futur["y"]][futur["x"]] = "0"
		stack.append(futur)
	else:
		stack.pop()

x = random.randint(1, sizex - 2) 
y = random.randint(1, sizey - 2)
while maze[y][x] != "0":
	x = random.randint(1, sizex - 2) 
	y = random.randint(1, sizey - 2)

orientation = ["N", "S", "W", "E"]
maze[y][x] = random.choice(orientation)

file1 = open("map_test.cub", "w+")
path = input("Enter your texture path: ")
type_file = input("Enter your type file (xpm for example): ")

file1.write(f'NO {path}NO.{type_file}\n')
file1.write(f'SO {path}SO.{type_file}\n')
file1.write(f'EA {path}EA.{type_file}\n')
file1.write(f'WE {path}WE.{type_file}\n')

rgb = input("Enter your ceiling color R,G,B format: ")
file1.write(f'C {rgb}\n')
rgb = input("Enter your floor color R,G,B format: ")
file1.write(f'F {rgb}\n\n')

for i in range(sizey):
	file1.write("".join(maze[i]))
	file1.write("\n")
