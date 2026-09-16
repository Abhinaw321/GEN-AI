"""
Product Billing and Discount Management System

Features:
1. Add products
2. View all products with prices
3. Calculate GST and final bill
4. Apply discounts based on the subtotal
"""

GST_RATE = 18
products = []


def add_product():
    name = input("Enter product name: ").strip()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per item: "))

    if not name or quantity <= 0 or price < 0:
        print("Enter a valid name, quantity, and price.")
        return

    products.append({
        "name": name,
        "quantity": quantity,
        "price": price,
    })
    print("Product added successfully!")


def view_products():
    if not products:
        print("No products found!")
        return

    print("\n----- PRODUCT DETAILS -----")
    print(f"{'No.':<5}{'Product':<20}{'Quantity':<10}{'Price':<12}{'Amount':<12}")

    for number, product in enumerate(products, start=1):
        amount = product["quantity"] * product["price"]
        print(
            f"{number:<5}{product['name']:<20}"
            f"{product['quantity']:<10}{product['price']:<12.2f}{amount:<12.2f}"
        )


def calculate_bill():
    if not products:
        print("No products found!")
        return

    subtotal = 0
    for product in products:
        subtotal += product["quantity"] * product["price"]

    if subtotal >= 3000:
        discount_rate = 10
    elif subtotal <= 2000:
        discount_rate = 6
    else:
        discount_rate = 0

    discount = subtotal * discount_rate / 100
    taxable_amount = subtotal - discount
    gst = taxable_amount * GST_RATE / 100
    final_amount = taxable_amount + gst

    print("\n----- BILL SUMMARY -----")
    print(f"Subtotal:       Rs. {subtotal:.2f}")
    print(f"Discount ({discount_rate}%): Rs. {discount:.2f}")
    print(f"GST ({GST_RATE}%):       Rs. {gst:.2f}")
    print(f"Final Amount:    Rs. {final_amount:.2f}")


while True:
    print("\n===== PRODUCT BILLING SYSTEM =====")
    print("1. Add Product")
    print("2. View All Products")
    print("3. Calculate GST and Final Bill")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        try:
            add_product()
        except ValueError:
            print("Quantity and price must be valid numbers.")
    elif choice == 2:
        view_products()
    elif choice == 3:
        calculate_bill()
    elif choice == 4:
        print("Program ended!")
        break
    else:
        print("Invalid choice!")
