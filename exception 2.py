def test():
    try:
        a = int(input("Enter number: "))
        b = int(input("Enter number: "))
        print(a / b)
    except ValueError:
        print("Enter numbers only")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    try:
        x = [10, 20]
        print(x[3])
    except IndexError:
        print("Index not found")


test()