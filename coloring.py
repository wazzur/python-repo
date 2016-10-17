import sys
import pprint
from random import randint


def createMatrix(*dim):
	"Creates a 2D or 3D Matrix"
	if len(dim) == 2:
		matrix = [[-1 for x in range(dim[0])] for y in range(dim[1])]
	elif len(dim) == 3:
		matrix = [[[-1 for x in range(dim[0])] for y in range(dim[1])] for z in range(dim[2])]
	else:
		print("unhandled number of dimensions")
	return matrix;


def colorRandomly(matrix, K, dim):
	"Assigns colors randomly to the matrix based on the given K value in 2 or 3 dimensions"
	for a, x in enumerate(matrix):
		for b, y in enumerate(matrix):
			if dim == 2:
				matrix[a][b] = randint(0, K-1)
			elif dim == 3:
				for c, z in enumerate(matrix):
					matrix[a][b][c] = randint(0, K-1)
	return matrix;


def calculateL(matrix, K, dim):
	"Calculates the sums of distances of all colors in the matrix and returns the min"
	lowest = sys.maxsize
	pairSums = []
	for c in range(0, K):
		sum = sumClosestPairs(matrix, c, dim)
		pairSums.append(sum)
		if sum < lowest:
			lowest = sum

	print("\nThe sums for each colors are: ")
	print(pairSums)

	"Objective is to maximize the minimum of these distances"
	return lowest;


def sumClosestPairs(matrix, color, dim):
	"find and sum the closest pair distances of same color in matrix"
	sum = 0
	for a, x in enumerate(matrix):
		for b, y in enumerate(matrix):
			if dim == 2:
				if matrix[a][b] == color:
					sum += findClosest(matrix, color, dim, a, b)
			elif dim == 3:
				for c, z, in enumerate(matrix):
					if matrix[a][b][c] == color:
						sum += findClosest(matrix, color, dim, a, b, c)
	return sum

def findClosest(matrix, color, dim, a2, b2, c2=None):
	"Finds the closest element of the same color in the matrix for both 2D and 3D"
	min = sys.maxsize
	for a, x in enumerate(matrix):
		for b, y in enumerate(matrix):
			if c2 is None:
				if int(a) == int(a2) and int(b) == int(b2):
					continue
				if matrix[a][b] == color:
					checkDist = dist(dim,a2,b2,a,b)
					if checkDist < min:
						min = checkDist
			else:
				for c, z in enumerate(matrix):
					if int(a) == int(a2) and int(b) == int(b2) and int(c) == int(c2):
						continue
					if matrix[a][b][c] == color:
						checkDist = dist(dim,a2,b2,c2,a,b,c)
						if checkDist < min:
							min = checkDist
	return [0 if min == sys.maxsize else min][0]


def dist(dim, *points):
	"Calculates the distance between two points using basic algebra"
	"Supports both 2d and 3d elements"
	if dim == 2:
		a = (points[0], points[1])
		b = (points[2], points[3])
		return ((((b[0]-a[0])**2)+((b[1]-a[1])**2))**(1/2))
	elif dim == 3:
		a = (points[0], points[1], points[2])
		b = (points[3], points[4], points[5])
		return ((((b[0]-a[0])**2)+((b[1]-a[1])**2)+((b[2]-a[2])**2))**(1/2))
	else:
		print("Error in distance function")

def main():
	"Accepts either command line arguments or will prompt user if none is given"
	"Calls random coloring and calculates the L for the colored matrix"

	dim = 2
	if len(sys.argv) == 4:
		X = sys.argv[1]
		Y = sys.argv[2]
		K = sys.argv[3]
	elif len(sys.argv) == 5:
		dim = 3
		X = sys.argv[1]
		Y = sys.argv[2]
		Z = sys.argv[3]
		K = sys.argv[4]
	else:
		X = input("Enter X dimension value: ")
		Y = input("Enter Y dimension value: ")
		choice = input("would you like a Z dimension?  [Y/N]: ")
		if choice == ('Y' or 'y'):
			dim = 3
			Z = input ("Enter Z dimension value: ")
		K = input("Enter how many colors(K) you would like: ")

	print("X is set to " + X)
	print("Y is set to " + Y)
	if dim == 3:
		print("Z is set to " + Z)
	print(K + " colors will be used")

	if dim == 2:
		test = createMatrix(int(X), int(Y))
	if dim == 3:
		test = createMatrix(int(X), int(Y), int(Z))

	print("\n")
	test = colorRandomly(test, int(K), dim)
	pprint.pprint(test)
	print("\n")

	L = calculateL(test, int(K), dim)
	print("\nMin L for this coloring: ")
	print(L)


"RUNS THE PROGRAM"
main()
