# !!! Import Logic.py to any other file required

# Importing modules
import random
from simple_colors import *

# Defining variables
winValue = 2048
score=0

# Initial game starting
def start_game():
	matrix =[]
	for i in range(4):
		matrix.append([""] * 4)
	print(yellow("Welcome to the 2048 Game!", "bright"))
	print(yellow("Commands are as follows : "), end="\n\n")
	print(magenta("'W' or 'w' : Move Up", "italic"))
	print(magenta("'S' or 's' : Move Down", "italic"))
	print(magenta("'A' or 'a' : Move Left", "italic"))
	print(magenta("'D' or 'd' : Move Right", "italic"), end="\n\n")
	print(cyan("'stop': Stop the game anytime", "italic"), end="\n\n")
	return matrix

# Adds random 2 or 4 to a empty space in the matrix
def add_number(matrix):
	r = random.randint(0, 3)
	c = random.randint(0, 3)
	
	while(matrix[r][c] != ""):
		r = random.randint(0, 3)
		c = random.randint(0, 3)
	matrix[r][c] = random.choice([2,4])
	global score
	score += 2

# Print matrix
def print_game(matrix):
	print(red(f"\nTotal Score: {score}\n", ["bold"]))
	for i in range(0,4):
		print(matrix[i])

# Gets the current state of the matrix
def get_current_state(matrix):	
	for i in range(4):
		for j in range(4):
			if(matrix[i][j]== winValue):
				return 'WON'
	for i in range(4):
		for j in range(4):
			if(matrix[i][j]== ""):
				return 'Continue Playing'
	for i in range(3):
		for j in range(3):
			if(matrix[i][j]== matrix[i + 1][j] or matrix[i][j]== matrix[i][j + 1]):
				return 'Try someother move'
	for i in range(1,4):
		for j in range(1,4):
			if(matrix[i][j]== matrix[i -1][j] or matrix[i][j]== matrix[i][j - 1]):
				return 'Try someother move'
	return 'LOST'

# Compress the matrix
def compress(matrix):
	changed = False
	new_matrix = []
	for i in range(4):
		new_matrix.append([""] * 4)
	for i in range(4):
		pos = 0
		for j in range(4):
			if(matrix[i][j] != ""):
				new_matrix[i][pos] = matrix[i][j]
				if(j != pos):
					changed = True
				pos += 1
	return new_matrix, changed

# Merges same numbers
def merge(matrix):
	changed = False
	for i in range(4):
		for j in range(3):
			if(matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != ""):
				matrix[i][j] = matrix[i][j] * 2
				global score;
				score+=matrix[i][j]
				matrix[i][j + 1] = ""
				changed = True
	return matrix, changed

#Reverses the matrix
def reverse(matrix):
	new_matrix =[]
	for i in range(4):
		new_matrix.append([])
		for j in range(4):
			new_matrix[i].append(matrix[i][3 - j])
	return new_matrix

#Transposes the matrix
def transpose(matrix):
	new_matrix = []
	for i in range(4):
		new_matrix.append([])
		for j in range(4):
			new_matrix[i].append(matrix[j][i])
	return new_matrix

#MOVES
#Move left
def move_left(grid):
	new_grid, changed1 = compress(grid)
	new_grid, changed2 = merge(new_grid)
	changed = changed1 or changed2
	new_grid, temp = compress(new_grid)
	return new_grid, changed

# Move Right
def move_right(grid):
	new_grid = reverse(grid)
	new_grid, changed = move_left(new_grid)
	new_grid = reverse(new_grid)
	return new_grid, changed

# Move up
def move_up(grid):
	new_grid = transpose(grid)
	new_grid, changed = move_left(new_grid)
	new_grid = transpose(new_grid)
	return new_grid, changed

# Move down
def move_down(grid):
	new_grid = transpose(grid)
	new_grid, changed = move_right(new_grid)
	new_grid = transpose(new_grid)
	return new_grid, changed

#Optional (Cheat Codes)
def multiply(matrix, multiply):
	for i in range(4):
		for j in range(4):
			matrix[i][j]*=multiply
			global score
			if(type(matrix[i][j]) != str):
				score+=matrix[i][j]
	return matrix
