__name__ = "vutsuak"

from scipy.linalg import circulant
from numpy.linalg import det, eigvals
import numpy as np
from sympy.ntheory import factorint
from pandas import DataFrame


def sigma(n):
    ct = 0
    for i in range(1, n + 1):
        if n % i == 0:
            ct += i
    return ct


def prime_factors(n):
    dict = factorint(n)
    return dict


def matrix():
    eigenvalues = []
    determinant = []
    circulant_matrix = []
    for i in range(2, 21):
        array = []
        for j in range(1, i + 1):
            l = sigma(j)
            array.append(l)

        circulant_matrix.append(circulant(array))
        eigenvalues.append(eigvals(circulant_matrix[-1]))
        determinant.append(det(np.transpose(circulant_matrix[-1])))
    i = range(2, 21)
    df = DataFrame({'n': i, 'determininant': determinant, 'eigenvalues': eigenvalues})
    df.to_excel('rough.xlsx', index=False)
    for i in range(len(determinant)):
        print(np.transpose(circulant_matrix[i]))
        print("the eigenvalues of circulant matrix  for n= " + str(i + 2) + " is " + str(eigenvalues[i]))
        print("the determinant of circulant matrix  for n= " + str(i + 2) + " is " + str(determinant[i]))
        print()


if __name__ == "vutsuak":
    matrix()
