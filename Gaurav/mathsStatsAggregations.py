import numpy as np

matrix = np.array([[1,2], [3,4]])
print(matrix)
print(np.sum(matrix))
print(np.sum(matrix,axis=0)) #sum across Y-axis (vertical)
print(np.sum(matrix,axis=1)) #sum across X-axis (horizontal)
print(10*"+-*-+","\r\n")