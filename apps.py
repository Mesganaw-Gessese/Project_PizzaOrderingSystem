


sizeP = {
"s" : 40,
"m" : 50,
"l" : 60,
"xl" : 75

}


sum = 0
def choice():
    menu = input("""
           press 'S' for small size (4 slices)
           press 'M' for medium size (6 slices)
           press 'L' for large size (8 slices)
           press 'XL' for extra large (8 large slices
           please choose your order: """)
    return (menu)


x = choice()
def quantity():
    global sum
    pizzaNumber = int(input("How many pizzas do you want? "))
    sum += (sizeP[x] * pizzaNumber) - sizeP[x]
    return (sum)



def extras():
    global sum
    extra = input("Do you want extra y/n? ")
    if extra == "y":
      sum += (sizeP[x] + 2) - sizeP[x]
    return (sum)

def contiunation():
    con = input("do you want to continue y/n? ")
    if con == "n":
        exit()
    else:
        while True:
           choice()
           quantity()
           extras()
           stoping = input("do you want to continue again y/n? ")
           if stoping == "n":
               break



def delivery():
    global sum
    city = input("Do you live in Bear sheva y/n? ")
    if city == "y":
        sum += sizeP[x] + 20
    else:
        sum = sizeP[x] + 60


def totalPrice():
    from utilities import playGame
    global sum
    print("The total price with delivery is: ", sum)
    print("The total price with discount is", sum - (sum * (playGame() / 100)), "$")



