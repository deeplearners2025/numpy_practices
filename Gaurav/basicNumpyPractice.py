import numpy as np
a1d = np.array([1,2,3])
print("One D array : \r\n", a1d)
print(10*"+-*-+","\r\n")

a2d = np.array([[1,2], [3,4]])
print("Two D array : \r\n", a2d)
print(10*"+-*-+","\r\n")

a3d = np.array([[[1,2], [3,4]],[[111,222], [333,444]]])
print("Three D array : \r\n", a3d)
print(10*"+-*-+","\r\n")

print(np.zeros((2,3),int))
print(np.zeros((2,3),str))

print(np.ones((2,3),str))
print(np.ones((2,3),int))
print(10*"+-*-+","\r\n")

print(np.arange(1,10,2))
print(np.arange(1,13).reshape((3,4))) #the count in the range of numbers must match the shape size
print(10*"+-*-+","\r\n")

x = np.array([1,2,3])
y = np.array([4,5,6])
print ("Addition: ", x + y)
print ("Subtraction: ", y - x)
print ("Multiplication: ", x * y)
print ("Division: ", y/x)
print ("Dot product: ", np.dot(x,y))
print(10*"+-*-+","\r\n")
