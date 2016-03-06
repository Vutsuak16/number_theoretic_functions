__name__ = "vutsuak"

from scipy.linalg import circulant
from numpy.linalg import det
import numpy as np
from sympy.ntheory import factorint


# tau is the number theoretic function that counts the number of divisors of a given integer
# we can also use formula to solve this which we will use in prime-factors

def mobius(n):
    dict = factorint(n)
    factor_count = list(dict.values())
    for i in factor_count:
        if i != 1:
            return 0
    if n == 1:
        return 1
    else:
        return (-1) ** (len(factor_count))


def matrix():
    determinant = []
    circulant_matrix = []
    for i in range(2, 21):
        array = []
        for j in range(1, i + 1):
            l = mobius(j)
            array.append(l)

        circulant_matrix.append(circulant(array))
        determinant.append(det(np.transpose(circulant_matrix[-1])))
    for i in range(len(determinant)):
        print(np.transpose(circulant_matrix[i]))
        print("the determinant of circulant matrix  for n= " + str(i + 2) + " is " + str(determinant[i]))


if __name__ == "vutsuak":
    matrix()
