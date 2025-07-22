import numpy as np

# Array Aggregations
matrix = np.array([[1,2], [3,4]])
print(matrix)
print(np.sum(matrix))
print(np.sum(matrix,axis=0)) #sum across Y-axis (vertical)
print(np.sum(matrix,axis=1)) #sum across X-axis (horizontal)
print(10*"+-*-+","\r\n")

# Mean, Median, Std Dev
a = np.array([1,2,4,5,6])
print(a.mean())
print(np.mean(a))  #note that mean works both ways
print(np.median(a))
print(np.std(a))
print(10*"+-*-+","\r\n")

#Broadcasting
a = np.array([[1],[2],[3]])
print("a.shape: ",a.shape)
b = np.array([10,20,30])
print("b.shape: ",b.shape)
print(a + b)
print(10*"+-*-+","\r\n")

# Matrix Multiplication
# Remember that the multiplication of the shape (n1,m1) and (n2,m2) will result in the shape (n1,m2), given m1 == n2
a1 = np.array([[1,2],[3,4]])
print("a1.shape: ",a1.shape)
a2 = np.array([[2,0],[5,7]])
print("a2.shape: ",a2.shape)
print(np.matmul(a1,a2))

a3 = np.array([[1,2],[3,4]])
print("a3.shape: ",a3.shape)
a4 = np.array([[2],[0]])
print("a4.shape: ",a4.shape)
print(np.matmul(a3,a4))

# This will raise an error because m1 != n2, i.e., 4 != 2
A = np.random.rand(3, 4)
print(A)
B = np.random.rand(2, 5)
print(B)
# np.matmul(A, B)  #error
print(10*"+-*-+","\r\n")

#Random Numbers
print(np.random.rand(2, 3))
print(np.random.randn(3, 3))
print(np.random.randint(0, 100, size=(3, 2)))