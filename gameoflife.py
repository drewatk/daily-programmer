#!/usr/bin/env python3

###################################
#   /r/dailyprogrammer 165 Easy   #
#       ASCII Game of Life        #
#          Drew Atkinson          #
###################################
	
import sys

# error checking
if len(sys.argv) != 2:
    print('Usage: gameoflife.py input_file.txt')
    sys.exit(1)
    
# file opening adapted from /u/ehcubed
with open(sys.argv[1], "r") as f:
    [N, X, Y] = [int(k) for k in f.readline().split()]
    grid = f.read().split()

# prompt to print each iteration
if input('Print each iteration? (y or n):') == 'y':
    printEach = True
else:
    printEach = False

#for every iteration
for n in range(N):
    newGrid = ''
	
	#for every cell
    for x in range(X):
        for y in range(Y):
            alive = 0
            for i in [(x - 1) % X, x, (x + 1) % X]:
                for j in [(y - 1) % Y, y, (y + 1) % Y]:
                    if (i,j) != (x,y) and grid[i][j] == '#':
                        alive += 1
				
				
			#if off and 3 neighbors are on, turn it on
            if grid[x][y] == '.' and alive == 3:
                newGrid += '#'
			#if on and less than 2 of its neighbors are on or more than 3 of neigbors are on, kill it 
            elif grid[x][y] == '#' and alive not in [2, 3]:
                newGrid += '.'
            else:
                newGrid += grid[x][y]
        newGrid += '\n'
    grid = newGrid.split()
    if printEach:
        print('\n'.join(grid))
        print()

if not printEach:
    print("\n".join(grid))
