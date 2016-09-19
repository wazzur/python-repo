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
	pairSums = []
	for c in range(0, K):
		pairSums.append(sumClosestPairs(matrix, colorArray[c]))

	print "\nThe sums are: "
	print pairSums

	"Objective is to maximize the minimum of these distances"
	return;

def sumClosestPairs(matrix, color):
	"find and sum the closest pair distances of same color in matrix"
	sum = 0

	for i, x in enumerate(matrix):
		for j, y in enumerate(matrix):
			if matrix[i][j] == color:
				"find closest pair distance"
				"add to sum"
				"make sure pairwise color does not repeat distance"
				pass
	return sum;

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

	calculateL(test, int(K))

main()
