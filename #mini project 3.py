class ShoppingCart:

    class Product:
        def __init__(self, name, price, quantity):
            self.name = name
            self.price = price
            self.quantity = quantity

        def total(self):
            return self.price * self.quantity

    def __init__(self):
        self.cart = []

    def add_product(self):
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))

        P = self.Product(name, price, quantity)
        self.cart.append(P)

        print("Product added successfully")

    def show_cart(self):
        for c in self.cart:
            print(c.name, c.price, c.quantity, c.total())


shop = ShoppingCart()

shop.add_product()
shop.show_cart()