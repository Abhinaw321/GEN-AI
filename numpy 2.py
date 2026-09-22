import numpy as np

# 1D Array
n1 = np.array([1,2,3,4,5])
print("1D Array:")
print(n1)
print("Size:", n1.size)
print("Shape:", n1.shape)
print("Dimension:", n1.ndim)


# 2D Array
n2 = np.array([[1,2,3],
               [4,5,6]])
print("\n2D Array:")
print(n2)
print("Size:", n2.size)
print("Shape:", n2.shape)
print("Dimension:", n2.ndim)


# 3D Array
n3 = np.array([[[1,2,3],
                [4,5,6]],
               
               [[7,8,9],
                [10,11,12]]])

print("\n3D Array:")
print(n3)
print("Size:", n3.size)
print("Shape:", n3.shape)
print("Dimension:", n3.ndim)
n4 = np.array([[[[1,2],
                 [3,4]],

                [[5,6],
                 [7,8]]],


               [[[9,10],
                 [11,12]],

                [[13,14],
                 [15,16]]]])

print("4D Array:")
print(n4)
print("Size:", n4.size)
print("Shape:", n4.shape)
print("Dimension:", n4.ndim)
n5=np.array(list(map(int,input("enter elements of 4D array:").split())))
print(n5)
n=int(input("enter the number of elements:"))
n6=np.array([(int(input("enter element:"))) for i in range(n)])
print(n6)