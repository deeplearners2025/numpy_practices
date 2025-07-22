import numpy as np

#Conditional Replacement
ar = np.array([1,2,3,4,5,6])
ar[ar<3] = 100
ar[ar>5] = 200
print(ar)
print(10*"+-*-+","\r\n")

#Unique Values and Counting
a = np.array([1, 2, 2, 3, 3, 3,3])
uniq, counts = np.unique(a, return_counts=True)
print(uniq)
print(counts)
print(dict(zip(uniq,counts)))
print(10*"+-*-+","\r\n")

#Solve Linear Equations
# 2x + y = 5,  x + 3y = 6
A = np.array([[2, 1], [1, 3]])
B = np.array([5, 6])
x = np.linalg.solve(A, B)
print(x)
print(10*"+-*-+","\r\n")

#Apply Custom Function with vectorize

def custom_fn(x,y,z):
    return x**2 + y*2 + z

vect_testFn = np.vectorize(custom_fn)
a = np.array([[1],[2],[3]])
b = np.array([[4],[5],[6]])
c = np.array([[7],[8],[9]])
print(vect_testFn(a,b,c))

a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.array([7,8,9])
print(vect_testFn(a,b,c))

