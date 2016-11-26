import sys
import pprint as pp
import coloringLHD as LHD
from random import randint

def create_matrix(X,Y,Z):
    "Creates a 2D or 3D Matrix"
    if Z:
        matrix = [[[0 for x in range(X)] for y in range(Y)] for z in range(Z)]
    else:
        matrix = [[0 for x in range(X)] for y in range(Y)]
    return matrix;


def random_coloring(matrix, K, Z):
    "Assigns colors randomly to the matrix based on the given K value in 2 or 3 dimensions"
    for a, x in enumerate(matrix):
        for b, y in enumerate(x):
            if Z:
                for c, z in enumerate(y):
                    matrix[a][b][c] = randint(0, K-1)
            else:
                matrix[a][b] = randint(0, K-1)
    return matrix;


def summerize(matrix, K, Z):
    "Prints matrix and finds L for the respective matrix."
    "Calculates the sums of distances of all colors in the matrix and returns the min"
    "Objective is to maximize the minimum of these distances"

    lowest = sys.maxsize
    pairSums = {}
    for col in range(0, K):
        sum = sumClosestPairs(matrix, col, Z)
        pairSums[col] = sum
        if sum < lowest:
            lowest = sum
            i = [col]
        elif sum == lowest:
            i.append(col)


    pp.pprint(matrix)
    print("\nThe sums for each colors are: \n", pairSums)
    if(len(i) > 1):
        print("\nClosest colors for this coloring: ", i)
        print("Minimum L for these colorings: ", lowest)
    else:
        print("\nClosest color for this coloring: ", i[0])
        print("Minimum L for this coloring: ", lowest)

    return lowest;


def sumClosestPairs(matrix, color, Z):
    "find and sum the closest pair distances of same color in matrix"
    sum = 0
    for a, x in enumerate(matrix):
        for b, y in enumerate(x):
            if Z:
                for c, z, in enumerate(y):
                    if matrix[a][b][c] == color:
                        sum += findClosest(matrix, color, Z, a, b, c)
            else:
                if matrix[a][b] == color:
                    sum += findClosest(matrix, color, Z, a, b)
    return sum

def findClosest(matrix, color, Z, a2, b2, c2=None):
    "Finds the closest element of the same color in the matrix for both 2D and 3D"
    min = sys.maxsize
    for a, x in enumerate(matrix):
        for b, y in enumerate(x):
            if c2:
                for c, z in enumerate(y):
                    if int(a) == int(a2) and int(b) == int(b2) and int(c) == int(c2):
                        continue
                    if matrix[a][b][c] == color:
                        checkDist = dist(Z,a2,b2,c2,a,b,c)
                        if checkDist < min:
                            min = checkDist
            else:
                if int(a) == int(a2) and int(b) == int(b2):
                    continue
                if matrix[a][b] == color:
                    checkDist = dist(Z,a2,b2,a,b)
                    if checkDist < min:
                        min = checkDist

    return [0 if min == sys.maxsize else min][0]


def dist(Z, *points):
    "Calculates the distance between two points using basic algebra"
    "Supports both 2d and 3d elements"
    if Z:
        a = (points[0], points[1], points[2])
        b = (points[3], points[4], points[5])
        return ((((b[0]-a[0])**2)+((b[1]-a[1])**2)+((b[2]-a[2])**2))**(1/2))
    elif Z is None:
        a = (points[0], points[1])
        b = (points[2], points[3])
        return ((((b[0]-a[0])**2)+((b[1]-a[1])**2))**(1/2))
    else:
        print("Error in distance function")
        return 0


def print_variables(x,y,z,k):
    "Prints all user-set variables to screen"
    print("X is set to ", str(x))
    print("Y is set to ", str(y))
    if z:
        print("Z is set to ", str(z))
    print(k, " colors will be used\n")


def preprocess(argv):
    "Collects x,y,z,k values from user and returns them to the system"
    if len(argv) == 4:
        X = argv[1]
        Y = argv[2]
        K = argv[3]
        Z = None
    elif len(argv) == 5:
        X = argv[1]
        Y = argv[2]
        Z = int(argv[3])
        K = argv[4]
    else:
        X = input("Enter X dimension value: ")
        Y = input("Enter Y dimension value: ")
        choice = input("would you like a Z dimension?  [Y/N]: ")
        if choice != ('Y' or 'y'):
            Z = int(input ("Enter Z dimension value: "))
        else:
            Z = None
        K = input("Enter how many colors(K) you would like: ")
    while int(K) < 1:
        K = input("Please enter a positive value for colors (K > 0): ")

    return int(X),int(Y),Z,int(K)

def menu():
    print("------------------")
    print("Select Coloring:")
    print("O - Optimized")
    print("R - Randomized")
    print("Q - Quit")
    print("------------------")
    return input()

def main():
    "Accepts either command line arguments or will prompt user if none is given"
    "Calls random coloring and calculates the L for the colored matrix"

    X,Y,Z,K = preprocess(sys.argv)
    print_variables(X,Y,Z,K)

    while True:
        raw = create_matrix(X, Y, Z)
        choice = menu()

        if (choice == "r") or (choice == "R"):
            print("Random Coloring:")
            rand = random_coloring(raw, K, Z)
            summerize(rand, K, Z)
        elif (choice == "o") or (choice == "O"):
            print("Optimized Coloring:")
            opt = LHD.colorLatinHypercube(raw, K, Z)
            summerize(opt, K, Z)
        elif (choice == "q") or (choice == "Q"):
            break;
        else:
            print("Error in MENU, unsupported choice: ", choice)


def getL(matrix, K, Z):
    lowest = sys.maxsize
    pairSums = {}
    for col in range(0, K):
        sum = sumClosestPairs(matrix, col, Z)
        pairSums[col] = sum
        if sum < lowest:
            lowest = sum
    return lowest


def run(it = 1000):
    "runs a fixed matrix many times to compare results"
    "store max, min and avg? at least the best..."

    X = 80
    Y = 80
    Z = None
    K = 256

    RMAX = 0
    RMIN = sys.maxsize
    OMAX = 0
    OMIN = sys.maxsize
    RMEAN = 0
    OMEAN = 0
    for i in range(it):
        raw = create_matrix(X, Y, Z)
        rand = random_coloring(raw, K, Z)
        RL = getL(rand, K, Z)

        RMEAN += RL
        if RL > RMAX:
            RMAX = RL
        if RL < RMIN:
            RMIN = RL

        raw = create_matrix(X, Y, Z)
        opt = LHD.colorLatinHypercube(raw, K, Z)
        OL = getL(opt, K, Z)

        OMEAN += OL
        if OL > OMAX:
            OMAX = OL
        if OL < OMIN:
            OMIN = OL

    OMEAN = OMEAN/it
    RMEAN = RMEAN/it

    print("Stats over ", it, " iterations")
    print("Random Max: ", RMAX)
    print("Random Min: ", RMIN)
    print("Random Avg: ", RMEAN)
    print("Opt Max: ", OMAX)
    print("Opt Min: ", OMIN)
    print("Opt Avg: ", OMEAN)




run()

"RUNS THE PROGRAM"
#main()

