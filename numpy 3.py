import numpy as np
rows=int(input("enter number of rows"))
colls=int(input("enter number of cols"))
t=[]
for i in range(rows):
    v=list(map(int,input().split()))
    t.append(v)
n6=np.array(t)
print(n6)