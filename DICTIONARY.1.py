supplier = dict()

while True:
    print("1. Add")
    print("2. View")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        sid = int(input("Enter Supplier id: "))
        sname = input("Enter the name of supplier: ")
        item = input("Enter product: ")
        qty = int(input("Enter quantity: "))
        rate = float(input("Enter price: "))

        supplier[sid] = {
            "name": sname,
            "product": item,
            "quantity": qty,
            "price": rate
        }

        print("Supplier added Successfully!!")

    elif choice == 2:
        if supplier:
            for sid, sup in supplier.items():
                print("Supplier id:", sid)
                print("Supplier Name:", sup["name"])
                print("Product:", sup["product"])
                print("Quantity:", sup["quantity"])
                print("Price:", sup["price"])
        else:
            print("No Record found")

    elif choice == 3:
        search_id = int(input("Enter id: "))

        if search_id in supplier:
            sup = supplier[search_id]

            print("Supplier id:", search_id)
            print("Supplier Name:", sup["name"])
            print("Product:", sup["product"])
            print("Quantity:", sup["quantity"])
            print("Price:", sup["price"])
        else:
            print("Supplier not found")

    elif choice == 4:
        update_id = int(input("Enter id: "))

        if update_id in supplier:
            sname = input("Enter name: ")
            item = input("Enter product: ")
            qty = int(input("Enter quantity: "))
            rate = float(input("Enter price: "))

            supplier[update_id] = {
                "name": sname,
                "product": item,
                "quantity": qty,
                "price": rate
            }

            print("Supplier updated Successfully!!")
        else:
            print("Id Not found")

    elif choice == 5:
        delete_id = int(input("Enter id: "))

        if delete_id in supplier:
            del supplier[delete_id]
            print("Supplier deleted!!")
        else:
            print("Id not found")

    elif choice == 6:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")