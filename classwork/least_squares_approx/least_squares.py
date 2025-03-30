import numpy as np

X = np.asarray([-0.94, -0.34, 0.06, 0.16, 1.06])
Y = np.asarray([-0.42, -0.42, 0.58, -1.42, 1.68])

def correlation_coefficient(A, B):
    return (np.dot(A,B) / (np.linalg.norm(X) * np.linalg.norm(Y)))

print(correlation_coefficient(X,Y))