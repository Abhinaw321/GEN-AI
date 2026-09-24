import pandas as pd
import numpy as np

data=[
    [1,"david","developer",2500,"noida"],
    [2,"pitter","programmer",45000,"delhi"],
    [3,"kumar","hr",32000,"banglore"],
    [4,"kumar","trainer",16000,"chennai"],
    [5,"hari","manager",50000,"delhi"]
]

df=pd.DataFrame(data,columns=["Id","Name","Post","Salary","City"])

print(df)


# 2nd way - 2D Dataset

emp={
    "id":[1,2,3,4,5],
    "name":["ram","shyam","nikhil","david","bitter"],
    "post":["developer","hr","clerk","programmer","trainer"],
    "salary":[130000,340000,22000,32000,17000],
    "city":["noida","delhi","mumbai","banglore","kerela"]
}

df=pd.DataFrame(emp)

print(df)


# get only name
print(df["name"])


# get top 2
print(df.head(2))


# get last 2
print(df.tail(2))


# whose salary is between 25000 and 30000
print(df[df["salary"].between(25000,30000)])
#GET SALARY B/W 35000 TO 25000
print(df[df["salary"].between(35000,25000)])
#how ro get name,post and salary
print(df[["name", "post", "salary"]])
#how to add columns 9th interview question 
df["age"] = [21, 22, 23, 24, 25]
 
