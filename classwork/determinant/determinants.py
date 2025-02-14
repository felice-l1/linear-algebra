import numpy as np
import random

M = np.random.randint(-100,100,size =(4,4))
print(M)
def determinant(M):
    if len(M) == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    else:
        tot = 0
        for i in range(len(M[0])):
            tot += (-1)**(i) * M[0][i] * determinant(np.column_stack((M[1:, 0:i], M[1:, i+1:])))
        return tot

print(determinant(M))
print(np.linalg.det(M))

# first 25 primes
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# p = random.randint(0, len(primes) - 1)

def mod_matrix(M, p):
    N = np.zeros(np.shape(M))
    for i in range(len(M)):
        for j in range(len(M[0])):
            N[i][j] = M[i][j] % p
    return N


M = np.array([[1, 2, 3], [3, 4, 5], [4, 6, 8]])
# returns % of matrices which are invertible 
def percent_invertible(M, primes):
    total = 0
    invertible = 0
    for p in primes:
        N = mod_matrix(M, p)
        if determinant(N) != 0:
            invertible += 1
            total += 1
    return invertible/total * 100
print(mod_matrix(M, 103))
print(determinant(M))
print(determinant(mod_matrix(M, 103)))
print(percent_invertible(M, primes))
