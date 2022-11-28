

print("Welcome to our pizza house:")

age = int(input("Please enter your age: "))
while age < 18:
    print("You are under age you can't order \n "
          "Thanks for your visit Have A Good Day!:")
    break
else:
    # from apps import *
    # choice()
    from apps import quantity
    quantity()
    from apps import extras
    extras()
    from apps import contiunation
    contiunation()
    from apps import delivery
    delivery()
    from apps import totalPrice
    sum = totalPrice()


