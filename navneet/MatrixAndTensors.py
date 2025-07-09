import numpy as np

arr1 = np.array([1, 2, 3, 4, 5]) # using list

print("1D array using list", arr1)

arr2= np.array((1,2,3,4,5)) # using tuple
print("1D array using tuple", arr2)

# creating 2D array using set :
arr3=np.array(((1,2),(3,4), (4,5), (6,7)))

print("2D array using set", arr3)


# creating 3D array using list

arr4=np.array([[[1,2],[2,3]],[[4,5],[6,7]]])

print("3D array using list", arr4)