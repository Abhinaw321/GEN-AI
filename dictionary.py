#DICTIONARY
d1= dict()
print(type(d1))

d={
    "id":1,
    "name":"suresh",
    "course":"java",
    "age":25,
    "city":"mohali"
}
print(d)

k=[1,2,3,4]
v=["pitter","david","warner","parker"]
d=dict(zip(k,v))
print(d)    
print(d.keys())
print(d.values())
print(d.items())

d=["id","name","post","salary"]
c=[101,"sonu","developer",25000]
d=dict(zip(d,c))
print(d)
print(d["name"])
print(d.get("salary"))

d={
    "id":11,
    "name":"hari",
}
print(d)
#add
d["course"]="java"
print(d)
#update #remove 
d.update({"course":"python"})
print(d)
d.pop("course")
print(d)    

