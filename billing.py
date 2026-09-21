# BILLING PROJECT

product = []

while True:
    print("1. Add Product")
    print("2. View All Products")
    print("3. GST Calculate")
    print("4. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        name = input("Enter product name: ")
        quantity = int(input("Enter product quantity: "))
        price = float(input("Enter product price: "))

        product.append((name, quantity, price))

        print("Product added successfully!")

    elif ch == 2:
        if len(product) == 0:
            print("No products available.")
        else:
            for p in product:
                total = p[1] * p[2]
                print(f"Product Name: {p[0]}, Quantity: {p[1]}, Price: {p[2]}, Total: {total}")

    elif ch == 3:
        subtotal = sum(p[1] * p[2] for p in product)

        if subtotal > 3000:
            discount = subtotal * 10 / 100

        elif subtotal > 2000:
            discount = subtotal * 5 / 100

        else:
            discount = 0

        amount_after_discount = subtotal - discount
        gst = amount_after_discount * 18 / 100
        final_amount = amount_after_discount + gst

        print(f"Subtotal: {subtotal}")
        print(f"Discount: {discount}")
        print(f"GST: {gst}")
        print(f"Final Amount: {final_amount}")

    elif ch == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. do it again u enter wrong dataa55uuuuuuuu.")