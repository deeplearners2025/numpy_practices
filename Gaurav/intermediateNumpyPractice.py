import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[1:4] )
print(10*"+-*-+","\r\n")

print(a[a>5])
print(10*"+-*-+","\r\n")

#Modify one value
a[4] = 99
print(a)

# Stack Arrays Vertically and Horizontally
arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([[5,6]])
print(np.vstack((arr1,arr2)))
print(arr1)
print(arr1.T)
print(np.hstack((arr1.T,arr2.T)))
# print(np.hstack((arr1,arr2))) #ValueError: all the input array dimensions except for the concatenation axis must match exactly, but along dimension 0, the array at index 0 has size 2 and the array at index 1 has size 1

