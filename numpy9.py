import numpy as np
n=np.array([10,20,30,40,50])
print(np.cumsum(n))
print(np.cumprod(n))

t=np.array([[1,2],[4,5]])
print(np.cumsum(t))
print(np.cumprod(t))

# 3d 
n=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(np.cumsum(n))
print(np.cumprod(n))