	
import random
from time import sleep
from colorama import Fore, Back, Style

def newGen(grid, size):
	future = [['*' for _ in range(size)] for _ in range(size)]

	for i in range(size):
		for j in range(size):
			alive_count = 0

			if grid[i][j] == 'o' or grid[i][j] == '*':
				nextj = (j + 1) % size
				nexti = (i + 1) % size
				backi = (i - 1 + size) % size
				backj = (j - 1 + size) % size

				if grid[backi][backj] == 'o':  # Check top-left
					alive_count += 1
				if grid[backi][j] == 'o':  # Check directly above
					alive_count += 1
				if grid[backi][nextj] == 'o':  # Check top-right
					alive_count += 1
				if grid[i][nextj] == 'o':  # Check right
					alive_count += 1
				if grid[nexti][nextj] == 'o':  # Check bottom-right
					alive_count += 1
				if grid[nexti][j] == 'o':  # Check directly below
					alive_count += 1
				if grid[nexti][backj] == 'o':  # Check bottom-left
					alive_count += 1
				if grid[i][backj] == 'o':  # Check left
					alive_count += 1

				if alive_count < 2 and grid[i][j] == 'o':
					future[i][j] = '*'
				elif (alive_count == 2 or alive_count == 3) and grid[i][j] == 'o':
					future[i][j] = 'o'
				elif alive_count > 3 and grid[i][j] == 'o':
					future[i][j] = '*'
				elif alive_count == 3 and grid[i][j] == '*':
					future[i][j] = 'o'

	return future
				
				




size=int(input("Please enter a grid size (IE: Entering 10 makes a 10x10):\t"))

chance=int(input("Please enter the number chance of a cell being alive (IE: 20 means 20%, 30 means 30%, etc.)"))
def displayBoard(grid,size):
	for i in range(size):
		for j in range(size):
			# print(len(grid))
			if grid[i][j]=='o':
				print(f"{Fore.GREEN}{grid[i][j]}", end='')
			else:
				print(f"{Fore.RED}{grid[i][j]}", end='')
			# print(grid[i][j],end='')

		print("\n",end='')
	print()
people=[]
temp_list=list()
# Create List of list
for i in range(size):
	people.append([])
	for j in range(size): 
		check=random.randint(0,100)
		if check<=chance:
			val='o'
		else:
			val='*'
		# print(val)
		people[i].append(val)


# people = [
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "o", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "o", "*", "*", "*", "o","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "o", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "o", "*", "*", "*", "*", "o","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "o", "o", "o", "o", "o", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
# 	 ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*","*", "*", "*", "*", "*", "*", "*", "*", "*", "*"]
# ]
displayBoard(people,size)
# print(people)

while True:
	future=newGen(people,size)
	print("\n\n")
	displayBoard(future,size)
	sleep(0.1)
	print("\n\n")
	people=newGen(future,size)
	displayBoard(people,size)

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.