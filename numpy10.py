# axis=0 means up and down
# axis=1 means left and right 
import numpy as np
n=np.array([
    [10,20,30],
    [40,50,60]
])
print(n)
print(np.sum(n,axis=0))
print(np.sum(n,axis=1))

# 3d
n=np.array([
    [[10,20,30],
     [40,50,60]],
    [[70,80,90],
     [100,110,120]]
])

print(n)
print(np.sum(n,axis=0))
print(np.sum(n,axis=1))
