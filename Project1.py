import sys

print("Hello, welcome to steve's pizza, where pizza rules \n")
print("Our menu ranges from: \n\nsmall(s) for $9.99, medium(m) for 14.99 or large(l) for 19.99 \nwith upto 5 toppings for an added fee:")
print("0) No toppings 1) Pepperoni +1.99 \n2) Supreme +2.99 \n3) Hawaiian +1.99 \n4) Meatlovers +2.99 \n5) BBQ chicken +1.99\n")
print("Please select from the menu:")


totalBill = 0
SPIZZA = 9.99
MPIZZA = 14.99
LPIZZA = 19.99
REGTOPPINGS = 1.99
PREMTOPPINGS = 2.99

numPizza = input("How many Pizzas would you like: ")
if (not numPizza.isdigit() or int(numPizza) < 0):
    print("Please try again!")
    sys.exit()

for i in range(0,int(numPizza)):
    pizzaSize = input("Please select the pizza size: (s, m or l) ").lower()
    pizzaTopping = input("Please select the topping: ")

    if (pizzaSize == "s" and pizzaTopping == "0"):
        pizzaBill = SPIZZA
    elif (pizzaSize == "s" and pizzaTopping == "1") or (pizzaSize == "s" and pizzaTopping == "3") or (pizzaSize == "s" and pizzaTopping == "5"):
        pizzaBill = SPIZZA + REGTOPPINGS
    elif (pizzaSize == "s" and pizzaTopping == "2") or (pizzaSize == "s" and pizzaTopping == "4"):
        pizzaBill = SPIZZA + PREMTOPPINGS
    elif (pizzaSize == "m" and pizzaTopping == "0"):
        pizzaBill = MPIZZA
    elif (pizzaSize == "m" and pizzaTopping == "1") or (pizzaSize == "m" and pizzaTopping == "3") or (pizzaSize == "m" and pizzaTopping == "5"):
        pizzaBill = MPIZZA + REGTOPPINGS
    elif (pizzaSize == "m" and pizzaTopping == "2") or (pizzaSize == "m" and pizzaTopping == "4"):
        pizzaBill = MPIZZA + PREMTOPPINGS
    elif (pizzaSize == "l" and pizzaTopping == "0"):
        pizzaBill = LPIZZA
    elif (pizzaSize == "l" and pizzaTopping == "1") or (pizzaSize == "l" and pizzaTopping == "3") or (pizzaSize == "l" and pizzaTopping == "5"):
        pizzaBill = LPIZZA + REGTOPPINGS
    elif (pizzaSize == "l" and pizzaTopping == "2") or (pizzaSize == "l" and pizzaTopping == "4"):
        pizzaBill = LPIZZA + PREMTOPPINGS
    else:
        if (not pizzaSize == "s" or pizzaSize == "m" or pizzaSize == "l") or (not pizzaTopping.isdigit() or int(pizzaTopping) < 0 or int(pizzaTopping) > 5):
            print("Theres an error in your selections, please try again")
            sys.exit()
            
     
    totalBill += pizzaBill


print("\nCurrently, your total is $:" + str(totalBill) + ".\n")

finalUserInput = int(input("Would you like to proceed? Press 1)yes or 2)no "))

if (finalUserInput == 1):
    print("Thank you for your purchase of $" + str(totalBill) + ". Your order is on the way!")
elif (finalUserInput == 2):
    print("Sorry to see you go.")
    sys.exit()
else:
    print("There has been an error, goodbye!")
    sys.exit()

