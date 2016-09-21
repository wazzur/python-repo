import sys
import numpy
from random import randint

colorArray = numpy.array(['Red', 'Green', 'Blue', 'Yellow', 'Teal',
                'Magenta', 'Orange', 'Purple'])


def createMatrix(X, Y):
	matrix = numpy.chararray((X,Y), itemsize = 8 )
	matrix[:] = 'Black'
	return matrix;


def printMatrix(matrix):
	for i, y in enumerate(matrix):
		print matrix[i]
	return;


def getColors(K):
	if K < colorArray.size:
		subArray = []
                for i in xrange(0, K):
                        subArray.append(colorArray[i])
                return subArray;
	else:
		return colorArray;


def color(matrix, colorArray):
        for i, x in enumerate(matrix):
		for j, y in enumerate(matrix):
			choice = randint(0, len(colorArray)-1)
			matrix[i][j] = colorArray[choice]
	return matrix;


def calculateL(matrix, K):
	lowest = 99999
	pairSums = []
	for c in range(0, K):
		sum = sumClosestPairs(matrix, colorArray[c])
		pairSums.append(sum)
		if sum < lowest:
			lowest = sum

	print "\nThe sums for each colors are: "
	print pairSums

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
	a = numpy.array((x1, y1))
	b = numpy.array((x2, y2))
	return numpy.linalg.norm(a-b);

def main():
	X = sys.argv[1]
	Y = sys.argv[2]
	K = sys.argv[3]
	print "X is set to " + X
	print "Y is set to " + Y
	print "up to " + K + " colors will be used"

	test = createMatrix(int(X), int(Y))
	print getColors(int(K))

	print "\n"
	test = color(test, getColors(int(K)))
	printMatrix(test)

	L = calculateL(test, int(K))
	print "\nMin L for this coloring:"
	print L

main()
