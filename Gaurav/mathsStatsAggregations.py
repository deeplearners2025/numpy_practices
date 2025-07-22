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

#Broadcasting
