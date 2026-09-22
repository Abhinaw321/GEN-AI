try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    c = a / b
    print(c)

except ZeroDivisionError:
    print("exception generated")

finally:
    print("this is finally block")