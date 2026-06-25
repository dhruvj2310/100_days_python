print("Welcome to Python Pizza Deliveries! 🍕")

size = input("\nWhat size do you want? S, M, L: ")
pepperoni = input("Do you want to add pepperoni? y or n: ")
extra_cheese = input("Do you want to add extra cheese? y or n: ")

bill = 0

## SIZE ##
if size == "S":
    bill += 15
    print("\nSmall pizza $15.")

elif size == "M":
    bill += 20
    print("\nMedium pizza $20.")

elif size == "L":
    bill += 25
    print("\nLarge pizza $25.")

else:
    print("\nPlease select a valid size.")

## PEPPERONI ##
if pepperoni == "y":
    bill += 2
    print("Pepperoni $2.")

elif pepperoni == "n":
    print("No pepperoni.")

else:
    print("Please enter y or n.")

## EXTRA CHEESE ##
if extra_cheese == "y":
    bill += 1
    print("Extra Cheese $1.")

elif extra_cheese == "n":
    print("No extra cheese.")

else:
    print("Please enter y or n.")

print(f"\nYour total bill is ${bill}")