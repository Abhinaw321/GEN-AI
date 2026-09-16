# mini project
students=[]
while True:
  print("1. Add Student")
  print("2. View Student")
  print("3. Search Student")
  print("4. Find max marks with name")
  print("5. Exit")
  ch=int(input("enter ur choice:"))
  if ch==1:
    name=input("enter name:")
    marks=int(input("enter marks:"))
    students.append((name,marks))
    print("Student added Successfully")
  elif ch==2:
    print(students)
  elif ch==3:
    name=input("enter name:")
    for s in students:
      if s[0]==name:
        print(s)
      else:
        print("student not found")
  elif ch==4:
    max_marks=0
    max_name=""
    for s in students:
      if s[1]>max_marks:
        max_marks=s[1]
        max_name=s[0] 
        print(max_name,max_marks)
      else:
        print("no student found")
  elif ch==5:
      print("exiting the program")
      break
  else:
      print("invalid choice")