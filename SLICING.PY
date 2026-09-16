T=[11,22,33,44,55,66,76,88,98,101]
print(T[0:3]) #output: [11, 22, 33]
print(T[:6]) #output: [11, 22, 33, 44, 55, 66]
print(T[3:]) #output: [44, 55, 66, 76, 88, 98, 101]
print(T[::2]) #output: [11, 33, 55, 76, 98]
print(T[2::3]) #output: [33, 66, 98]
print(T[::-1]) #output: [101, 98, 88, 76, 66, 55, 44, 33, 22, 11]
print(T[1:8:2]) #output: [22, 44, 66, 88]
print(T[1:8:3]) #output: [22, 55, 88]
print(T[1:8:4]) #output: [22, 66]
print(T[1:8:5]) #output: [22, 88]

for i in T:
    if i % 2 == 0:
        print(i)
