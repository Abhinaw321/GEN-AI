import numpy as np
#  why slicing in numpy
a1 = np.array([1,2,3,4,5,6,7,8,9])
# slicing in 1D
print(a1[5])
print(a1[1:5:2])
print(a1[::-1])

a2 = np.array([[1,2,3,4],[4,5,6,7]])
# slicing in 2d array
print(a2[0][1:3])
print(a2[1][:3])
print(a2[1][::-1])


a3 = np.array([[[1,2,3,4],[4,5,6,7]]])
# slicing in 3d
print(a3[0][1][:3])

print(a3[0][1][::-1])
print(a3[0][0][1:3])
print(a3[0][0][-2])
print(a3[0][1][1])
print(a3[0][1][-1])