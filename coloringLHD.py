#!/bin/env python3

#############################################################
# Module for coloring matrix with distributed latin			#
# hypercube design. 										#
#															#
# coloringLHD_v01.py 							            #
# By: Jennifer Yarboro										#
# 10/16/2016												#
#															#
#############################################################

import sys
import math
import pprint

def columnSteps(numOfColors):
    ''' Returns the number of column steps to the right based
    on the number of colors in the matrix.
    '''
    generateXn = True

    Xn_1 = 1
    n = Xn_2 = Xn_3 = 0

    while generateXn:
        Xn = Xn_3 + Xn_2 + Xn_1

        if numOfColors < Xn:
            steps = n - 1
            generateXn = False
        else:
            Xn_3 = Xn_2
            Xn_2 = Xn_1
            Xn_1 = Xn
            n += 1

    return steps


def colorLatinHypercube(matrix, K, Z):
    ''' Method of determining color dispersion based on latin hypercube
    designs. For increasing n, each row begins the string at an
    increasing n column steps to the right.

    Pattern:

    Xn = X(n-1) + X(n-2) + X(n-3)

    where n is the number of colors and Xn - 1 is the
    number of column steps to the right.

    X1 = 1 colors 			0 column steps

    X2 = 2 to 3 colors 		1 column steps

    X3 = 4 to 6 colors 		2 column steps

    X4 = (4+2+1)
        = 7 to 12 colors	3 column steps

    X5 = (7+4+2)
        = 13 to 23 colors	4 column steps

        ... 				...

        Xn = X(n-1) + X(n-2) + X(n-3)
            = Xn to (X(n+1) - 1) colors

                            n-1 column steps
    '''

    # get number of column steps to the right
    steps = columnSteps(K)
    #print (steps)

    # assign the matrix a color number based on formula
    for a, x in enumerate(matrix):
        for b, y in enumerate(matrix[a]):
            if Z:
                for c, z in enumerate(matrix[b]):

                    if (K + a * (K - steps) + b + 1 + c * (K - steps - 1)) % K == 0:
                        matrix[a][b][c] = K - 1
                    else:
                        matrix[a][b][c] = ((K + a * (K - steps) + b + 1 + c * (K - steps - 1)) % K) - 1


            else:
                if (K + a * (K - steps) + b + 1) % K == 0:
                    matrix[a][b] = K - 1
                else:
                    matrix[a][b] = ((K + a * (K - steps) + b + 1) %K) - 1

    #pprint.pprint(matrix)
    return matrix

#dummy = matrix = [[-1 for x in range(20)] for y in range(8)]
#colorLatinHypercube(matrix, 8)
