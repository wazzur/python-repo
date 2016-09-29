import sys
import math
from random import randint


"TODO: create dictionary to map integers to colors"


def createMatrix(X, Y):
	matrix = [[-1 for x in range(X)] for y in range(Y)]
	return matrix;


def printRawMatrix(matrix):
	for i, y in enumerate(matrix):
		print(matrix[i])
	return;


def colorMatrix(matrix):
	"TODO: NEEDS WORK"
	for i, x in enumerate(matrix):
		for j, y in enumerate(matrix):
	                "TODO: set matrix number to dictionary color entry"
	return matrix;


def color(matrix, K):
	for i, x in enumerate(matrix):
		for j, y in enumerate(matrix):
			matrix[i][j] = randint(0, K-1)
	return matrix;


def calculateL(matrix, K):
	lowest = 99999
	pairSums = []
	for c in range(0, K):
		sum = sumClosestPairs(matrix, c)
		pairSums.append(sum)
		if sum < lowest:
			lowest = sum

	print("\nThe sums for each colors are: ")
	print(pairSums)

	"Objective is to maximize the minimum of these distances"
	return lowest;


def sumClosestPairs(matrix, color):
	"find and sum the closest pair distances of same color in matrix"
	sum = 0

	for i, x in enumerate(matrix):
		for j, y in enumerate(matrix):
			if matrix[i][j] == color:
				sum += findClosest(matrix, i, j, color)
	return sum;


def findClosest(matrix, x1, y1, color):
	min = 99999
	for i, x2 in enumerate(matrix):
		for j, y2 in enumerate(matrix):
			if int(i) == int(x1):
				if int(j) == int(y1):
					continue
			if matrix[i][j] == color:
				checkDist = dist(x1,y1,i,j)
				if checkDist < min:
					min = checkDist
	if min == 99999:
		return 0;
	else:
		return min;


def dist(x1, y1, x2, y2):
	a = (x1, y1)
	b = (x2, y2)
	return math.hypot(b[0]-a[0], b[1]-a[1]);


def main():
	X = sys.argv[1]
	Y = sys.argv[2]
	K = sys.argv[3]
	print("X is set to " + X)
	print("Y is set to " + Y)
	print("up to " + K + " colors will be used")

	test = createMatrix(int(X), int(Y))
	print("\n")
	test = color(test, int(K))

	printRawMatrix(test)
	print("\n")
	colorMatrix(test)
	"TODO: test printing colored matrix after function is written"

	L = calculateL(test, int(K))
	print("\nMin L for this coloring:")
	print(L)

main()
