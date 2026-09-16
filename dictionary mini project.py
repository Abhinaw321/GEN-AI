#implementation of dictionary minor project
employee=dict()
while True:
    print("1. Add")
    print("2. Display")
    print("3. Search")  
    print("4. update")
    print("5. Delete")
    print("6. Exit")
    ch=int(input("Enter your choice:"))

    if ch==1:
        id=int(input("Enter id:"))
        name=input("Enter name:")
        post=input("Enter post:")
        salary=int(input("Enter salary:"))
        employee[id]={"name":name,"post":post,"salary":salary}
        print("Employee added successfully")
    elif ch==2:
        if employee:
            for id, emp in employee.items():
                print("Emp id:", id)
                print("Name:", emp["name"])
                print("Post:", emp["post"])
                print("Salary:", emp["salary"])
                print("-------------------------")
        else:
            print("No employee records found.")
    elif ch==3:
        id=int(input("Enter id to search:"))
        if id in employee:
            emp=employee[id]
            print("Emp id:", id)
            print("Name:", emp["name"])
            print("Post:", emp["post"])
            print("Salary:", emp["salary"])
        else:
            print("Employee not found.")    
            elif ch==4:
        id=int(input("Enter id to update:"))
        if id in employee:
            name=input("Enter new name:")
            post=input("Enter new post:")
            salary=int(input("Enter new salary:"))
            employee[id]={"name":name,"post":post,"salary":salary}
            print("Employee updated successfully")
        else:
            print("Employee not found.")
    elif ch==5:
        id=int(input("Enter id to delete:"))
        if id in employee:
            del employee[id]
            print("Employee deleted successfully")
        else:
            print("Employee not found.")
    elif ch==6:
        print("Exiting the program.")
        break