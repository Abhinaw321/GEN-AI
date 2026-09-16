#tuple 
T1=()
T2=(1,2,3,4)
T3=11,22,33
print(T3)
T4=(11,22,[101,102])
T5=((1,2,3),("sun","mon","tue"))
T=(1,2,3,4,5,6,7,8)
#count,index,remove,pop,sort,reverse,append,extend,insert
# 1. COUNT
print(T.count(5))

# 2. INDEX
print(T.index(5))

# 3. LENGTH
print(len(T))

# 4. MAX
print(max(T))

# 5. MIN
print(min(T))

# 6. SUM
print(sum(T))

# 7. SORTTED
print(sorted(T))

# 8. REVERSE
print(tuple(reversed(T)))

#HOW TO DELETE AN ELEMENT FROM TUPLE
T = (1, 2, 3, 4, 5)
L = list(T)
L.remove(3)
T = tuple(L)
print(T)

#CAN YOU EXPLAIN HOW LIST IS MUTABLE AND TUPLE IS IMMUTABLE
L = [1, 2, 3]
L[0] = 10  
print(L)

T = (1, 2, 3)
T[0] = 10  
print(T)

