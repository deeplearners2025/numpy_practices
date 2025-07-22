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
