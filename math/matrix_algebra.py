# Matrix Algebra
import numpy as np

A = np.array([[1,2,3],[2,7,4]])
B = np.array([[1,-1],[0,1]])
C = np.array([[5,-1],[9,1],[6,0]])
D = np.array([[3,-2,-1], [1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array([1,8,0,5]).reshape(-1,1)


# DIMENSIONS
A.shape
B.shape
C.shape
D.shape

u.shape
v.shape
w.shape


# VECTOR OPERATIONS

u + v
u - v
6*u
u.dot(v)
np.linalg.norm(u)


# MATRIX OPERATIONS
A + C # Error
A-C.T
C.T + 3*D
B.dot(A)
B.dot(A.T) # error

