#hw7pr2.py
#Game of Life
from random import *
import random

def createOneRow(width):
	""" returns one row of zeros of width "width"...
		 You might use this in your createBoard(width, height) function """
	row = []
	for col in range(width):
		row += [0]
	return row

def createBoard(width,height):
	A = []
	for row in range(height):
		A += [createOneRow(width)]
	return A

def printBoard(A):
	for row in A:
		for col in row:
			print(col,end=" ")
		print()
	print("\n")

def diagonalize(width, height):
	A = createBoard(width, height)
	for row in range(1,height-1):
		for col in range(1,width-1):
			if row == col:
				A[row][col] = 1
			else:
				A[row][col] = 0
	return A

def innerCells(w,h):
	A = createBoard(w,h)
	for row in range(1,h):
		for col in range(1,w):
			if (row == 0) or (row == h-1):
				A[row][col] = 0
			elif (col == 0) or (col == w-1):
				A[row][col] = 0
			else:
				A[row][col] = 1
	return A

def randomCells(w,h):
	A = createBoard(w,h)
	for row in range(1,h):
		for col in range(1,w):
			if (row == 0) or (row == h-1):
				A[row][col] = 0
			elif (col == 0) or (col == w-1):
				A[row][col] = 0
			else:
				A[row][col] = random.choice([0,1])
	return A

def copy(A):
	height = len(A)
	width = len(A[0])
	newA = createBoard(width,height)

	for row in range(height):
		for col in range(width):
			newA[row][col] = A[row][col]
	return newA

def innerReverse(A):
	height = len(A)
	width = len(A[0])
	newA = createBoard(width,height)

	for row in range(height):
		for col in range(width):
			if (row == 0) or (row == height-1):
				A[row][col] = 0
			elif (col == 0) or (col == width-1):
				A[row][col] = 0
			elif A[row][col] == 1:
				newA[row][col] = 0
			elif A[row][col] == 0:
				newA[row][col] = 1
	return newA

def countNeighbors(row,col,A):
	liveCount = 0
	if A[row-1][col] == 1:
		liveCount += 1
	if A[row-1][col+1] == 1:
		liveCount += 1
	if A[row-1][col-1] == 1:
		liveCount += 1
	if A[row][col+1] == 1:
		liveCount += 1
	if A[row][col-1] == 1:
		liveCount += 1
	if A[row+1][col] == 1:
		liveCount += 1
	if A[row+1][col+1] == 1:
		liveCount += 1
	if A[row+1][col-1] == 1:
		liveCount += 1

	return liveCount

def next_life_generation(A):
	height = len(A)
	width = len(A[0])
	newA = createBoard(width,height)

	for row in range(height):
		for col in range(width):
			if (row == 0) or (row == height-1):
				newA[row][col] = 0
			elif (col == 0) or (col == width-1):
				newA[row][col] = 0
			elif(countNeighbors(row,col,A) < 2):
				newA[row][col] = 0
			elif(countNeighbors(row,col,A) > 3):
				newA[row][col] = 0
			elif(A[row][col] == 0 and (countNeighbors(row,col,A) == 3)):
				newA[row][col] = 1
			else:
				newA[row][col] = A[row][col]
	return newA

#A = createBoard(3,6)
#A = diagonalize(7,6)
#A = innerCells(5,5)
#A = randomCells(8,8)
#printBoard(A)
#print("\n")
#newA = copy(A)
#printBoard(newA)
#print("\n")
#A[2][2] = 5
#printBoard(A)
#print("\n")
#printBoard(newA)
#A2 = innerReverse(A)
#printBoard(A2)
#print("\n")
'''A = [[0,0,0,0,0],
	[0,0,1,0,0],
	[0,0,1,0,0],
	[0,0,1,0,0],
	[0,0,0,0,0]]
printBoard(A)
countNeighbors(2,1,A)
countNeighbors(2,2,A)
countNeighbors(0,1,A)
A = [ [0,0,0,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,0,0,0]]
printBoard(A)
A2 = next_life_generation(A)
printBoard(A2)
A3 = next_life_generation(A2)
printBoard(A3)'''

